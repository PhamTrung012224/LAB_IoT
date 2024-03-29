import sys
import random
import time
from Adafruit_IO import MQTTClient


AIO_FEED_ID = ["button1","button2"]
AIO_USERNAME = "Trung012224"
AIO_KEY = ""
# aio_PamD696O1h0PXF5nKt1z59PdVKXr
def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_ID:
        client.subscribe(topic)
    

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload + ", feed id: " + feed_id)
    
client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

counter=10
sensor_type=0

while True:
    counter=counter-1
    if counter<=0:
        counter=10
        
        #TODO
        if sensor_type==0:
            temp=random.randint(10,20)
            client.publish("cambien1",temp)
            sensor_type=1
        elif sensor_type==1:
            light=random.randint(0,500)
            client.publish("cambien2",light)
            sensor_type=2
        elif sensor_type==2:
            humi=random.randint(50,70)
            client.publish("cambien3",humi)
            sensor_type=0
            
    time.sleep(1)
    pass