# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rare/ui/components/dialogs/sync_save_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SyncSaveDialog(object):
    def setupUi(self, SyncSaveDialog):
        SyncSaveDialog.setObjectName("SyncSaveDialog")
        SyncSaveDialog.resize(648, 394)
        self.verticalLayout = QtWidgets.QVBoxLayout(SyncSaveDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title_label = QtWidgets.QLabel(SyncSaveDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy)
        self.title_label.setObjectName("title_label")
        self.verticalLayout.addWidget(self.title_label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.local_gb = QtWidgets.QGroupBox(SyncSaveDialog)
        self.local_gb.setObjectName("local_gb")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.local_gb)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.date_info_local = QtWidgets.QLabel(self.local_gb)
        self.date_info_local.setText("TextLabel")
        self.date_info_local.setAlignment(QtCore.Qt.AlignCenter)
        self.date_info_local.setObjectName("date_info_local")
        self.verticalLayout_2.addWidget(self.date_info_local)
        self.icon_local = QtWidgets.QLabel(self.local_gb)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.icon_local.sizePolicy().hasHeightForWidth())
        self.icon_local.setSizePolicy(sizePolicy)
        self.icon_local.setText("")
        self.icon_local.setAlignment(QtCore.Qt.AlignCenter)
        self.icon_local.setObjectName("icon_local")
        self.verticalLayout_2.addWidget(self.icon_local)
        self.upload_button = QtWidgets.QPushButton(self.local_gb)
        self.upload_button.setObjectName("upload_button")
        self.verticalLayout_2.addWidget(self.upload_button)
        self.horizontalLayout.addWidget(self.local_gb)
        self.cloud_gb = QtWidgets.QGroupBox(SyncSaveDialog)
        self.cloud_gb.setObjectName("cloud_gb")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.cloud_gb)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.date_info_remote = QtWidgets.QLabel(self.cloud_gb)
        self.date_info_remote.setText("TextLabel")
        self.date_info_remote.setAlignment(QtCore.Qt.AlignCenter)
        self.date_info_remote.setObjectName("date_info_remote")
        self.verticalLayout_3.addWidget(self.date_info_remote)
        self.icon_remote = QtWidgets.QLabel(self.cloud_gb)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.icon_remote.sizePolicy().hasHeightForWidth())
        self.icon_remote.setSizePolicy(sizePolicy)
        self.icon_remote.setText("")
        self.icon_remote.setAlignment(QtCore.Qt.AlignCenter)
        self.icon_remote.setObjectName("icon_remote")
        self.verticalLayout_3.addWidget(self.icon_remote)
        self.download_button = QtWidgets.QPushButton(self.cloud_gb)
        self.download_button.setObjectName("download_button")
        self.verticalLayout_3.addWidget(self.download_button)
        self.horizontalLayout.addWidget(self.cloud_gb)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.cancel_button = QtWidgets.QPushButton(SyncSaveDialog)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout_2.addWidget(self.cancel_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(SyncSaveDialog)
        QtCore.QMetaObject.connectSlotsByName(SyncSaveDialog)

    def retranslateUi(self, SyncSaveDialog):
        _translate = QtCore.QCoreApplication.translate
        SyncSaveDialog.setWindowTitle(_translate("SyncSaveDialog", "Sync saves with cloud"))
        self.title_label.setText(_translate("SyncSaveDialog", "Select save, you want to use for "))
        self.local_gb.setTitle(_translate("SyncSaveDialog", "Local"))
        self.upload_button.setText(_translate("SyncSaveDialog", "Upload"))
        self.cloud_gb.setTitle(_translate("SyncSaveDialog", "Cloud"))
        self.download_button.setText(_translate("SyncSaveDialog", "Download"))
        self.cancel_button.setText(_translate("SyncSaveDialog", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SyncSaveDialog = QtWidgets.QDialog()
    ui = Ui_SyncSaveDialog()
    ui.setupUi(SyncSaveDialog)
    SyncSaveDialog.show()
    sys.exit(app.exec_())
