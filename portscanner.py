
import socket
import termcolor

def scan_port(ipadd, port):
	try:
		sock = socket.socket()
		sock.connect((ipadd, port))

		print(termcolor.colored((f"[+] Port {port} Mengo"), "green"))

		sock.close()
	except:
		pass

def scan(addr, ports):
	print(f"\n[*] {addr}: ")
	for p in range(1,ports):
		scan_port(addr, p)

targets = input("[*] Lebokke IP ne Lek (nek +1 = 1,2,3): ")
ports = int(input("[*] Wani piro (port): "))

if ',' in targets:
	print(termcolor.colored(("[*] Kosek..."), "yellow"))
	for i in targets.split(','):
		scan(i.strip(' '), ports)
else:
	scan(targets,ports)
