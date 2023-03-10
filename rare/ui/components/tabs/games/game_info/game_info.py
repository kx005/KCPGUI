# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rare/ui/components/tabs/games/game_info/game_info.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GameInfo(object):
    def setupUi(self, GameInfo):
        GameInfo.setObjectName("GameInfo")
        GameInfo.resize(791, 583)
        self.layout_game_info = QtWidgets.QHBoxLayout(GameInfo)
        self.layout_game_info.setObjectName("layout_game_info")
        self.layout_game_info_form = QtWidgets.QGridLayout()
        self.layout_game_info_form.setContentsMargins(6, 6, 6, 6)
        self.layout_game_info_form.setSpacing(12)
        self.layout_game_info_form.setObjectName("layout_game_info_form")
        spacerItem = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_game_info_form.addItem(spacerItem, 8, 1, 1, 1)
        self.dev = QtWidgets.QLabel(GameInfo)
        self.dev.setText("error")
        self.dev.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.dev.setObjectName("dev")
        self.layout_game_info_form.addWidget(self.dev, 0, 1, 1, 1)
        self.lbl_dev = QtWidgets.QLabel(GameInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_dev.sizePolicy().hasHeightForWidth())
        self.lbl_dev.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_dev.setFont(font)
        self.lbl_dev.setObjectName("lbl_dev")
        self.layout_game_info_form.addWidget(self.lbl_dev, 0, 0, 1, 1, QtCore.Qt.AlignRight)
        self.app_name = QtWidgets.QLabel(GameInfo)
        self.app_name.setText("error")
        self.app_name.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.app_name.setObjectName("app_name")
        self.layout_game_info_form.addWidget(self.app_name, 1, 1, 1, 1)
        self.install_path = QtWidgets.QLabel(GameInfo)
        self.install_path.setText("error")
        self.install_path.setWordWrap(True)
        self.install_path.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.install_path.setObjectName("install_path")
        self.layout_game_info_form.addWidget(self.install_path, 5, 1, 1, 1)
        self.lbl_platform = QtWidgets.QLabel(GameInfo)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_platform.setFont(font)
        self.lbl_platform.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_platform.setObjectName("lbl_platform")
        self.layout_game_info_form.addWidget(self.lbl_platform, 6, 0, 1, 1)
        self.version = QtWidgets.QLabel(GameInfo)
        self.version.setText("error")
        self.version.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.version.setObjectName("version")
        self.layout_game_info_form.addWidget(self.version, 2, 1, 1, 1)
        self.lbl_install_path = QtWidgets.QLabel(GameInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_install_path.sizePolicy().hasHeightForWidth())
        self.lbl_install_path.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_install_path.setFont(font)
        self.lbl_install_path.setObjectName("lbl_install_path")
        self.layout_game_info_form.addWidget(self.lbl_install_path, 5, 0, 1, 1, QtCore.Qt.AlignRight)
        self.lbl_install_size = QtWidgets.QLabel(GameInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_install_size.sizePolicy().hasHeightForWidth())
        self.lbl_install_size.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_install_size.setFont(font)
        self.lbl_install_size.setObjectName("lbl_install_size")
        self.layout_game_info_form.addWidget(self.lbl_install_size, 4, 0, 1, 1, QtCore.Qt.AlignRight)
        spacerItem1 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layout_game_info_form.addItem(spacerItem1, 8, 0, 1, 1)
        self.platform = QtWidgets.QLabel(GameInfo)
        self.platform.setText("error")
        self.platform.setObjectName("platform")
        self.layout_game_info_form.addWidget(self.platform, 6, 1, 1, 1)
        self.game_actions_stack = QtWidgets.QStackedWidget(GameInfo)
        self.game_actions_stack.setMinimumSize(QtCore.QSize(250, 0))
        self.game_actions_stack.setObjectName("game_actions_stack")
        self.installed_page = QtWidgets.QWidget()
        self.installed_page.setObjectName("installed_page")
        self.installed_layout = QtWidgets.QVBoxLayout(self.installed_page)
        self.installed_layout.setContentsMargins(0, 0, 0, 0)
        self.installed_layout.setObjectName("installed_layout")
        self.verify_widget = QtWidgets.QStackedWidget(self.installed_page)
        self.verify_widget.setObjectName("verify_widget")
        self.page_verify_button = QtWidgets.QWidget()
        self.page_verify_button.setObjectName("page_verify_button")
        self.layout_verify_button = QtWidgets.QVBoxLayout(self.page_verify_button)
        self.layout_verify_button.setContentsMargins(0, 0, 0, 0)
        self.layout_verify_button.setSpacing(0)
        self.layout_verify_button.setObjectName("layout_verify_button")
        self.verify_button = QtWidgets.QPushButton(self.page_verify_button)
        self.verify_button.setObjectName("verify_button")
        self.layout_verify_button.addWidget(self.verify_button)
        self.verify_widget.addWidget(self.page_verify_button)
        self.page_verify_progress = QtWidgets.QWidget()
        self.page_verify_progress.setObjectName("page_verify_progress")
        self.layout_verify_progress = QtWidgets.QVBoxLayout(self.page_verify_progress)
        self.layout_verify_progress.setContentsMargins(0, 0, 0, 0)
        self.layout_verify_progress.setSpacing(0)
        self.layout_verify_progress.setObjectName("layout_verify_progress")
        self.verify_progress = QtWidgets.QProgressBar(self.page_verify_progress)
        self.verify_progress.setProperty("value", 24)
        self.verify_progress.setObjectName("verify_progress")
        self.layout_verify_progress.addWidget(self.verify_progress)
        self.verify_widget.addWidget(self.page_verify_progress)
        self.installed_layout.addWidget(self.verify_widget)
        self.repair_button = QtWidgets.QPushButton(self.installed_page)
        self.repair_button.setObjectName("repair_button")
        self.installed_layout.addWidget(self.repair_button)
        self.move_stack = QtWidgets.QStackedWidget(self.installed_page)
        self.move_stack.setMinimumSize(QtCore.QSize(0, 20))
        self.move_stack.setObjectName("move_stack")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.page)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.move_button = QtWidgets.QToolButton(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.move_button.sizePolicy().hasHeightForWidth())
        self.move_button.setSizePolicy(sizePolicy)
        self.move_button.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.move_button.setObjectName("move_button")
        self.horizontalLayout_2.addWidget(self.move_button)
        self.move_stack.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.move_stack.addWidget(self.page_2)
        self.installed_layout.addWidget(self.move_stack)
        self.uninstall_button = QtWidgets.QPushButton(self.installed_page)
        self.uninstall_button.setStyleSheet("")
        self.uninstall_button.setObjectName("uninstall_button")
        self.installed_layout.addWidget(self.uninstall_button)
        self.game_actions_stack.addWidget(self.installed_page)
        self.uninstalled_page = QtWidgets.QWidget()
        self.uninstalled_page.setObjectName("uninstalled_page")
        self.uninstalled_layout = QtWidgets.QVBoxLayout(self.uninstalled_page)
        self.uninstalled_layout.setObjectName("uninstalled_layout")
        self.install_button = QtWidgets.QPushButton(self.uninstalled_page)
        self.install_button.setStyleSheet("")
        self.install_button.setObjectName("install_button")
        self.uninstalled_layout.addWidget(self.install_button)
        self.game_actions_stack.addWidget(self.uninstalled_page)
        self.layout_game_info_form.addWidget(self.game_actions_stack, 7, 1, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.install_size = QtWidgets.QLabel(GameInfo)
        self.install_size.setText("error")
        self.install_size.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.install_size.setObjectName("install_size")
        self.layout_game_info_form.addWidget(self.install_size, 4, 1, 1, 1)
        self.lbl_version = QtWidgets.QLabel(GameInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_version.sizePolicy().hasHeightForWidth())
        self.lbl_version.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_version.setFont(font)
        self.lbl_version.setObjectName("lbl_version")
        self.layout_game_info_form.addWidget(self.lbl_version, 2, 0, 1, 1, QtCore.Qt.AlignRight)
        self.lbl_game_actions = QtWidgets.QLabel(GameInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_game_actions.sizePolicy().hasHeightForWidth())
        self.lbl_game_actions.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_game_actions.setFont(font)
        self.lbl_game_actions.setObjectName("lbl_game_actions")
        self.layout_game_info_form.addWidget(self.lbl_game_actions, 7, 0, 1, 1, QtCore.Qt.AlignRight)
        self.lbl_grade = QtWidgets.QLabel(GameInfo)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_grade.setFont(font)
        self.lbl_grade.setObjectName("lbl_grade")
        self.layout_game_info_form.addWidget(self.lbl_grade, 3, 0, 1, 1, QtCore.Qt.AlignRight)
        self.lbl_app_name = QtWidgets.QLabel(GameInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_app_name.sizePolicy().hasHeightForWidth())
        self.lbl_app_name.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_app_name.setFont(font)
        self.lbl_app_name.setObjectName("lbl_app_name")
        self.layout_game_info_form.addWidget(self.lbl_app_name, 1, 0, 1, 1, QtCore.Qt.AlignRight)
        self.grade = QtWidgets.QLabel(GameInfo)
        self.grade.setText("error")
        self.grade.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.grade.setObjectName("grade")
        self.layout_game_info_form.addWidget(self.grade, 3, 1, 1, 1)
        self.layout_game_info.addLayout(self.layout_game_info_form)

        self.retranslateUi(GameInfo)
        self.game_actions_stack.setCurrentIndex(0)
        self.verify_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(GameInfo)

    def retranslateUi(self, GameInfo):
        _translate = QtCore.QCoreApplication.translate
        GameInfo.setWindowTitle(_translate("GameInfo", "Game Info"))
        self.lbl_dev.setText(_translate("GameInfo", "Developer"))
        self.lbl_platform.setText(_translate("GameInfo", "Platform"))
        self.lbl_install_path.setText(_translate("GameInfo", "Installation Path"))
        self.lbl_install_size.setText(_translate("GameInfo", "Installation Size"))
        self.verify_button.setText(_translate("GameInfo", "Verify Installation"))
        self.repair_button.setText(_translate("GameInfo", "Repair Installation"))
        self.move_button.setText(_translate("GameInfo", "Move Installation"))
        self.uninstall_button.setText(_translate("GameInfo", "Uninstall Game"))
        self.install_button.setText(_translate("GameInfo", "Install Game"))
        self.lbl_version.setText(_translate("GameInfo", "Version"))
        self.lbl_game_actions.setText(_translate("GameInfo", "Actions"))
        self.lbl_grade.setText(_translate("GameInfo", "ProtonDB Grade"))
        self.lbl_app_name.setText(_translate("GameInfo", "Application Name"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GameInfo = QtWidgets.QWidget()
    ui = Ui_GameInfo()
    ui.setupUi(GameInfo)
    GameInfo.show()
    sys.exit(app.exec_())
