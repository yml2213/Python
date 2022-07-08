# !/bin/env python3
# -*- coding: utf-8 -*


# =================================以下代码不懂不要随便乱动====================================
try:
    import requests
    import json
    import sys
    import os
    import re
    import time
    from loguru import logger
except Exception as e:
    logger.error(e)
requests.packages.urllib3.disable_warnings()
# --------------------------------------------------------------------------------------------
Script_Name = "测试"
Name_Pinyin = "ceshi"
Script_Change = ""
Script_Version = "0.0.1"
Version_Check = "0.0.2"
# --------------------------------------------------------------------------------------------


def Origin_Version(name, type):
    if (type == 1):
        url = "https://raw.gh.fakev.cn/yml2213/Python/master/" + name + "/" + name + ".py"
    elif (type == 2):
        url = "hhttp://yml-gitea.ml:2233/yml/JavaScript-yml/raw/branch/master/" + name + ".py"
    try:
        info_url = url
        info_headers = {}
        response = requests.get(
            url=info_url, headers=info_headers, verify=False)
        result = response.json()
        print(result)

        # name = result['data']['name']
        # id = result['data']['id']
        # return name, id
    except Exception as e:
        print(e)
        # msg("{0}获取个人信息失败,可能是DD_token 和 cookies过期".format(DD_token))


def tip():
    logger.info("================ 脚本只支持青龙新版 =================")
    logger.info("============ 具体教程以请自行查看顶部教程 =============\n")
    logger.info("🔔 " + Script_Name + " ,开始!")
    logger.info("📌 本地脚本: V " + Script_Version +
                "远程仓库版本: V" + Origin_Version(Name_Pinyin, 1))
    logger.info("📌 🆙 更新内容: " + Script_Change)


def Mac_env(tpyqc_data):
    global ckArr
    pwd = os.path.dirname(os.path.abspath(__file__)) + os.sep
    path = pwd + ".env"
    with open(path, "r+") as f:
        env = f.read()
        if tpyqc_data in env:
            r = re.compile(r'tpyqc_data="(.*?)"', re.M | re.S | re.I)
            data = r.findall(env)
            # print(data[0])
            if "@" in data[0]:
                ck = data[0].split("@")
                ckArr = ck
            elif "\n" in data[0]:
                ck = data[0].split("\n")
                ckArr = ck
            else:
                ckArr = data
        else:
            logger.warning("检查变量" + tpyqc_data + "是否已填写")


def ql_env(tpyqc_data):
    global ckArr
    if tpyqc_data in os.environ:
        ckArr = []
        data = os.environ[tpyqc_data]
        if "@" in data:
            ck = data.split("@")
            ckArr = ck
        elif "\n" in data:
            ck = data.split("\n")
            ckArr = ck
        else:
            ckArr = data


Mac_env("tpyqc_data")
ql_env("tpyqc_data")


class tpycq:
    url_tpycq = "https://mrobot.pcauto.com.cn/auto_passport3_back_intf/passport3/rest/login_new.jsp"

    def __init__(self, phone, passwd):
        self.phone = phone
        self.passwd = passwd

    def login(self):
        try:
            url = self.url_tpycq
            data = "password=" + self.passwd + "&username=" + self.phone
            hearders = {
                "Content-Type": "application/x-www-form-urlencoded",
            }
            response = requests.post(
                url=url, headers=hearders, data=data, verify=False)
            result = response.json()
            # print(result)

            if result["status"] == 0:
                logger.info("登录: " + result["message"])
                # msg("登录: " + result["message"])
                session = result["session"]
                print(session)

            # else:
            #     countDay = result['obj']['countDay']
            #     commodityName = result['obj']['integralTaskSignPackageVOList'][0]['commodityName']
            #     msg("【账号{0}】今日签到成功 ,连续签到{1}天 ,获得【{2}】".format(
            #         account, countDay, commodityName))

        except Exception as e:
            print(e)
            # msg("【账号{}】签到失败 ,可能是Cookie过期".format(account))


# 获取通知服务
class msg(object):
    def __init__(self, m=""):
        self.str_msg = m
        self.message()

    def message(self):
        global msg_info
        print(self.str_msg)
        try:
            msg_info = "{}\n{}".format(msg_info, self.str_msg)
        except:
            msg_info = "{}".format(self.str_msg)
        sys.stdout.flush()  # 这代码的作用就是刷新缓冲区。
        # 当我们打印一些字符时 ,并不是调用print函数后就立即打印的。一般会先将字符送到缓冲区 ,然后再打印。
        # 这就存在一个问题 ,如果你想等时间间隔的打印一些字符 ,但由于缓冲区没满 ,不会打印。就需要采取一些手段。如每次打印后强行刷新缓冲区。

    def getsendNotify(self, a=0):
        if a == 0:
            a += 1
        try:
            url = "https://gitee.com/curtinlv/Public/raw/master/sendNotify.py"
            response = requests.get(url)
            if "curtinlv" in response.text:
                with open("sendNotify.py", "w+", encoding="utf-8") as f:
                    f.write(response.text)
            else:
                if a < 5:
                    a += 1
                    return self.getsendNotify(a)
                else:
                    pass
        except:
            if a < 5:
                a += 1
                return self.getsendNotify(a)
            else:
                pass

    def main(self):
        global send
        cur_path = os.path.abspath(os.path.dirname(__file__))
        sys.path.append(cur_path)
        if os.path.exists(cur_path + "/sendNotify.py"):
            try:
                from sendNotify import send
            except:
                self.getsendNotify()
                try:
                    from sendNotify import send
                except:
                    print("加载通知服务失败~")
        else:
            self.getsendNotify()
            try:
                from sendNotify import send
            except:
                print("加载通知服务失败~")


msg().main()
nowtime = int(round(time.time() * 1000))


if __name__ == "__main__":
    global msg_info
    global ckArr
    tip()
    # logger.info("================ 脚本只支持青龙新版 =================")
    # logger.info("============ 具体教程以请自行查看顶部教程 =============\n")
    # logger.info("🔔 " + Script_Name + " ,开始!")
    # logger.info("📌 本地脚本: V " + Script_Version +
    #             "远程仓库版本: V" + Origin_Version(Name_Pinyin, 1))
    # logger.info("📌 🆙 更新内容: " + Script_Change)

    for data in ckArr:
        ck = data.split("&")
        logger.info("开始 登录")
        print(ck[0], ck[1])
        # tpycq.login(ck[0], ck[1])
