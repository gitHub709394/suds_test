# -*- coding: utf-8 -*-
# @Time    : 2018/12/6 11:36 PM
# @Author  : Tan
# @File    : demo.py
# @Software: PyCharm


from suds.client import Client


def main():
    url = "http://www.webxml.com.cn/webservices/qqOnlineWebService.asmx?wsdl"
    client = Client(url)
    print(client)
    result = client.service.qqCheckOnline("337918559")
    print(client.messages)
    print(result)


if __name__ == '__main__':
    main()
