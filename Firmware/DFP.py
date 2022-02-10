#Constantes
from machine import UART
import time

START_BYTE  = 0x7E
VERSION_BYTE = 0xFF
COMMAND_LENGTH = 0x06
END_BYTE  = 0xEF
ACKNOWLEDGE = 0x00

uart1 = UART(2,9600)
uart1.init(9600,bits=8,parity=None, stop=2)


def highByte(v):
    v>>=8
    return v%256
    
def lowByte(v):
    return v%256

def highNibble(v):
    v>>=4
    return v%16

def lowNibble(v):
    return v%16


def sendInfo(cmd, param1, param2):
    checksum = -(VERSION_BYTE + COMMAND_LENGTH + cmd + ACKNOWLEDGE + param1 + param2)
    command_line = bytes([START_BYTE, VERSION_BYTE, COMMAND_LENGTH, cmd, ACKNOWLEDGE, param1, param2, highByte(checksum), lowByte(checksum), END_BYTE])
    uart1.write(command_line)
    
def DFP_setup():
    
    #myDFPlayer.volume(25);
    #7E FF 06 06 XX 00 19 XX EF 
    sendInfo(0x06,0x00,0x20)
   
    #myDFPlayer.EQ(DFPLAYER_EQ_NORMAL)
    #7E FF 06 07 XX 00 00 XX EF 
    sendInfo(0x07,0x00,0x00)
  
    #myDFPlayer.outputDevice(DFPLAYER_DEVICE_SD)
    #7E FF 06 09 XX 00 02 XX EF 
    sendInfo(0x09,0x00,0x02)

'''
DFP_setup()

sendInfo(0x16,0x00,0x00)
sendInfo(0x03,0x00,0x06) # Gatito
sendInfo(0x03,0x00,0x07) # Perrito
time.sleep(2)
'''