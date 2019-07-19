import RPi.GPIO as GPIO
import urllib.request as ur
from urllib.request import urlopen
from bs4 import BeautifulSoup
#from httplib import HTTPResponse
import urllib
import dht11
import time
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import datetime
from urllib.error import HTTPError
# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#GPIO.cleanup()
#read data using Pin GPIO21 
instance = dht11.DHT11(pin=4)

connection = mysql.connector.connect(host='db4free.net',
                                 database='sathishdb',
                                 user='sathish',
                                 password='sathish@14')
cursor = connection.cursor()
while True:
    result = instance.read()
    if result.is_valid():
        temp="%d" % result.temperature
        print(temp)
        humid="%d" % result.humidity
        #humid="70%%"
        print(humid)
        req=urllib.request.urlopen("https://api.thingspeak.com/update?api_key=2BJXDA7Z517Y7IZM&field1="+str(temp))
        #humid="%d %%" % result.humidity
        req=urllib.request.urlopen("https://api.thingspeak.com/update?api_key=2BJXDA7Z517Y7IZM&field2="+str(humid))
        print("Record inserted successfully into thingspeak dashboard")
        c = connection.cursor()
        c.execute("insert into `sensor_db`(`DATE`,`TEMP C`,`HUMID %`)values(sysdate(),%s,%s)",(temp,humid))
        connection.commit()
        print ("Record inserted successfully into python_users table")



