# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/fengyunc/Documents/python_workbench/crawlpic/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(660, 236)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 660, 191))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.combobox_companyname = QtWidgets.QComboBox(self.tab)
        self.combobox_companyname.setGeometry(QtCore.QRect(80, 10, 161, 26))
        self.combobox_companyname.setObjectName("combobox_companyname")
        self.lineedit_personname = QtWidgets.QLineEdit(self.tab)
        self.lineedit_personname.setGeometry(QtCore.QRect(80, 50, 113, 21))
        self.lineedit_personname.setObjectName("lineedit_personname")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(20, 10, 60, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 50, 20))
        self.label_2.setObjectName("label_2")
        self.btn_addinfo = QtWidgets.QPushButton(self.tab)
        self.btn_addinfo.setGeometry(QtCore.QRect(240, 30, 113, 32))
        self.btn_addinfo.setObjectName("btn_addinfo")
        self.list_info = QtWidgets.QListWidget(self.tab)
        self.list_info.setGeometry(QtCore.QRect(360, 0, 281, 111))
        self.list_info.setObjectName("list_info")
        self.label_info = QtWidgets.QLabel(self.tab)
        self.label_info.setGeometry(QtCore.QRect(260, 120, 381, 20))
        self.label_info.setText("")
        self.label_info.setObjectName("label_info")
        self.btn_start = QtWidgets.QPushButton(self.tab)
        self.btn_start.setGeometry(QtCore.QRect(530, 120, 113, 32))
        self.btn_start.setObjectName("btn_start")
        self.progressBar = QtWidgets.QProgressBar(self.tab)
        self.progressBar.setGeometry(QtCore.QRect(10, 120, 520, 30))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.btn_removeinfolist = QtWidgets.QPushButton(self.tab)
        self.btn_removeinfolist.setGeometry(QtCore.QRect(310, 90, 50, 30))
        self.btn_removeinfolist.setObjectName("btn_removeinfolist")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setAccessibleName("")
        self.tab_2.setObjectName("tab_2")
        self.label_setting_companylist = QtWidgets.QLabel(self.tab_2)
        self.label_setting_companylist.setGeometry(QtCore.QRect(0, 0, 60, 16))
        self.label_setting_companylist.setObjectName("label_setting_companylist")
        self.btn_savesettings = QtWidgets.QPushButton(self.tab_2)
        self.btn_savesettings.setGeometry(QtCore.QRect(260, 130, 113, 32))
        self.btn_savesettings.setObjectName("btn_savesettings")
        self.btn_addsettingcompanyname = QtWidgets.QPushButton(self.tab_2)
        self.btn_addsettingcompanyname.setGeometry(QtCore.QRect(10, 20, 51, 32))
        self.btn_addsettingcompanyname.setObjectName("btn_addsettingcompanyname")
        self.btn_delsettingcompanyname = QtWidgets.QPushButton(self.tab_2)
        self.btn_delsettingcompanyname.setGeometry(QtCore.QRect(10, 50, 51, 32))
        self.btn_delsettingcompanyname.setObjectName("btn_delsettingcompanyname")
        self.list_settingscompanyname = QtWidgets.QListWidget(self.tab_2)
        self.list_settingscompanyname.setGeometry(QtCore.QRect(60, 0, 201, 131))
        self.list_settingscompanyname.setObjectName("list_settingscompanyname")
        self.label_setting_savingpath = QtWidgets.QLabel(self.tab_2)
        self.label_setting_savingpath.setGeometry(QtCore.QRect(270, 0, 60, 21))
        self.label_setting_savingpath.setObjectName("label_setting_savingpath")
        self.lineEdit_savingpath = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_savingpath.setGeometry(QtCore.QRect(330, 0, 321, 21))
        self.lineEdit_savingpath.setObjectName("lineEdit_savingpath")
        self.btn_choosesavingpath = QtWidgets.QPushButton(self.tab_2)
        self.btn_choosesavingpath.setGeometry(QtCore.QRect(552, 20, 101, 32))
        self.btn_choosesavingpath.setObjectName("btn_choosesavingpath")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 660, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "自动截图器"))
        self.label.setText(_translate("MainWindow", "企业名称"))
        self.label_2.setText(_translate("MainWindow", "姓名"))
        self.btn_addinfo.setText(_translate("MainWindow", "添加===>>>"))
        self.btn_start.setText(_translate("MainWindow", "开始截图"))
        self.btn_removeinfolist.setText(_translate("MainWindow", "-"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "首页"))
        self.label_setting_companylist.setText(_translate("MainWindow", "企业名称"))
        self.btn_savesettings.setText(_translate("MainWindow", "保存"))
        self.btn_addsettingcompanyname.setText(_translate("MainWindow", "+"))
        self.btn_delsettingcompanyname.setText(_translate("MainWindow", "-"))
        self.label_setting_savingpath.setText(_translate("MainWindow", "存储路径"))
        self.btn_choosesavingpath.setText(_translate("MainWindow", "选择存储路径"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "设置"))
