# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import ssl
import json
from xlwt import *
# import xlwt
import sys

reload(sys)
sys.setdefaultencoding('utf8')
requests = requests.Session()
ssl._create_default_https_context = ssl._create_unverified_context

host = "http://www.zysj.com.cn"


def get_list():
    url = host + "/zhongyaocai/index.html"
    response = requests.get(url)
    bs = BeautifulSoup(response.text, 'html5lib')
    qiye_list = bs.select(".py a")
    arr = []
    for i in qiye_list:
        address = i.get("href")
        arr.append(host + address)
    return arr


def get_content(url):
    details = []
    response = requests.get(url)
    bs = BeautifulSoup(response.text, 'html5lib')
    for i in bs.select("#tab-content li a"):
        details.append(host + i.get("href"))
    return details


def get_arr_join(i, num):
    num = num or 0
    obj = {}
    obj["name"] = i.select("h1")[0].text.strip()  # 药物名称

    if i.select(".py") and len(i.select(".py")) > num:
        obj["py"] = i.select(".py")[num].text.strip()  # 拼音
    else:
        obj["py"] = ""

    if i.select(".ywm") and len(i.select(".ywm")) > num:
        obj["ywm"] = i.select(".ywm")[num].text.strip()  # 英文名
    else:
        obj["ywm"] = ""

    if i.select(".bm") and len(i.select(".bm")) > num:
        obj["bm"] = i.select(".bm")[num].text.strip()  # 别名
    else:
        obj["bm"] = ""

    if i.select(".cc") and len(i.select(".cc")) > num:
        obj["cc"] = i.select(".cc")[num].text.strip()  # 出处
    else:
        obj["cc"] = ""

    if i.select(".ly") and len(i.select(".ly")) > num:
        obj["ly"] = i.select(".ly")[num].text.strip()  # 来源
    else:
        obj["ly"] = ""

    if i.select(".yxt") and len(i.select(".yxt")) > num:
        obj["yxt"] = i.select(".yxt")[num].text.strip()  # 原形态
    else:
        obj["yxt"] = ""

    if i.select(".sjfb") and len(i.select(".sjfb")) > num:
        obj["sjfb"] = i.select(".sjfb")[num].text.strip()  # 生境分部
    else:
        obj["sjfb"] = ""

    if i.select(".gj") and len(i.select(".gj")) > num:
        obj["gj"] = i.select(".gj")[num].text.strip()  # 归经
    else:
        obj["gj"] = ""

    if i.select(".xw") and len(i.select(".xw")) > num:
        obj["xw"] = i.select(".xw")[num].text.strip()  # 性味
    else:
        obj["xw"] = ""

    if i.select(".gnzz") and len(i.select(".gnzz")) > num:
        obj["gnzz"] = i.select(".gnzz")[num].text.strip()  # 功能主治
    else:
        obj["gnzz"] = ""

    if i.select(".yfyl") and len(i.select(".yfyl")) > num:
        obj["yfyl"] = i.select(".yfyl")[num].text.strip()  # 用法用量
    else:
        obj["yfyl"] = ""

    if i.select(".hxcf") and len(i.select(".hxcf")) > num:
        obj["hxcf"] = i.select(".hxcf")[num].text.strip()  # 化学成分
    else:
        obj["hxcf"] = ""

    if i.select(".ylzy") and len(i.select(".ylzy")) > num:
        obj["ylzy"] = i.select(".ylzy")[num].text.strip()  # 药理作用
    else:
        obj["ylzy"] = ""

    if i.select(".ff") and len(i.select(".ff")) > num:
        obj["ff"] = i.select(".ff")[num].text.strip()  # 复方
    else:
        obj["ff"] = ""

    if i.select(".jb") and len(i.select(".jb")) > num:
        obj["jb"] = i.select(".jb")[num].text.strip()  # 鉴别
    else:
        obj["jb"] = ""

    if i.select(".bz") and len(i.select(".bz")) > num:
        obj["bz"] = i.select(".bz")[num].text.strip()  # 备注
    else:
        obj["bz"] = ""

    if i.select(".zl") and len(i.select(".zl")) > num:
        obj["zl"] = i.select(".zl")[num].text.strip()  # 摘录
    else:
        obj["zl"] = ""

    if i.select(".gjls") and len(i.select(".gjls")) > num:
        obj["gjls"] = i.select(".gjls")[num].text.strip()  # 各家论述
    else:
        obj["gjls"] = ""

    if i.select(".lcyy") and len(i.select(".lcyy")) > num:
        obj["lcyy"] = i.select(".lcyy")[num].text.strip()  # 临床应用
    else:
        obj["lcyy"] = ""
    return obj


