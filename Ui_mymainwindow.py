# 继承pyuic生成的ui代码
# 需要的修改在此进行，以防修改了ui后重新生成的ui代码把自己做的修改覆盖
import os
from Ui_mainwindow import Ui_MainWindow
from PyQt5.QtCore import Qt

class Ui_MyMainWindow(Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        
        
    # def settingTableView(self):
    #     self.tableWidget_settingcompanyname.setColumnCount(1)
    #     self.tableWidget_settingcompanyname.setHorizontalHeaderLabels(["企业名称"])
    #     self.tableWidget_settingcompanyname.horizontalHeader().setStretchLastSection(True)
    #     self.tableWidget_settingcompanyname.setFocusPolicy(Qt.StrongFocus)
        
    #     #从配置文件中写入设置的list(保持设置，以免再保存设置覆盖)
    #     if os.path.exists("settings.ini"):
    #         f = open("settings.ini")
    #         list_contents = f.read().splitlines()
    #         f.close()
    #         for i,item in enumerate(list_contents):
    #             self.tableWidget_settingcompanyname.setItem(i,1,item)
    
    def loadsettings(self):
        #加载设置
        if os.path.exists("settings.ini"):
            #设置文件存在
            #加载combobox的内容
            #获取文件内容
            f = open("settings.ini")
            list_content = f.read().splitlines()
            #写入combobox
            self.combobox_companyname.addItems(list_content)
            #写入设置页的listwidget
            self.list_settingscompanyname.addItems(list_content)
            #关闭文件
            f.close()
    
        
    
        
        
        