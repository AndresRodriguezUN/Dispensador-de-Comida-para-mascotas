import network
import time

def do_connect():
    
    timeout = 0 # WiFi Connection Timeout variable 

    wifi = network.WLAN(network.STA_IF)

    # Restarting WiFi
    wifi.active(False)
    time.sleep(0.5)
    wifi.active(True)

    wifi.connect('FamiliaPCortes','D1013691159')

    if not wifi.isconnected():
        print('connecting..')
        while (not wifi.isconnected() and timeout < 5):
            print(5 - timeout)
            timeout = timeout + 1
            time.sleep(1)
            
    if(wifi.isconnected()):
        print('Connected...')
        print('network config:', wifi.ifconfig())
