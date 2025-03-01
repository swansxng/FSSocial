import os, socket
os.system(f'python manage.py runsslserver {socket.gethostbyname(socket.getfqdn())}:443')
#