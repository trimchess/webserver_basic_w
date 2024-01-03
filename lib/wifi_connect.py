import time
import binascii
import rp2
import network

#def connect_to_network(wlan, ssid, password, country='CH'):
def connect_to_network(ssid, password, country='CH'):
    print(f'Connect to network...')
    wlan = network.WLAN(network.STA_IF)
    rp2.country = country
    wlan.active(True)
    wlan.config(pm=0xa11140)  # Disable power-save mode
    wlan.connect(ssid, password)
    
    max_wait = 10
    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_wait -= 1
        time.sleep(3)
        print(f'Connecting ({max_wait})')

    if wlan.status() != 3:
        raise RuntimeError('network connection failed')
    else:
        status = wlan.ifconfig()
        mac = binascii.hexlify(wlan.config('mac'),':').decode()
        print(f'Connected, ip = {status[0]}, MAC = {mac}')
    time.sleep(1)
