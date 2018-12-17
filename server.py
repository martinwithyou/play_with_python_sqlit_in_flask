from wsgiref.simple_server import make_server
from demo6 import application

httpd = make_server('',8000,application)
print('serving http on port 8000 ....')
httpd.serve_forever()