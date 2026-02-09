import socket

target = "google.com" 

def port_scan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is OPEN")
        s.close()
    except:
        pass

print(f"Scanning target: {target}")
for p in range(1, 101):
    port_scan(p)