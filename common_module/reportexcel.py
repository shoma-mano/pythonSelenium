#coding: UTF-8

import slackweb
import os
import requests

def SendToSlack(message):
 
    # Slackへの投稿に必要は情報を設定
    token = 'your token'
    channel = 'your channel'
    text = message
 
    param ={
        'token': token,
        'channels': 'your channels',
        'initial_comment': text
      }
 
    # 投稿するExcelファイルを絶対パスを取得
    fullpath = os.path.join("excelpath", "message")
    files = {'file': open(fullpath, 'rb')}
 
    # SlackへExcelファイルを投稿
    r=requests.post(url='https://slack.com/api/files.upload', params=param, files=files)
    print(r.url)
    print(r.text)
    print(message+"のエクセルをSlackに投稿しました")


