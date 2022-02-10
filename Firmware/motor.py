from machine import Pin
import time


m0 = Pin(26,Pin.OUT)
m1 = Pin(27,Pin.OUT)
m2 = Pin(14,Pin.OUT)
m3 = Pin(12,Pin.OUT)

def motorOff():
    m0.off(), m1.off(), m2.off(), m3.off()


def rotate(flag):
   
    cont = 0
    s = 2
    x=0
    
    while (x<=flag):
        if(cont==0):
            m0.off(), m1.off(), m2.off(), m3.on()
            cont = cont+1
            time.sleep_ms(s)
        if(cont==1):
            m0.off(), m1.off(), m2.on(), m3.on()
            cont = cont+1
            time.sleep_ms(s)
        if(cont==2):
            m0.off(), m1.off(), m2.on(), m3.off()
            cont = cont+1
            time.sleep_ms(s)
        if(cont==3):
            m0.off(), m1.on(), m2.on(), m3.off()
            cont = cont+1
            time.sleep_ms(s)
        if(cont==4):
            m0.off(), m1.on(), m2.off(), m3.off()
            cont = cont+1
            time.sleep_ms(s)
        if(cont==5):
            m0.on(), m1.on(), m2.off(), m3.off()
            cont = cont+1
            time.sleep_ms(s)
        if(cont==6):
            m0.on(), m1.off(), m2.off(), m3.off()
            cont = cont+1
            time.sleep_ms(s)
        if(cont==7):
            m0.on(), m1.off(), m2.off(), m3.on()
            cont = 0
            time.sleep_ms(s)
        x = x+1
    x=0
    """
    while (x<=flag):
        if(cont==0):
            m0.on(), m1.off(), m2.off(), m3.on()
            cont = cont+1
            time.sleep_ms(s)
        if(cont==1):
            m0.off(), m1.off(), m2.on(), m3.on()
            cont = cont+1
            time.sleep_ms(s)
        if(cont==2):
            m0.off(), m1.on(), m2.on(), m3.off()
            cont = cont+1
            time.sleep_ms(s)
        if(cont==3):
            m0.on(), m1.on(), m2.off(), m3.off()
            cont = 0
            time.sleep_ms(s)
        x = x+1
    x=0
    """
    m0.off(), m1.off(), m2.off(), m3.off()

#rotate(170)