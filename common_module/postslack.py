#coding: UTF-8

import slackweb
import os
import requests
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


def SendToSlackFile(kinoumei, message):
 
    # Slackへの投稿に必要は情報を設定
    token = 'xoxp-1174239099089-1399634450978-1691987472838-bf22cd2f8ee85e1f71d24ca94f76d598'
    channel = 'C01BS0J2HL3'
    text = message + ':*期待通りの出力が得られませんでした*'+'\n\n期待結果：'+kinoumei.expectedmessage+'\n\n出力結果：'+kinoumei.message
    if(kinoumei.result=="エラー"):
      text = message + ':エラー'+'\n\nエラーメッセージ:'+kinoumei.message
    if(kinoumei.result=="〇"):
      text = message + ':期待通りの出力が得られました'+'\n\n期待結果：'+kinoumei.expectedmessage+'\n\n出力結果：'+kinoumei.message
 
    param ={
        'token': token,
        'channels': 'C01BS0J2HL3,C01K9ER1FFF',
        'initial_comment': text
      }
 
    # 投稿するExcelファイルを絶対パスを取得
    fullpath = os.path.join(os.getcwd()+"\\excel", kinoumei.name+kinoumei.testtype+".xlsx")
    files = {'file': open(fullpath, 'rb')}
 
    # SlackへExcelファイルを投稿
    r=requests.post(url='https://slack.com/api/files.upload', params=param, files=files)
    print(message+"のエクセルをSlackに投稿しました")

def SendToSlackMessage(message):
    client = WebClient(token='your token') 
    # Slackへの投稿に必要は情報を設定
    channel = '#coding: UTF-8

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


'
    text=message
    response=client.chat_postMessage(channel='your channel', text=text)
    # param ={
    #     'token': token,
    #     'channel': channel,
    #     'text': text
    #   }
    
    # r = requests.post(url='https://slack.com/api/chat.postMessage', params=param)
    # print(r.text)
    # print(r.url)
