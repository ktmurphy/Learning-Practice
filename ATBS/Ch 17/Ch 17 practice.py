#! python3
"""
import time
time.time()
def calcProd():
    product = 1
    for i in range(100000):
        if i == 0:
            continue
        product = i * product
    return product

startTime= time.time()
prod = calcProd()
endTime = time.time()
print('The result is %s digits long.' % (len(str(prod))))
print('Took %s seconds to calculate.' % (endTime - startTime))

import time
print('hi')
time.sleep(1)
print('bye')

now = time.time()
print(round(now, 3))

import datetime, time
dt = datetime.datetime.now()
halloween2019 = datetime.datetime(2019, 10, 31, 0, 0, 0)
newyears2019 = datetime.datetime(2019, 1, 1, 0, 0, 0)

delta = datetime.timedelta(days = 11, hours = 10, minutes = 9, seconds = 8)
delta2 = datetime.timedelta(days = 365 * 30)
##strftime (not under datetime)
oct21st = datetime.datetime(2019, 10, 21, 16, 29, 0)
print(oct21st.strftime('%Y/%m/%d %H:%M:%S'))

#converting strings to datetime using strptime
newobj = datetime.datetime.strptime('October 21, 2019', '%B %d, %Y')

#multithreading using threading module
import threading, time
print('Start of program')
def takeANap():
    time.sleep(3)
    print('Wake up')

threadObj = threading.Thread(target = takeANap)
threadObj.start()
print('end of program')

threadObj2 = threading.Thread(target = print, args = ['cats', 'dogs', 'frogs'], kwargs ={'sep': '&'})
threadObj2.start()

import subprocess
paintProc = subprocess.Popen('C:\\Windows\\System32\\mspaint.exe')
paintProc.poll() == None

subprocess.Popen(['C:\\Windows\\notepad.exe', 'C:\\Users\\katie\\OneDrive\\Documents\\Coding\\ATBS\\Ch 5 - Chess Board Checker'])
"""
fileObj = open("hello.txt.", "w")
fileObj.write("Hello world!")
fileObj.close()
import subprocess

subprocess.Popen(["start", "hello.txt"], shell=True)
