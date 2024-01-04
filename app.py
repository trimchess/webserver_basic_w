import asyncio 
from time import sleep
from machine import Pin, ADC
import lib.wifi_connect as wifi_cnt
import lib.web as web
import lib.WIFI_CONFIG as wifi_conf
import lib.LED as led
from lib.file_reader import read_file
from lib.html_helper import write_header, write_css_header

# global definitions
app = web.App(host='0.0.0.0', port=80)
onboard = Pin('LED', Pin.OUT)
onboard.off()
temp_sensor = ADC(4)
button20 = Pin(20, Pin.IN)
button21 = Pin(21, Pin.IN)
button22 = Pin(22, Pin.IN)

# routes
@app.route('/')
async def index_handler(r, w):
    write_header(w)
    str_1 = 'OFF'
    if onboard.value() == 1:
        str_1 = 'ON'
    response_helper = 'LED Onboard: ' + str_1
    response = html_p_1 % response_helper
    w.write(response)
    await w.drain()

# /stylesheet route handler
@app.route('/styles.css')
async def style_handler(r, w):
    write_css_header(w)
    response = styles_css
    w.write(response)
    await w.drain()

# /led/off route handler
@app.route('/led/off')
async def led_off_handler(r, w):
    write_header(w)
    onboard.off()
    response = html_p_1 % 'LED Onboard: OFF'
    w.write(response)
    await w.drain()

# /led/on route handler
@app.route('/led/on')
async def led_on_handler(r, w):
    write_header(w)
    onboard.on()
    response = html_p_1 % 'LED Onboard: ON'
    w.write(response)
    await w.drain()

# /led/toggle route handler
@app.route('/led/toggle')
async def led_toggle_handler(r, w):
    write_header(w)
    onboard.toggle()
    str_1 = 'OFF'
    if onboard.value() == 1:
        str_1 = 'ON'
    response_helper = 'LED Onboard: ' + str_1
    response = html_p_1 % response_helper
    w.write(response)
    await w.drain()

# /b20/state route handler
@app.route('/b20/state')
async def b20_state_handler(r, w):
    write_header(w)
    z = "Released"
    if not button20.value():
        z = "Pressed"
    response_helper = 'B20 State ' + z
    response = html_p_1 % response_helper
    w.write(response)
    await w.drain()

# /b21/state route handler
@app.route('/b21/state')
async def b21_state_handler(r, w):
    write_header(w)
    z = "Released"
    if not button21.value():
        z = "Pressed"
    response_helper = 'B21 State ' + z
    response = html_p_1 % response_helper
    w.write(response)
    await w.drain()

# /b22/state route handler
@app.route('/b22/state')
async def b22_state_handler(r, w):
    write_header(w)
    z = "Released"
    if not button22.value():
        z = "Pressed"
    response_helper = 'B22 State ' + z
    response = html_p_1 % response_helper
    w.write(response)
    await w.drain()

# /core/temp route handler
@app.route('/core/temp')
async def core_temp_handler(r, w):
    write_header(w)
    z = str(core_temp())
    response_helper = 'TEMP ' + z
    response = html_p_1 % response_helper
    w.write(response)
    await w.drain()

def core_temp():
    conversion_factor = 3.3 / (65535)
    reading = temp_sensor.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    return round(temperature, 2)

async def main():
    the_led = led.LED(10, 1)
    webserver = asyncio.create_task(app.serve())
    task_blink = asyncio.create_task(the_led.led_toggle())
    tasks = []
    tasks.append(webserver)
    tasks.append(task_blink)
    res = await asyncio.gather(*tasks, return_exceptions=True)

if __name__ == '__main__':
    html_p_1 = read_file('/html/index.html')
    styles_css = read_file('/css/styles.css')
    try:
        wifi_cnt.connect_to_network(wifi_conf.SSID, wifi_conf.PSK, wifi_conf.COUNTRY)
    except RuntimeError as e:
        print(f'{e}, server halted')
        while (1):
            sleep(1)
    try:
        asyncio.run(main())
    except:
        asyncio.new_event_loop()



