from machine import Pin
import asyncio


class LED():
    def __init__(self, pin, delay = 0.2):
        self.led = Pin(pin, Pin.OUT)
        self.led.off()
        self.delay = delay
        
    async def led_toggle(self):
        while 1:
            self.led.toggle()
            await asyncio.sleep(self.delay)
