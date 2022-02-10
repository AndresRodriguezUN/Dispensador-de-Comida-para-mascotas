from machine import *
import time
import motor
import wlan
from umqtt.simple import MQTTClient
import ntptime
import OLED
import DFP
import gfx

# Global Variables

numComidas = 0
index = 0
comida1 = ("","")
comida2 = ("","")
comida3 = ("","")
tipo = 0
espera = 0
estadoMascota = [0,0]

#Pin_DEF
led = Pin(15,Pin.OUT) # Led de usuario
pir = Pin(5,Pin.IN) # Pin de PIR
infra = Pin(13,Pin.IN) # Pin de infra
scl = Pin(32,Pin.OUT, Pin.PULL_UP)
sda = Pin(33,Pin.OUT, Pin.PULL_UP)
pinesI2C = SoftI2C(scl = scl, sda=sda, freq = 400000)

#Motor_Config
motor.motorOff()
#Wifi_Config
wlan.do_connect()
#DFP_Config
DFP.DFP_setup()
#Oled_Config
oled = OLED.SSD1306_I2C(128, 64, pinesI2C, addr = 0x03C)
#GFX_Config
gfx = gfx.GFX(128, 64, oled.pixel)
oled.fill(0)
oled.show()

#Recv_info_fromBroker
def recv_info(topic, msg):
    global numComidas
    global comida1
    global comida2
    global comida3
    global tipo
    
    print(topic.decode())
    print(type(msg.decode()))
    if(msg == b'azul'):
        led.on()
        client.publish("diego_micro/example2", "Encendido")
    if(msg == b'rojo'):
        led.off()
        client.publish("diego_micro/example2", "Apagado")
    if(msg == b'motor'):
        motor.rotate(1000)
        client.publish("diego_micro/example2", "Moviendo")
    if(topic == b'diego_micro/numero_comidas'):
        numComidas = msg.decode()
        numComidas = int(msg)
        print(str(numComidas) + str(type(numComidas)))
    if(topic == b'diego_micro/comida_1'):
        com = msg.decode()
        comida1 = com.split(":")
        comida1[0] = int(comida1[0])
        comida1[1] = int(comida1[1])
        print(str(comida1[0]) + str(type(comida1[0])))
    if(topic == b'diego_micro/comida_2'):
        com = msg.decode()
        comida2 = com.split(":")
        comida2[0] = int(comida2[0])
        comida2[1] = int(comida2[1])
        print(str(comida2[0]) + str(type(comida2[0])))
    if(topic == b'diego_micro/comida_3'):
        com = msg.decode()
        comida3 = com.split(":")
        comida3[0] = int(comida3[0])
        comida3[1] = int(comida3[1])
        print(str(comida3[0]) + str(type(comida3[0])))
    if(topic == b'diego_micro/tipo'):
        tipo = msg.decode()
        tipo = int(tipo)

#Set_MQTTClient_toTopicSubscribe
client = MQTTClient('diego_micro/client1','broker.hivemq.com')
client.set_callback(recv_info)
client.connect()
client.subscribe(b"diego_micro/example1")
client.subscribe(b"diego_micro/numero_comidas")
client.subscribe(b"diego_micro/comida_1")
client.subscribe(b"diego_micro/comida_2")
client.subscribe(b"diego_micro/comida_3")
client.subscribe(b"diego_micro/tipo")

def rtcUpdate():
    timezone = -5
    a=1
    while(a):
        try:
            ntptime.settime()
            rtc = list(time.localtime())
            if((rtc[3]+timezone)<0):
                rtc[3] = rtc[3]+19
            else:
                rtc[3] = rtc[3]+timezone
            a=0
        except Exception as e:
            print(e)
            a=1
        time.sleep(3)
    return rtc

def stringHour(rtc):
    hour = str(rtc[3])
    if(rtc[4]<10):
        minute = "0"+str(rtc[4])
    else:
        minute = str(rtc[4])
    printHour = (hour,minute)
    return printHour

def proxCom():
    
    global numComidas
    global comida1
    global comida2
    global comida3
    
    com = [0,0,0,0,0,0]
    
    if((numComidas == 1) or (numComidas == 2) or (numComidas == 3)):
            com[0] = comida1[0]
            com[1] = comida1[1]
            com[2] = comida2[0]
            com[3] = comida2[1]
            com[4] = comida3[0]
            com[5] = comida3[1]
            
    return com

while True:
    
    # Bienvenida
    rtc = rtcUpdate()
    oled.fill(0)
    oled.text("BIENVENIDO",25,8)
    aux1 = stringHour(rtc)
    oled.text("Hora: "+ aux1[0] +":"+ aux1[1],22,25)
    oled.text("Proxima comida", 10,40)
    oled.show()
    client.check_msg()
    if(numComidas != 0):
        com = proxCom()
        oled.text("Hora: " + str(com[index])+":"+str(com[index+1]),22,50)
        oled.show()
        if(rtc[3] == com[index]):
            if(rtc[4] == com[index+1]):
                motor.rotate(170)
                if(tipo ==0):
                    DFP.sendInfo(0x16,0x00,0x00)
                    DFP.sendInfo(0x03,0x00,0x06) # Gatito
                if(tipo ==1):
                    DFP.sendInfo(0x16,0x00,0x00)
                    DFP.sendInfo(0x03,0x00,0x07) # Perrito
                v = pir.value()
                time.sleep(3)
                while((v==0) and (espera<10)):
                    v = pir.value()
                    espera = espera +1
                    time.sleep(1)
                if(espera>10):
                    estadoMascota[0] = 0
                else:
                    estadoMascota[0] = 1
                w = infra.value()
                if(w == 0):
                    estadoMascota[1] = 0
                else:
                    estadoMascota[1] = 1
                espera = 0
                index = index+2
                if((estadoMascota[0] ==0) and (estadoMascota[1] == 0)):
                    est = 1
                if((estadoMascota[0] ==0) and (estadoMascota[1] == 1)):
                    est = 4
                if((estadoMascota[0] ==1) and (estadoMascota[1] == 1)):
                    est = 8
                if((estadoMascota[0] ==1) and (estadoMascota[1] == 0)):
                    est = 4
                client.publish("diego_micro/estado", str(est))
                estadoMascota[0] = 0
                estadoMascota[1] = 0
                
        if(index > 4):
            index = 0
    
    time.sleep(1)
    
    
