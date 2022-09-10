# 程序的入口主程序

from functools import partial
import os
import sys
from PyQt5.QtWidgets import *
from Ui_mymainwindow import Ui_MyMainWindow
from handleactions import *
from Ui_add_dialog import Ui_Dialog


class parentWindow(QMainWindow):
    def __init__(self) -> None:
        QMainWindow.__init__(self)
        self.main_ui = Ui_MyMainWindow()
        self.main_ui.setupUi(self)
        #初步设置
        self.main_ui.loadsettings()
        #绑定信号和槽
        #向ui实例里的pushbutton的clicked信号与槽xxx连接
        #ui.pushbutton.clicked.connect(addInformation)
        #clicked信号连接xxx槽，带传参的（使用lambda）
        #ui.btn_addinfo.clicked.connect(lambda: buttonaction.addInformation(ui))
        #clicked信号连接xxx槽，带传参的（使用functools的partial）
        #ui.pushButton.clicked.connect(partial(buttonaction.addInformation,ui))
        self.main_ui.btn_addinfo.clicked.connect(lambda: buttonaction.addInformation(self.main_ui))
        self.main_ui.btn_savesettings.clicked.connect(lambda: buttonaction.saveSettings(self.main_ui))
        self.main_ui.btn_delsettingcompanyname.clicked.connect(lambda: buttonaction.delSettingCompanyName(self.main_ui))
        self.main_ui.btn_start.clicked.connect(lambda: buttonaction.startScreenShot(self.main_ui,self))
        self.main_ui.btn_choosesavingpath.clicked.connect(lambda: buttonaction.chooseSavingPath(self.main_ui,self))
        self.main_ui.btn_removeinfolist.clicked.connect(lambda: buttonaction.removeListinfo(self.main_ui))
        

class childWindow(QDialog):
    def __init__(self) -> None:
        QDialog.__init__(self)
        self.child_ui = Ui_Dialog()
        self.child_ui.setupUi(self)
        
        

    
def bindingWindowByButton(window:parentWindow,child:childWindow):
    window.main_ui.btn_addsettingcompanyname.clicked.connect(child.show)
    #绑定信号和槽
    child.child_ui.btn_ok.clicked.connect(lambda: buttonaction.addSettingCompanyName(window.main_ui,child.child_ui,child))

if __name__ == '__main__':
    #创建一个QApplication实例
    app = QApplication(sys.argv)
    #创建一个QMainwindow实例
    window = parentWindow()
    child = childWindow()
    
    #通过按钮关联窗体
    bindingWindowByButton(window,child)

    #显示窗口实例
    window.show()
    #app.exit()
    sys.exit(app.exec_())
    
    