# webserver_basic_w

Basic web application for Raspberry Pico.

## html
index.html, error_404.html the projects html files
## css
styles.css The projects style sheett
## lib
The projects libraries
### web.py
see https://github.com/wybiral/micropython-aioweb. A very minimal asyncio web framework for MicroPython. basic endpoint/method based routing similar to flask (currently doesn't do any pattern matching)
### file_reader.py
helper for reading html and css files
### html_helper.py
helper for writing html/css headers
### wifi_connect.py
helper to connect to the local wifi network
### WIFI_CONFIG.py
connection data for wifi connection (ssid, psk). Must be added by the user.
