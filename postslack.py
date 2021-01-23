#coding: UTF-8

import slackweb
import os
import requests

def SendToSlack(filename, message):
 
    # Slackへの投稿に必要は情報を設定
    token = 'xoxp-1174239099089-1399634450978-1643779448311-7e26c9f71eac0a1b00e852387eb229f6'
    channel = 'C01BS0J2HL3'
    text = message + '\n\n成功'
 
    param ={
        'token': token,
        'channels': 'C01BS0J2HL3,C01K9ER1FFF',
        'initial_comment': text
      }
 
    # 投稿するExcelファイルを絶対パスを取得
    fullpath = os.path.join(os.getcwd()+"\\excel", filename)
    files = {'file': open(fullpath, 'rb')}
 
    # SlackへExcelファイルを投稿
    requests.post(url='https://slack.com/api/files.upload', params=param, files=files)
    print(message+"のエクセルをSlackに投稿しました")

