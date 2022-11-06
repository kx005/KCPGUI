import os
from logging import getLogger

from PyQt5.QtCore import QThreadPool, QSettings
from PyQt5.QtWidgets import QWidget, QFileDialog, QVBoxLayout, QGroupBox, QFormLayout, QLabel, QPushButton, QSizePolicy, \
    QMessageBox, QCheckBox
from legendary.models.game import Game, InstalledGame

from rare.shared import LegendaryCoreSingleton
from rare.utils.extra_widgets import PathEdit
from rare.utils.misc import icon, WineResolver, get_raw_save_path
from rare.widgets.cloud_widget import CloudWidget

logger = getLogger("CloudSavesTab")


class CloudSavesTab(QWidget):
    def __init__(self, parent=None):
        super(CloudSavesTab, self).__init__(parent=parent)

        self.core = LegendaryCoreSingleton()
        self.settings = QSettings()
        self.game: Game = None
        self.igame: InstalledGame = None
        self.change = True

        self.setLayout(QVBoxLayout())
        self.settings_group = QGroupBox(self.tr("Options"))
        self.layout().addWidget(self.settings_group)
        self.settings_group.setLayout(QFormLayout())

        self.sync_cb = QCheckBox(self.tr("Automatically Sync"))
        self.settings_group.layout().addRow(None, self.sync_cb)

        self.cloud_save_path_edit = PathEdit(
            "",
            file_type=QFileDialog.DirectoryOnly,
            placeholder=self.tr("Cloud save path"),
            edit_func=lambda text: (True, text, None)
            if os.path.exists(text)
            else (False, text, PathEdit.reasons.dir_not_exist),
            save_func=self.save_save_path,
        )
        self.settings_group.layout().addRow(QLabel(self.tr("Save path")), self.cloud_save_path_edit)

        self.compute_save_path_button = QPushButton(icon("fa.magic"), self.tr("Auto compute save path"))
        self.compute_save_path_button.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        self.compute_save_path_button.clicked.connect(self.compute_save_path)
        self.settings_group.layout().addRow(None, self.compute_save_path_button)

        self.cloud_widget = CloudWidget()
        self.layout().addWidget(self.cloud_widget)

    def update_game(self, app_name: str):
        self.change = False
        self.game = self.core.get_game(app_name)
        self.igame = self.core.get_installed_game(app_name)

        if not self.game.supports_cloud_saves:
            self.setEnabled(False)
            self.cloud_save_path_edit.setText("")
            self.change = True
            return
        self.setEnabled(True)
        sync_cloud = self.settings.value(f"{self.game.app_name}/auto_sync_cloud", True, bool)
        self.sync_cb.setChecked(sync_cloud)
        self.cloud_save_path_edit.setText(self.igame.save_path or "")
        self.change = True

    def compute_save_path(self):
        if self.core.is_installed(self.game.app_name) and self.game.supports_cloud_saves:
            try:
                new_path = self.core.get_save_path(self.game.app_name)
            except Exception as e:
                logger.warning(str(e))
                resolver = WineResolver(get_raw_save_path(self.game), self.game.app_name)
                if not resolver.wine_env.get("WINEPREFIX"):
                    self.cloud_save_path_edit.setText("")
                    QMessageBox.warning(self, "Warning", "No wine prefix selected. Please set it in settings")
                    return
                self.cloud_save_path_edit.setText(self.tr("Loading"))
                self.cloud_save_path_edit.setDisabled(True)
                self.compute_save_path_button.setDisabled(True)

                app_name = self.game.app_name[:]
                resolver.signals.result_ready.connect(lambda x: self.wine_resolver_finished(x, app_name))
                QThreadPool.globalInstance().start(resolver)
                return
            else:
                self.cloud_save_path_edit.setText(new_path)

    def wine_resolver_finished(self, path, app_name):
        logger.info(f"Wine resolver finished for {app_name}. Computed save path: {path}")
        if app_name == self.game.app_name:
            self.cloud_save_path_edit.setDisabled(False)
            self.compute_save_path_button.setDisabled(False)
            if path and not os.path.exists(path):
                try:
                    os.makedirs(path)
                except PermissionError:
                    self.cloud_save_path_edit.setText("")
                    QMessageBox.warning(
                        None,
                        "Error",
                        self.tr("Error while launching {}. No permission to create {}").format(
                            self.game.app_title, path
                        ),
                    )
                    return
            if not path:
                self.cloud_save_path_edit.setText("")
                return
            self.cloud_save_path_edit.setText(path)
        elif path:
            igame = self.core.get_installed_game(app_name)
            igame.save_path = path
            self.core.lgd.set_installed_game(app_name, igame)

    def save_save_path(self, text):
        if self.game.supports_cloud_saves and self.change:
            self.igame.save_path = text
            self.core.lgd.set_installed_game(self.igame.app_name, self.igame)