def get_detail(url):
    response = requests.get(url)
    bs = BeautifulSoup(response.text, 'html5lib')
    arr = []
    h2_list = bs.select("#content h2")
    print len(h2_list)
    if len(h2_list) == 0:
        data = get_arr_join(bs.select("#content")[0], 0)
        # file_write(data)
        print data
        save_file(data)
    else:
        for i in xrange(0, len(h2_list), 1):
            data = get_arr_join(bs.select("#content")[0], i)
            save_file(data)

    # arr.append(obj)


def save_file(data):
    f = open('test4.txt', 'a')
    data = json.dumps(data)
    f.writelines(data + "\n")
    f.close()


def file_write(Data):
    file = Workbook(encoding='utf-8')
    # 指定file以utf-8的格式打开
    table = file.add_sheet('药材')
    data = {}
    # 指定打开的文件名
    for i in xrange(0, len(Data), 1):
        data[i+1] = Data[i]
    # data = {
    #     "1": ["张三", 150, 120, 100, 2],
    #     "2": ["wang", 90, 99, 95, 65],
    #     "3": ["wu", 60, 66, 68, 566]
    # }
    # 字典数据

    ldata = []
    num = [a for a in data]
    # for循环指定取出key值存入num中
    num.sort()
    # 字典数据取出后无需，需要先排序

    for x in num:
        # for循环将data字典中的键和值分批的保存在ldata中
        t = [x]
        for a in data[x]:
            t.append(a)
        ldata.append(t)

    for i, p in enumerate(ldata):
        # 将数据写入文件,i是enumerate()函数返回的序号数
        for j, q in enumerate(p):
            print i, j, q
            table.write(i, j, q)
    file.save('yaocai2.xls')

def read_file():
    filename = 'test4.txt'  # txt文件和当前脚本在同一目录下，所以不用写具体路径
    try:
        f = open(filename, 'r')
        Array = []
        for i in f.readlines():
            json_file = json.loads(i)
            arr = []
            arr.append(json_file["name"])
            arr.append(json_file["py"])
            arr.append(json_file["ywm"])
            arr.append(json_file["bm"])
            arr.append(json_file["cc"])
            arr.append(json_file["ly"])
            arr.append(json_file["yxt"])
            arr.append(json_file["sjfb"])
            arr.append(json_file["gj"])
            arr.append(json_file["xw"])
            arr.append(json_file["gnzz"])
            arr.append(json_file["yfyl"])
            arr.append(json_file["hxcf"])
            arr.append(json_file["ylzy"])
            arr.append(json_file["ff"])
            arr.append(json_file["bz"])
            arr.append(json_file["gjls"])
            arr.append(json_file["lcyy"])
            Array.append(arr)
        return Array
    finally:
        if f:
            f.close()

if __name__ == '__main__':
    # for i in get_list():
    #     for j in get_content(i):
    #         get_detail(j)
    # url = "http://www.zysj.com.cn/zhongyaocai/yaocai_z/zhungaeryuanwei.html"
    # url = "http://www.zysj.com.cn/zhongyaocai/yaocai_z/zuiyucao.html"
    # get_detail(url)
    data = read_file()
    print data
    file_write(data)

