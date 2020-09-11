import xmlrpclib
import sys

ip = '127.0.0.1'
porta = '1027'
server = xmlrpclib.ServerProxy('http://' + ip + ':'+ porta)

print str(server.validate_cpf("03661861085"))
