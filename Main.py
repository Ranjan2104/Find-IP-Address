# Developed by Amresh Ranjan.

import socket as s

my_hostname = s.gethostname()

print('Your Hostname is: ' + my_hostname)

my_ip = s.gethostbyname(my_hostname)

print('Your Ip Address is: ' + my_ip)

host = 'facebook.com'

ip = s.gethostbyname(host)

print('The IP Address of ' + host + ' is: '  + ip)
