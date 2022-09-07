# 继承pyuic生成的ui代码
# 需要的修改在此进行，以防修改了ui后重新生成的ui代码把自己做的修改覆盖
import os
from Ui_mainwindow import Ui_MainWindow
from PyQt5.QtCore import Qt
import json
import tempfile

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
        #移动fake-useragent文件
        filename = "fake_useragent_0.1.11.json"
        f1 = open("./"+filename,"r")
        path = tempfile.gettempdir()
        f2 = open(path+'/'+filename,"w")
        
        content = f1.readline()#将第一行数据赋给content
        while len(content)>0:#如果读取到的数据长度不为0则循环执行
            f2.write(content)#在file2里写下content
            content=f1.readline()#再读一行赋给content
 
        f1.close()#关闭file1
        f2.close()
        
        #加载设置
        #if os.path.exists("settings.ini"):
        if os.path.exists("settings.json"):
            #设置文件存在
            settings_data = {}
            #f = open("settings.ini")
            with open("settings.json") as f:  
                #加载设置文件
                settings_data = json.load(f)
            
            #list_content = f.read().splitlines()
            #写入combobox
            self.combobox_companyname.addItems(settings_data["qymc"])
            #写入设置页的listwidget
            self.list_settingscompanyname.addItems(settings_data["qymc"])
            
            #写入储存路径
            saving_path = settings_data['savingpath']
            #设置中不存在路径，则默认程序根目录
            if saving_path != None:
                self.lineEdit_savingpath.setText(saving_path)
            else:
                self.lineEdit_savingpath.setText(r'./')
        else:
            #如果设置文件都不存在，下拉列表不用管，保存路径默认程序根目录
            self.lineEdit_savingpath.setText(r'./')
            
    
        
    
        
        
        