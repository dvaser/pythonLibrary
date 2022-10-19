import pywhatkit as kit
from datetime import datetime

try:
    time = datetime.now()
    kit.sendwhatmsg("+90532*******", "Dvase", time.hour, time.minute)
    print("Succesful")
except:
    print("Unsuccesful")
