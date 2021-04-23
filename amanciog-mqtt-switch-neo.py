from adafruit_circuitplayground import cp
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    # print("Connected with result code "+str(rc))
    if rc == 0:    # if result code is equals to 0 the red dot will be turn into true
        cp.red_led = True  
        client.subscribe("cpx/#") #it will subscribe to the topic cpx/# or all

def on_message(client, userdata, msg):  
    # print(msg.topic+" "+msg.payload.decode())
    if msg.topic == "cpx/switch0":  # the code checks the condition if topic is equals to the topic of cpx specifically in switch at index 0
        if msg.payload.decode() == "true": # it check if the payload is equal to true
            cp.pixels[0] = (255, 255, 255) #  if the payload is equal to true it displays the color of white at index 0
        else:
            cp.pixels[0] = (0, 0, 0) # if it does not met a condition it will display a color of black or none 
    elif msg.topic == "cpx/switch1":  #the code checks the condition if topic is equals to the topic of cpx specifically in switch at index 1
        if msg.payload.decode() == "true": #it check if the payload is equal to true
            cp.pixels[1] = (255, 255, 255) #  if the payload is equal to true it displays the color of white at index 1
        else:
            cp.pixels[1] = (0, 0, 0)  # if it does not met a condition it will display a color of black or none 
    elif msg.topic == "cpx/switch2":  # the code checks the condition if topic is equals to the topic of cpx specifically in switch at index 2
        if msg.payload.decode() == "true": # it check if the payload is equal to true
            cp.pixels[2] = (255, 255, 255) #if the payload is equal to true it displays the color of white at index 2
        else:
            cp.pixels[2] = (0, 0, 0) #  if the payload is equal to true it displays the color of white at index 0


cp.red_led = False

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60) # change the broker into mosquito

client.loop_forever()

# Broker for online client: https://iamelijah2016.github.io/
# wss://mqtt.eclipse.org:443/mqtt
# wss://test.mosquitto.org:8081/mqtt