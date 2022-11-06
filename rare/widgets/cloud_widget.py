from PyQt5.QtWidgets import QWidget
from legendary.models.game import Game

from rare.shared import LegendaryCoreSingleton
from rare.ui.components.tabs.games.game_info.cloud_widget import Ui_cloud_widget
from rare.utils.misc import icon


class CloudWidget(QWidget, Ui_cloud_widget):
    def __init__(self):
        super(CloudWidget, self).__init__()
        self.setupUi(self)
        self.core = LegendaryCoreSingleton()
        self.game: Game = None

        self.icon_local.setPixmap(icon("mdi.harddisk", "fa.desktop").pixmap(128, 128))
        self.icon_remote.setPixmap(icon("mdi.cloud-outline", "ei.cloud").pixmap(128, 128))

    def update_game(self, app_name):
        self.game = self.core.get_game(app_name)
