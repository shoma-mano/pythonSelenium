import datetime

s=datetime.datetime.now()
print(str(s.month)+""+str(s.day))

if len(str(s.month))==1:
    month=str(0)+str(s.month)
    print(month)

print(month)