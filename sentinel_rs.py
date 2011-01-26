import socket, sys, threading, time
# Sentinel Framework v1.0 (2011) - Professional Network Audit Tool
class SentinelScanner:
    def __init__(self, host, timeout=1.0):
        self.host = host
        self.timeout = timeout
        self.results = []
    def scan_port(self, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(self.timeout)
        if s.connect_ex((self.host, port)) == 0:
            print(f"[!] Alert: Port {port} is OPEN on {self.host}")
            self.results.append(port)
        s.close()
    def start_audit(self, port_range):
        print(f"[*] Sentinel Audit Started for {self.host}")
        threads = []
        for port in port_range:
            t = threading.Thread(target=self.scan_port, args=(port,))
            threads.append(t)
            t.start()
        for t in threads: t.join()
if __name__ == "__main__":
    SentinelScanner("192.168.1.1").start_audit([21, 22, 23, 80, 443])
