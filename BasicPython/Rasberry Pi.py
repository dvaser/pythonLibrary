import RPi.GPIO as GPIO
import time as t
from pygame import *
import requests

channel = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel,GPIO.IN)
mixer.init()
mixer.music.load("NNN 3 DAKKADA UYUTAN NNN.mp3")

def send_simple_message():
    print("I am sending an email.")
    return requests.post(
        "https://api.mailgun.net/v3/sandbox41fe03ba21db42e8a043e8a28b168d63.mailgun.org/messages",
        auth=("api", "30cfbd32420fa8d044fb61471acf4352-8ed21946-2a44adf5"),
        data={"from": 'hello@example.com',
            "to": ["mlkakb35@gmail.com"],
            "subject": "Bebeginiz uyandi",
            "html": "<html> Ses algılandı bebeginiz uyandi ve agliyor. </html>"})

def callback(channel):
    if GPIO.input(channel):
        print("ses algilandi")
        mixer.music.play()
        send_simple_message()
        print("ninni caliyor")
    else:
        print("aralık dışı ses")

GPIO.add_event_detect(channel,GPIO.BOTH,bouncetime=300)
GPIO.add_event_callback(channel,callback)
while True:
    t.sleep(1)