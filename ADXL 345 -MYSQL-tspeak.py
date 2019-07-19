import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import urllib.request as ur
from urllib.request import urlopen
from bs4 import BeautifulSoup
#from httplib import HTTPResponse
import urllib
#import dht11
import time
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
# Import the ADXL345 module.
import Adafruit_ADXL345


# Create an ADXL345 instance.
accel = Adafruit_ADXL345.ADXL345()
connection = mysql.connector.connect(host='db4free.net',
                                 database='sathishdb',
                                 user='sathish',
                                 password='sathish@14')
cursor = connection.cursor()

# Alternatively you can specify the device address and I2C bus with parameters:
#accel = Adafruit_ADXL345.ADXL345(address=0x54, busnum=2)

# You can optionally change the range to one of:
#  - ADXL345_RANGE_2_G   = +/-2G (default)
  - ADXL345_RANGE_4_G   = +/-4G
#  - ADXL345_RANGE_8_G   = +/-8G
#  - ADXL345_RANGE_16_G  = +/-16G
# For example to set to +/- 16G:
#accel.set_range(Adafruit_ADXL345.ADXL345_RANGE_16_G)

# Or change the data rate to one of:
#  - ADXL345_DATARATE_0_10_HZ = 0.1 hz
#  - ADXL345_DATARATE_0_20_HZ = 0.2 hz
#  - ADXL345_DATARATE_0_39_HZ = 0.39 hz

  - ADXL345_DATARATE_0_78_HZ = 0.78 hz
#  - ADXL345_DATARATE_1_56_HZ = 1.56 hz
#  - ADXL345_DATARATE_3_13_HZ = 3.13 hz
#  - ADXL345_DATARATE_6_25HZ  = 6.25 hz
#  - ADXL345_DATARATE_12_5_HZ = 12.5 hz
#  - ADXL345_DATARATE_25_HZ   = 25 hz
#  - ADXL345_DATARATE_50_HZ   = 50 hz
#  - ADXL345_DATARATE_100_HZ  = 100 hz (default)
#  - ADXL345_DATARATE_200_HZ  = 200 hz
#  - ADXL345_DATARATE_400_HZ  = 400 hz

#  - ADXL345_DATARATE_800_HZ  = 800 hz
#  - ADXL345_DATARATE_1600_HZ = 1600 hz
#  - ADXL345_DATARATE_3200_HZ = 3200 hz
# For example to set to 6.25 hz:
#accel.set_data_rate(Adafruit_ADXL345.ADXL345_DATARATE_6_25HZ)

print('Printing X, Y, Z axis values, press Ctrl-C to quit...')
while True:
    # Read the X, Y, Z axis acceleration values and print them.
    x, y, z = accel.read()
    print('X={0}Hz, Y={1}Hz, Z={2}Hz'.format(x, y, z))
    print('X={0}Hz'.format(x))
    print('Y={0}Hz'.format(y))
    print('Z={0}Hz'.format(z))
    # Wait half a second and repeat.
 time.sleep(0.5)
    X=('{0}'.format(x))
    #req=urllib.request.urlopen("https://api.thingspeak.com/update?api_key=2BJX$
    req=urllib.request.urlopen("https://api.thingspeak.com/update?api_key=2BJXDA7Z517Y7IZM&field3="+str(x))
    Y=('{0}'.format(y))
    #req=urllib.request.urlopen("https://api.thingspeak.com/update?api_key=2BJX$
    req=urllib.request.urlopen("https://api.thingspeak.com/update?api_key=2BJXDA7Z517Y7IZM&field4="+str(y))
    Z=('{0}'.format(z))
    #req=urllib.request.urlopen("https://api.thingspeak.com/update?api_key=2BJXD$
    req=urllib.request.urlopen("https://api.thingspeak.com/update?api_key=2BJXDA7Z517Y7IZM&field1="+str(z))
    c = connection.cursor()
    c.execute("insert into `SONY`(`DATE TIME +5.30H`,`X axis Hz`,`Y axis Hz`,`Z axis Hz`)values(sysdate(),%s,%s,%s)",(X,Y,Z))
    connection.commit()
    print ("Record inserted successfully into python_users table")
    while(x>38):
        fromaddr="sathianju333@gmail.com"
        toaddr="rajkumar.m@wabco-auto.com"
        msg = MIMEMultipart()
        msg['From']=fromaddr
        msg['To']=toaddr
        msg['subject']="VIBRATION ALERT" 
        body="Please check the CNC motor"
        msg.attach(MIMEText(body,'plain'))
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login("sathianju333@gmail.com","anjugam14")
        server.sendmail(fromaddr,toaddr,msg.as_string())
        print("Email send succesfully")
        break
        server.guit()
     while(y>238):
        fromaddr="sathianju333@gmail.com"
        toaddr="rajkumar.m@wabco-auto.com"
        msg = MIMEMultipart()
        msg['From']=fromaddr
        msg['To']=toaddr
        msg['subject']="VIBRATION ALERT" 
        body="Please check the CNC motor"
        msg.attach(MIMEText(body,'plain'))
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login("sathianju333@gmail.com","anjugam14")
        server.sendmail(fromaddr,toaddr,msg.as_string())
        print("Email send succesfully")
        break
        server.guit()
    while(z>=235):
        fromaddr="sathianju333@gmail.com"
        toaddr="rajkumar.m@wabco-auto.com"
        msg = MIMEMultipart()
        msg['From']=fromaddr
        msg['To']=toaddr
        msg['subject']="VIBRATION ALERT" 
        body="Please check the CNC motor"
        msg.attach(MIMEText(body,'plain'))
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login("sathianju333@gmail.com","anjugam14")
        server.sendmail(fromaddr,toaddr,msg.as_string())
        print("Email send succesfully")
        break
        server.guit()

          
