import datetime
import time

today = datetime.datetime.now()
# strftime('%Y-%m-%d %H:%M')
print(today)
c_m=(time.strftime('%m',time.localtime(time.time())))
# c_m=7
month= []
month.append([int(c_m)-1])
month.append([int(c_m)])
month.append([int(c_m)+1])
# print(a)
s =int(c_m)%3
if s == 0:
    month.append([int(c_m)-5, int(c_m)-4, int(c_m)-3])
    month.append([int(c_m)-2,int(c_m)-1,int(c_m)])
    month.append([int(c_m)+1, int(c_m)+2, int(c_m)+3])
if s == 1:
    month.append([int(c_m)-3, int(c_m) -2, int(c_m)-1])
    month.append([int(c_m),int(c_m)+1,int(c_m)+2])
    month.append([int(c_m)+3, int(c_m) + 4, int(c_m) + 5])
if s == 2:
    month.append([int(c_m) - 4, int(c_m)-3, int(c_m) -2])
    month.append([int(c_m)-1,int(c_m),int(c_m)+1])
    month.append([int(c_m)+2, int(c_m)+3, int(c_m) + 4])
# print(a)

month.append([1,2,3,4,5,6])
month.append([7,8,9,10,11,12])
print(month)