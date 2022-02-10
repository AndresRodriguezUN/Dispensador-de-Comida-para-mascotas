from machine import *
import OLED, framebuf
from time import sleep

scl = Pin(32,Pin.OUT, Pin.PULL_UP)
sda = Pin(33,Pin.OUT, Pin.PULL_UP)
pinesI2C = SoftI2C(scl = scl, sda=sda, freq = 400000)
#Oled_Config
oled = OLED.SSD1306_I2C(128, 64, pinesI2C, addr = 0x03C) 

with open('gato_2_.pbm', 'rb') as f:   # Abre el fichero para lectura en modo binario
    f.readline()                                # Salta la línea del identificador mágico
    f.readline()                                # Salta la línea de las dimensiones de la imagen
    # f.readline()                                 # Salta la línea de comentario (descomentar si existe)
    data = bytearray(f.read())                  # Lee los datos de la imagen
fbuf = framebuf.FrameBuffer(data, 64, 64, framebuf.MONO_HLSB)   # Datos y tamaño de la imagen...
oled.framebuf.blit(fbuf, 32, 0)# Framebuffer y punto de inicio de representación
oled.invert(1)
oled.fill(1)
oled.show()                                     # Muestra el resultado