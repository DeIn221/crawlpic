# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/fengyunc/Documents/python_workbench/crawlpic/add_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(423, 49)
        self.lineEdit_inputname = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_inputname.setGeometry(QtCore.QRect(10, 10, 291, 31))
        self.lineEdit_inputname.setObjectName("lineEdit_inputname")
        self.btn_ok = QtWidgets.QPushButton(Dialog)
        self.btn_ok.setGeometry(QtCore.QRect(310, 10, 101, 31))
        self.btn_ok.setObjectName("btn_ok")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "添加"))
        self.btn_ok.setText(_translate("Dialog", "OK"))
