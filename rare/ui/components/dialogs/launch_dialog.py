# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'launch_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets


class Ui_LaunchDialog(object):
    def setupUi(self, LaunchDialog):
        LaunchDialog.setObjectName("LaunchDialog")
        LaunchDialog.resize(400, 168)
        self.verticalLayout = QtWidgets.QVBoxLayout(LaunchDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title_label = QtWidgets.QLabel(LaunchDialog)
        self.title_label.setObjectName("title_label")
        self.verticalLayout.addWidget(self.title_label)
        self.image_prog_bar = QtWidgets.QProgressBar(LaunchDialog)
        self.image_prog_bar.setProperty("value", 0)
        self.image_prog_bar.setObjectName("image_prog_bar")
        self.verticalLayout.addWidget(self.image_prog_bar)
        self.image_info = QtWidgets.QLabel(LaunchDialog)
        self.image_info.setObjectName("image_info")
        self.verticalLayout.addWidget(self.image_info)
        self.steam_prog_bar = QtWidgets.QProgressBar(LaunchDialog)
        self.steam_prog_bar.setProperty("value", 0)
        self.steam_prog_bar.setObjectName("steam_prog_bar")
        self.verticalLayout.addWidget(self.steam_prog_bar)
        self.steam_info = QtWidgets.QLabel(LaunchDialog)
        self.steam_info.setObjectName("steam_info")
        self.verticalLayout.addWidget(self.steam_info)

        self.retranslateUi(LaunchDialog)
        QtCore.QMetaObject.connectSlotsByName(LaunchDialog)

    def retranslateUi(self, LaunchDialog):
        _translate = QtCore.QCoreApplication.translate
        LaunchDialog.setWindowTitle(_translate("LaunchDialog", "Dialog"))
        self.title_label.setText(_translate("LaunchDialog", "<h2>Launching Rare</h2>"))
        self.image_info.setText(_translate("LaunchDialog", "Downloading images"))
        self.steam_info.setText(_translate("LaunchDialog", "Getting Steam grades"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    LaunchDialog = QtWidgets.QDialog()
    ui = Ui_LaunchDialog()
    ui.setupUi(LaunchDialog)
    LaunchDialog.show()
    sys.exit(app.exec_())