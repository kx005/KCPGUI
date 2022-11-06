import datetime

from PyQt5.QtCore import Qt, QObject
from PyQt5.QtWidgets import QDialog, QSizePolicy, QLayout
from legendary.models.game import InstalledGame

from rare.ui.components.dialogs.sync_save_dialog import Ui_SyncSaveDialog
from rare.utils.misc import icon


class CloudSaveUtils(QObject):
    def __init__(self):
        super(CloudSaveUtils, self).__init__()
        self.latest_saves = {}
