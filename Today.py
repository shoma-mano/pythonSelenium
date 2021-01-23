import time
import datetime

#日付文字列取得（12/1ならtodayは1201となる)
s=datetime.datetime.now()

month=str(s.month)
day=str(s.day)

if len(str(s.month))==1:
    month=str(0)+str(s.month)

if len(str(s.day))==1:
    day=str(0)+str(s.day)

today=month+day

def get():
    return today