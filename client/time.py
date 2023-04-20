
import datetime as dt
from sre_constants import REPEAT
import time
from timeit import repeat
from numpy import true_divide
import schedule
import calendar
from datetime import datetime
from datetime import timedelta
from rocketry.args import Session
import rocketry
appd = rocketry.Rocketry()
from rocketry import Rocketry
@appd.task('every 1 sec')
def sms():
    print('sdj')
appd.run()




# maindate =dt.timedelta()
# inic = 1
# befordate = dt.date( 2023,   1 ,inic)
# inics = 3 
# fg =dt.datetime.today()
# dated = dt.date( 2023,   1 ,inics)
# curentv =  dated - befordate 
# import threading
# totalt = 4*24*60*60
# from time import sleep
# def df():
   
#     print('df')
#     t = REPEAT(1.0, lambda:print('hgf'))
#     t.start()
#     sleep(5)
#     t.cancel()
# df()

# def df():
   
#     print('df')
#     t = threading.Timer(3000,df)
#     t.start
#     return t
# df()


# print(totalt)
# if curentv == 4:
#     print(curentv )
#     print(befordate)
#     print(dated)

# while True:
#     inics+=4
#     print(inics)

# df = fg.day
# dfm = fg.month
# dfy = fg.year
# tim = fg.time
# mn= calendar.month(dfy,dfm)
# for mn,e in mn:
#     if mn or e >= 4:

#         print(mn)



# print(mn)

# def planmaturity():
#     dd = dt.datetime.now()
#     print(dd.today())


# day =4
# secon = day *24*60*60    
# schedule.every(90).day.do(planmaturity)

# schedule.run_pending()
# time.sleep(secon)
# def alr():
#     print('djf')
# alr()    