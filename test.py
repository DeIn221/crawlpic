#用于测试各个库的用法和效果

from ast import List
import os
from urllib import request, response
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests
import time
import json




def get_image(url, dir_name,pic_name):
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
    
    
def test_bs():
    url = "http://sjfw.scjs.net.cn:8001/xxgx/Person/rZsxx.aspx?id=E3BAC7EC5660056024B667DE3D6E42ED39302092E075D864"
    url1 = "http://sjfw.scjs.net.cn:8001/xxgx/Person/rList.aspx"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27'
    }
    response = requests.get(url,headers=headers)
    response.encoding="utf-8"
    
    bs_1 = BeautifulSoup(response.text)
    input_name = bs_1.select('#mc')
    input_companyname = bs_1.select('#qymc')
    summit_btn = bs_1.select('#MainContent_Button1')
    
    input_name.value = '李莉'
    input_companyname.value = '四川中润发建设工程有限公司'

    
    data = {
        'mc': '李莉',
        'qymc': '四川中润发建设工程有限公司'
    }
    r1 = requests.post(url1,headers=headers,data=data)
    bs_2 = BeautifulSoup(r1.text)
    
    tag = bs_2.select(".cursorDefault > tr + tr > td")
    index = tag[0].text.find('：')
    print(tag[0].text)
    print(tag[0].text[index+1])
    
def test_json():
    with open('settings.json') as f:
        settings = json.load(f)
        print(settings['qymc'])
    
    
      

if __name__ == "__main__":
    # flag = os.path.exists("settings.ini")
    # print(flag)
    
    # list_contents = ["a","b","c"]
    # for i,item in enumerate(list_contents):
    #     print(item)
    #     print(i)
    
    # f = open("aaa.txt",'w')

    # for i in range(5-1):
    #     f.write(str(i)+'\n')
    # f.write(str(max(range(5))))
    # f.close()
    
    # print(max(range(5)))
    
    # url = 'http://sjfw.scjs.net.cn:8001/xxgx/Person/rZsxx.aspx?id=E3BAC7EC5660056024B667DE3D6E42ED39302092E075D864'

    # dir_name = r'./四川中润发建设工程有限公司/李莉/'
    # pic_name = r'李莉-证书信息.png'

    # get_image(url, dir_name,pic_name)
    
    # test_bs()
    
    test_json()
        
        