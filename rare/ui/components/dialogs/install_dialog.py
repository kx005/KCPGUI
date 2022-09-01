# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rare/ui/components/dialogs/install_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_InstallDialog(object):
    def setupUi(self, InstallDialog):
        InstallDialog.setObjectName("InstallDialog")
        InstallDialog.resize(383, 436)
        InstallDialog.setWindowTitle("Rare")
        self.install_dialog_layout = QtWidgets.QFormLayout(InstallDialog)
        self.install_dialog_layout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.install_dialog_layout.setObjectName("install_dialog_layout")
        self.install_dialog_label = QtWidgets.QLabel(InstallDialog)
        self.install_dialog_label.setObjectName("install_dialog_label")
        self.install_dialog_layout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.install_dialog_label)
        self.install_dir_label = QtWidgets.QLabel(InstallDialog)
        self.install_dir_label.setObjectName("install_dir_label")
        self.install_dialog_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.install_dir_label)
        self.install_dir_layout = QtWidgets.QHBoxLayout()
        self.install_dir_layout.setObjectName("install_dir_layout")
        self.install_dialog_layout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.install_dir_layout)
        self.platform_label = QtWidgets.QLabel(InstallDialog)
        self.platform_label.setObjectName("platform_label")
        self.install_dialog_layout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.platform_label)
        self.platform_combo_box = QtWidgets.QComboBox(InstallDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.platform_combo_box.sizePolicy().hasHeightForWidth())
        self.platform_combo_box.setSizePolicy(sizePolicy)
        self.platform_combo_box.setObjectName("platform_combo_box")
        self.install_dialog_layout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.platform_combo_box)
        self.shortcut_lbl = QtWidgets.QLabel(InstallDialog)
        self.shortcut_lbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.shortcut_lbl.setObjectName("shortcut_lbl")
        self.install_dialog_layout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.shortcut_lbl)
        self.shortcut_cb = QtWidgets.QCheckBox(InstallDialog)
        self.shortcut_cb.setText("")
        self.shortcut_cb.setObjectName("shortcut_cb")
        self.install_dialog_layout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.shortcut_cb)
        self.sdl_list_label = QtWidgets.QLabel(InstallDialog)
        self.sdl_list_label.setObjectName("sdl_list_label")
        self.install_dialog_layout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.sdl_list_label)
        self.sdl_list_frame = QtWidgets.QFrame(InstallDialog)
        self.sdl_list_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sdl_list_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sdl_list_frame.setObjectName("sdl_list_frame")
        self.sdl_list_layout = QtWidgets.QVBoxLayout(self.sdl_list_frame)
        self.sdl_list_layout.setSpacing(0)
        self.sdl_list_layout.setObjectName("sdl_list_layout")
        self.install_dialog_layout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.sdl_list_frame)
        self.collapsible_layout = QtWidgets.QVBoxLayout()
        self.collapsible_layout.setObjectName("collapsible_layout")
        self.advanced_layout = QtWidgets.QFormLayout()
        self.advanced_layout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.advanced_layout.setObjectName("advanced_layout")
        self.max_workers_label = QtWidgets.QLabel(InstallDialog)
        self.max_workers_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.max_workers_label.setObjectName("max_workers_label")
        self.advanced_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.max_workers_label)
        self.max_workers_layout = QtWidgets.QHBoxLayout()
        self.max_workers_layout.setObjectName("max_workers_layout")
        self.max_workers_spin = QtWidgets.QSpinBox(InstallDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.max_workers_spin.sizePolicy().hasHeightForWidth())
        self.max_workers_spin.setSizePolicy(sizePolicy)
        self.max_workers_spin.setObjectName("max_workers_spin")
        self.max_workers_layout.addWidget(self.max_workers_spin)
        self.max_workers_info_label = QtWidgets.QLabel(InstallDialog)
        font = QtGui.QFont()
        font.setItalic(True)
        self.max_workers_info_label.setFont(font)
        self.max_workers_info_label.setObjectName("max_workers_info_label")
        self.max_workers_layout.addWidget(self.max_workers_info_label)
        self.advanced_layout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.max_workers_layout)
        self.max_memory_label = QtWidgets.QLabel(InstallDialog)
        self.max_memory_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.max_memory_label.setObjectName("max_memory_label")
        self.advanced_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.max_memory_label)
        self.max_memory_layout = QtWidgets.QHBoxLayout()
        self.max_memory_layout.setObjectName("max_memory_layout")
        self.max_memory_spin = QtWidgets.QSpinBox(InstallDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.max_memory_spin.sizePolicy().hasHeightForWidth())
        self.max_memory_spin.setSizePolicy(sizePolicy)
        self.max_memory_spin.setMinimum(0)
        self.max_memory_spin.setMaximum(10240)
        self.max_memory_spin.setSingleStep(128)
        self.max_memory_spin.setProperty("value", 1024)
        self.max_memory_spin.setObjectName("max_memory_spin")
        self.max_memory_layout.addWidget(self.max_memory_spin)
        self.max_memory_info_label = QtWidgets.QLabel(InstallDialog)
        font = QtGui.QFont()
        font.setItalic(True)
        self.max_memory_info_label.setFont(font)
        self.max_memory_info_label.setObjectName("max_memory_info_label")
        self.max_memory_layout.addWidget(self.max_memory_info_label)
        self.advanced_layout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.max_memory_layout)
        self.install_prereqs_lbl = QtWidgets.QLabel(InstallDialog)
        self.install_prereqs_lbl.setObjectName("install_prereqs_lbl")
        self.advanced_layout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.install_prereqs_lbl)
        self.install_prereqs_check = QtWidgets.QCheckBox(InstallDialog)
        font = QtGui.QFont()
        font.setItalic(True)
        self.install_prereqs_check.setFont(font)
        self.install_prereqs_check.setText("")
        self.install_prereqs_check.setChecked(False)
        self.install_prereqs_check.setObjectName("install_prereqs_check")
        self.advanced_layout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.install_prereqs_check)
        self.dl_optimizations_label = QtWidgets.QLabel(InstallDialog)
        self.dl_optimizations_label.setObjectName("dl_optimizations_label")
        self.advanced_layout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.dl_optimizations_label)
        self.dl_optimizations_check = QtWidgets.QCheckBox(InstallDialog)
        self.dl_optimizations_check.setText("")
        self.dl_optimizations_check.setChecked(False)
        self.dl_optimizations_check.setObjectName("dl_optimizations_check")
        self.advanced_layout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.dl_optimizations_check)
        self.force_download_label = QtWidgets.QLabel(InstallDialog)
        self.force_download_label.setObjectName("force_download_label")
        self.advanced_layout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.force_download_label)
        self.force_download_check = QtWidgets.QCheckBox(InstallDialog)
        self.force_download_check.setText("")
        self.force_download_check.setObjectName("force_download_check")
        self.advanced_layout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.force_download_check)
        self.ignore_space_label = QtWidgets.QLabel(InstallDialog)
        self.ignore_space_label.setObjectName("ignore_space_label")
        self.advanced_layout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.ignore_space_label)
        self.ignore_space_check = QtWidgets.QCheckBox(InstallDialog)
        font = QtGui.QFont()
        font.setItalic(True)
        self.ignore_space_check.setFont(font)
        self.ignore_space_check.setObjectName("ignore_space_check")
        self.advanced_layout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.ignore_space_check)
        self.download_only_label = QtWidgets.QLabel(InstallDialog)
        self.download_only_label.setObjectName("download_only_label")
        self.advanced_layout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.download_only_label)
        self.download_only_check = QtWidgets.QCheckBox(InstallDialog)
        font = QtGui.QFont()
        font.setItalic(True)
        self.download_only_check.setFont(font)
        self.download_only_check.setObjectName("download_only_check")
        self.advanced_layout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.download_only_check)
        self.collapsible_layout.addLayout(self.advanced_layout)
        self.install_dialog_layout.setLayout(5, QtWidgets.QFormLayout.SpanningRole, self.collapsible_layout)
        self.download_size_label = QtWidgets.QLabel(InstallDialog)
        self.download_size_label.setObjectName("download_size_label")
        self.install_dialog_layout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.download_size_label)
        self.download_size_info_label = QtWidgets.QLabel(InstallDialog)
        font = QtGui.QFont()
        font.setItalic(True)
        self.download_size_info_label.setFont(font)
        self.download_size_info_label.setObjectName("download_size_info_label")
        self.install_dialog_layout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.download_size_info_label)
        self.install_size_label = QtWidgets.QLabel(InstallDialog)
        self.install_size_label.setObjectName("install_size_label")
        self.install_dialog_layout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.install_size_label)
        self.install_size_info_label = QtWidgets.QLabel(InstallDialog)
        font = QtGui.QFont()
        font.setItalic(True)
        self.install_size_info_label.setFont(font)
        self.install_size_info_label.setWordWrap(True)
        self.install_size_info_label.setObjectName("install_size_info_label")
        self.install_dialog_layout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.install_size_info_label)
        self.warn_label = QtWidgets.QLabel(InstallDialog)
        self.warn_label.setObjectName("warn_label")
        self.install_dialog_layout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.warn_label)
        self.warn_message = QtWidgets.QLabel(InstallDialog)
        font = QtGui.QFont()
        font.setItalic(True)
        self.warn_message.setFont(font)
        self.warn_message.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.warn_message.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.warn_message.setWordWrap(True)
        self.warn_message.setObjectName("warn_message")
        self.install_dialog_layout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.warn_message)
        self.button_layout = QtWidgets.QHBoxLayout()
        self.button_layout.setObjectName("button_layout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.button_layout.addItem(spacerItem)
        self.cancel_button = QtWidgets.QPushButton(InstallDialog)
        self.cancel_button.setObjectName("cancel_button")
        self.button_layout.addWidget(self.cancel_button)
        self.verify_button = QtWidgets.QPushButton(InstallDialog)
        self.verify_button.setObjectName("verify_button")
        self.button_layout.addWidget(self.verify_button)
        self.install_button = QtWidgets.QPushButton(InstallDialog)
        self.install_button.setObjectName("install_button")
        self.button_layout.addWidget(self.install_button)
        self.install_dialog_layout.setLayout(9, QtWidgets.QFormLayout.SpanningRole, self.button_layout)

        self.retranslateUi(InstallDialog)
        QtCore.QMetaObject.connectSlotsByName(InstallDialog)

    def retranslateUi(self, InstallDialog):
        _translate = QtCore.QCoreApplication.translate
        self.install_dialog_label.setText(_translate("InstallDialog", "error"))
        self.install_dir_label.setText(_translate("InstallDialog", "Install directory"))
        self.platform_label.setText(_translate("InstallDialog", "Platform"))
        self.shortcut_lbl.setText(_translate("InstallDialog", "Create shortcut"))
        self.sdl_list_label.setText(_translate("InstallDialog", "Optional packs"))
        self.max_workers_label.setText(_translate("InstallDialog", "Max workers"))
        self.max_workers_info_label.setText(_translate("InstallDialog", "Less is slower. (0: Default)"))
        self.max_memory_label.setText(_translate("InstallDialog", "Max shared memory"))
        self.max_memory_spin.setSuffix(_translate("InstallDialog", "MiB"))
        self.max_memory_info_label.setText(_translate("InstallDialog", "Less is slower (0: Default)"))
        self.install_prereqs_lbl.setText(_translate("InstallDialog", "Install prerequisites"))
        self.dl_optimizations_label.setText(_translate("InstallDialog", "Enable reordering"))
        self.force_download_label.setText(_translate("InstallDialog", "Force redownload"))
        self.ignore_space_label.setText(_translate("InstallDialog", "Ignore free space"))
        self.ignore_space_check.setText(_translate("InstallDialog", "Use with caution!"))
        self.download_only_label.setText(_translate("InstallDialog", "Download only"))
        self.download_only_check.setText(_translate("InstallDialog", "Do not try to install."))
        self.download_size_label.setText(_translate("InstallDialog", "Download size"))
        self.download_size_info_label.setText(_translate("InstallDialog", "Click verify..."))
        self.install_size_label.setText(_translate("InstallDialog", "Total install size"))
        self.install_size_info_label.setText(_translate("InstallDialog", "Click verify..."))
        self.warn_label.setText(_translate("InstallDialog", "Warning"))
        self.warn_message.setText(_translate("InstallDialog", "None"))
        self.cancel_button.setText(_translate("InstallDialog", "Cancel"))
        self.verify_button.setText(_translate("InstallDialog", "Verify"))
        self.install_button.setText(_translate("InstallDialog", "Install"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InstallDialog = QtWidgets.QDialog()
    ui = Ui_InstallDialog()
    ui.setupUi(InstallDialog)
    InstallDialog.show()
    sys.exit(app.exec_())
