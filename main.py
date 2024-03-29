import sys
# import random
import time
from Adafruit_IO import MQTTClient
from simple_ai import *


AIO_FEED_ID = ["button1","button2"]
AIO_USERNAME = "Trung012224"
AIO_KEY = ""
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

counter_ai=5
# counter=10
# sensor_type=0

while True:
    image_detector();
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # counter=counter-1
    # if counter<=0:
    #     counter=10
        
    #     #TODO
    #     if sensor_type==0:
    #         temp=random.randint(10,20)
    #         client.publish("cambien1",temp)
    #         sensor_type=1
    #     elif sensor_type==1:
    #         light=random.randint(0,500)
    #         client.publish("cambien2",light)
    #         sensor_type=2
    #     elif sensor_type==2:
    #         humi=random.randint(50,70)
    #         client.publish("cambien3",humi)
    #         sensor_type=0
    counter_ai=counter_ai-1
    if(counter_ai<=0):
        counter_ai=5
        ai_result=image_detector();
        client.publish("ai",ai_result)
        print("AI Output: ",ai_result)  
    time.sleep(1)
    pass