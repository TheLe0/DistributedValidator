import SimpleXMLRPCServer
import datetime
import sys
import re

from lib import validate_cpf

porta = int(1027)

print "The Server was Started"

server = SimpleXMLRPCServer.SimpleXMLRPCServer(("localhost", porta ))
server.register_function(validate_cpf, "validate_cpf")
server.serve_forever()
