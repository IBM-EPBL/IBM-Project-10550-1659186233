import random
i=0
while(i<=5):
    
    temp = random.randint(1,250)
    humidity = random.randint(1,100)
    print("Temperature :"+str(temp))
    print("Humidity :"+str(humidity))

    if ((temp<100&temp>60) & humidity==50):
        print("Both Temperature and humidity is Normal")
        print("Alarm Off")
        

    elif(temp>100 & humidity<50):
        print("Temperature is high")
        print("Humidity is low")
        print("Alarm On")

    elif(temp<60 & humidity>50):
        print("Temperature is LOW")
        print("Humidity is HIGH")
        print("Alarm On")

    elif((temp<100&temp>60) & humidity<50):
        print("Temperature is Normal")
        print("Humidity is low")
        print("Alarm Off")

    elif((temp<100&temp>60) & humidity>50):
        print("Temperature is Normal")
        print("Humidity is HIGH")
        print("Alarm Off")
    print("---------------------------------")
    i+=1
