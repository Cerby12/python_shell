import json
import socket
import sys
import os
import random 
import string 
import subprocess
from pystyle import Colors
import datetime

command_list = ['help','pc_name','ipv4','data_and_time','random mail','system','cls','exit','pc_off']

def random_string():
    number_random = random.randint(20,40)
    return ''.join(random.choice(string.ascii_letters) for i in range(number_random))



with open('configs.json') as f:
    config = json.load(f)
    color = config['color']
    shell_name = config['shell_name']
    shell_version = config['version']

reset_color = Colors.reset
orange = Colors.orange

print(f'Welcome to ' + orange + shell_name + reset_color + ' version' + orange + '\t' + shell_version + reset_color)
class shell:
    def __init__(self):
        while True:
            self.color = color
            self.name = shell_name
            self.version = shell_version
            if color == 'red':
                self.command = input(Colors.red + f'{shell_name} $ ')
            elif color == 'blue':
                self.command = input(Colors.blue + f'{shell_name} $ ')
            elif color == 'yellow':
                self.command = input(Colors.yellow + f'{shell_name} $ ')
            elif color == 'purple':
                self.command = input(Colors.purple + f'{shell_name} $ ')
            
            else:
                print('Color not found')
                sys.exit()

            if self.command in command_list:
                pass

            else:
                print('Command not found.')

            if self.command == 'help':
                print(command_list)
            
            elif self.command == 'pc_name':
                print(os.getlogin())
            
            elif self.command == 'ipv4':
                print(socket.gethostbyname(socket.gethostname()))
            
            elif self.command == 'data_and_time':
                print(datetime.datetime.now())
            
            elif self.command == 'random mail':
                dominian_list = ['gmail.com','yahoo.com','hotmail.com','outlook.com']
                print(random_string() + '@' + random.choice(dominian_list))
            
            elif self.command == 'system':
                print(sys.platform)
            
            elif self.command == 'cls':
                os.system('cls')
            
            elif self.command == 'exit':
                print(reset_color +'shell off')
                sys.exit()
            
            elif self.command == 'pc_off':
                print(reset_color + 'pc off')
                subprocess.run('shutdown -s',shell=True)
            
shell()
