import difflib
from time import sleep

import yaml

from my_thread import MyThread

import re

from web_driver import WEB_PAGE


def compare_string(str1, str2):
    flag = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            if str1[i] == "$":
                if flag == 1:
                    flag = 0
                else:
                    flag = 1
                continue
            elif flag == 1:
                continue
            else:
                print(i, str1[i], str2[i])
                return False
    return True

def diff(str1,str2):
    d = difflib.Differ()
    diff = d.compare(str1.split(), str2.split())
    # print('\n'.join(diff))
    return diff


if __name__ == "__main__":
    # record_path = r'C:\Users\admin\Desktop\record.avi'
    #
    # mythread = MyThread(record_path)
    # # mythread.video_record(record_path)
    # mythread.start()
    # i = 0
    #
    # while i < 10:
    #     i += 1
    #     sleep(1)
    #     print(i)
    #
    # mythread.stop()

    S1 = "产品详情\
    名称：\
    远程国际编辑\
    下载页地址：\
    https://pins-app-resources.oss-cn-qingdao.aliyuncs.com/pins-resources-publish/test/html/index.html?id=145\
    独立软件生产系统：V1.0.0"

    S2 = "产品详情\
    名称：\
    远程国际编辑\
    下载页地址：\
    $\
    独立软件生产系统：V1.0.0"


    # cs = compare_string(S2, s1)
    # print(cs)

    # a1= "hello world"
    # a2 = "hello python"
    #
    # diff = diff(S1, S2)
    # i = 0
    # for line in diff:
    #     i+=1
    #     print(i, line)

