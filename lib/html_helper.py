
def write_header(w):
    w.write(b'HTTP/1.0 200 OK\r\n')
    w.write(b'Content-Type: text/html; charset=utf-8\r\n')
    w.write(b'\r\n')

def write_css_header(w):
    w.write(b'HTTP/1.0 200 OK\r\n')
    w.write(b'Content-Type: text/css; charset=utf-8\r\n')
    w.write(b'\r\n')