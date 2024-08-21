import requests
import time
import random
import decimal

while True:
    print("sending data...........",end='\r')
    nitrogen=float(decimal.Decimal(random.randrange(260, 280))/100)
    phosprous = random.randint(50,80)
    potasium = float(decimal.Decimal(random.randrange(280, 290))/10)
    ph = random.randint(10,60)
    moisture = random.randint(20,60)
    temperature = random.randint(50,100)
    
    URL =  f'GET https://api.thingspeak.com/update?api_key=MFANKE0TWOR5X6O9&field1={nitrogen}&field2={phosprous}&field3={potasium}'
    
    response = requests.get(URL)
    
    print("the resonse code is : ", response)
    print("DAat Sent", nitrogen,phosprous,potasium,ph,moisture,temperature)
    
    time.sleep(1)