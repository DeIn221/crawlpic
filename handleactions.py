# 在这里实现槽

from curses import COLOR_RED
import re
import sys
import os
from tkinter import messagebox
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot,Qt
from Ui_mymainwindow import Ui_MyMainWindow
from Ui_add_dialog import Ui_Dialog
import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
from fake_useragent import UserAgent 
import random

class buttonaction():
    # 测试事件
    @pyqtSlot()
    def say_hello():
        print("button is clicked!")
    # 点击添加按钮后，向列表里添加一条查询信息
    @pyqtSlot()
    def addInformation(ui:Ui_MyMainWindow):
        
        ui.label_info.setText("")
        companyname = ui.combobox_companyname.currentText()
        peoplename = ui.lineedit_personname.text()
        str = companyname + ',' + peoplename
        count = ui.list_info.count()
        flag = 1
        for i in range(count):
            if ui.list_info.item(i).text() == str:
                flag = 0
                break
        if flag == 1:
            ui.list_info.addItem(str)
        else:
            ui.label_info.setText("【"+str+"】已经有啦！")
            ui.label_info.setStyleSheet("QLabel{color:rgba(255,0,0,255);}")
    #打开添加窗口
    @pyqtSlot()
    def addSettingCompanyName(ui:Ui_MyMainWindow,child_ui:Ui_Dialog,child_window):
        input_companyname = child_ui.lineEdit_inputname.text()
        ui.list_settingscompanyname.addItem(input_companyname)
        child_window.close()
        child_ui.lineEdit_inputname.setText("")
    #移除一行listwidget
    @pyqtSlot()
    def delSettingCompanyName(ui:Ui_MyMainWindow):
        rowcount = ui.list_settingscompanyname.count()
        item = ui.list_settingscompanyname.takeItem(rowcount-1)
        ui.list_settingscompanyname.removeItemWidget(item)
    # 设置选项点击保存
    @pyqtSlot()
    def saveSettings(ui:Ui_MyMainWindow):
        #f = open("settings.ini","w")
        # if not os.path.exists("settings.json"):
        #     os.mknod("settings.json",0o777)
        settings_data = {}
        companyname_list = []
        
        rowcount = ui.list_settingscompanyname.count()
        for i in range(rowcount):
            #写入配置文件
            #companyname = ui.list_settingscompanyname.item(i)
            companyname_list.append(ui.list_settingscompanyname.item(i).text())
            #f.write(companyname.text()+'\n')
        
        
        #companyname = ui.list_settingscompanyname.item(max(range(rowcount)))
        # f.write(companyname.text())
        # f.close()
        settings_data["qymc"] = companyname_list
        
        #保存存储路径
        saving_path = ui.lineEdit_savingpath.text()
        settings_data["savingpath"] = saving_path
        
        
        #将data写入文件
        with open("settings.json","w+") as f:
            json.dump(settings_data,f)
        
        
        #清空
        ui.combobox_companyname.clear()
        ui.list_settingscompanyname.clear()
        #重新加载
        ui.loadsettings()
    #开始截图
    @pyqtSlot()
    def startScreenShot(ui:Ui_MyMainWindow):
        
        #搜索页，和请求头
        search_url = "http://sjfw.scjs.net.cn:8001/xxgx/Person/rList.aspx"
        headers = {'User-Agent': UserAgent().random}
        #proxies = {'http': '39.130.150.44:80'}
        print(headers)
        
        #处理每一组搜索条件
        rowcount = ui.list_info.count()
        
        #对每一组进行截图
        for i in range(rowcount):
            str = ui.list_info.item(i).text()
            ret_list = str.split(',')
            #ret_list[0]是企业名称，[1]是人员名称
            #构建数据data
            data = {
                'qymc': ret_list[0],
                'mc': ret_list[1]
            }
            #拿到点击搜索后的页面
            s = requests.Session()
            s.cookies.clear()
            r1 = requests.post(search_url,data=data,headers=headers)
            
            #获取个人网页网址
            #使用bs解析html
            bs1 = BeautifulSoup(r1.text)
            #对是否搜索成功进行判断
            #进行状态码判断
            print(r1)
            if r1.status_code != 200:
                ui.label_info.setText('搜索网页返回状态：'+ str(r1.status_code))
                continue
            #对返回搜索返回结果判断
            ret_tags = bs1.select('.cursorDefault > tr + tr > td')
            index = ret_tags[0].text.find("：")
            if int(ret_tags[0].text[index+1]) <= 0:
                ui.label_info.setText(ret_list[0]+','+ret_list[1]+'搜索结果为：'+ret_tags[0].text[index+1]+'条')
                continue
            
            #获取可以打开的结果链接
            url_tag = bs1.select('.cursorDefault > tr > td > a')
            
            
            #拼接截图页网址
            screenshot_url = "http://sjfw.scjs.net.cn:8001/xxgx/Person/" + url_tag[0].attrs['href']
            #生成目录文件
            dir_name = ui.lineEdit_savingpath.text()+ret_list[0]+'/'+ret_list[1]
            tab_info_tag = bs1.select('.datas_tabs > .activeTinyTab > a > span')
            tab_name = tab_info_tag[0].text[0:4]
            pic_name = ret_list[1]+'-'+tab_name+'.png'
            
            doScreenShot(screenshot_url,dir_name,pic_name)
        
    #选择储存路径
    @pyqtSlot()
    def chooseSavingPath(ui:Ui_MyMainWindow,parentWindow):
        directory = QFileDialog().getExistingDirectory(parentWindow,"选取文件夹","./")
        ui.lineEdit_savingpath.setText(directory)
        

#做截图      
def doScreenShot(url, dir_name,pic_name):
    #edgedriver目录
    chromedriver = r"./chromedriver"

    os.environ["webdriver.chrome.driver"] = chromedriver
    #设置chrome开启的模式，headless就是无界面模式
    #一定要使用这个模式，不然截不了全页面，只能截到你电脑的高度
    chrome_options = Options()

    chrome_options.add_argument('headless')

    driver = webdriver.Chrome(chromedriver,chrome_options=chrome_options)
    
    #driver.create_options().add_argument("headless")
    #控制浏览器写入并转到链接
    driver.get(url)
    time.sleep(1)
    #接下来是全屏的关键，用js获取页面的宽高，如果有其他需要用js的部分也可以用这个方法
    width = driver.execute_script("return document.documentElement.scrollWidth")
    height = driver.execute_script("return document.documentElement.scrollHeight")
    print(width,height)
    #将浏览器的宽高设置成刚刚获取的宽高
    driver.set_window_size(width,height)
    time.sleep(1)
    #截图并关掉浏览器
    if os.path.exists(dir_name):
        driver.save_screenshot(dir_name+pic_name)
    else:
        os.makedirs(dir_name)
        driver.save_screenshot(dir_name+pic_name)
    driver.close()         
    
            
#伪装IP
def get_fakeIP():
    ip_page = requests.get(  # 获取200条IP
        'http://www.89ip.cn/tqdl.html?num=60&address=中国&kill_address=&port=&kill_port=&isp=')
    proxies_list = re.findall(
        r'(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)(:-?[1-9]\d*)',
        ip_page.text)

    # 转换proxies_list的元素为list,最初为'tuple'元组格式
    proxies_list = list(map(list, proxies_list))

    # 格式化ip  ('112', '111', '217', '188', ':9999')  --->  112.111.217.188:9999
    for u in range(0, len(proxies_list)):
        # 通过小数点来连接为字符
        proxies_list[u] = '.'.join(proxies_list[u])
        # 用rindex()查找最后一个小数点的位置，
        index = proxies_list[u].rindex('.')
        # 将元素转换为list格式
        proxies_list[u] = list(proxies_list[u])
        # 修改位置为index的字符为空白（去除最后一个小数点）
        proxies_list[u][index] = ''
        # 重新通过空白符连接为字符
        proxies_list[u] = ''.join(proxies_list[u])

    # proxies = {'协议':'协议://IP:端口号'}
    # 'https':'https://59.172.27.6:38380'
    
    return str(random.choice(proxies_list))
        
        
