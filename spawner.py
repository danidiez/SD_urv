from pyactor.context import set_context, create_host, serve_forever
import os, commands, sys

if __name__ == "__main__":
	set_context()
	ip= sys.argv[1]
	ip_portR= sys.argv[2]
	n =int(sys.argv[3])
	port = 6000
	for i in range(n):
		port+= 1
		ip_port="%s:%s" % (ip,port)
		command = "python actor.py %s %s &" % (ip_port,ip_portR)
		os.system(command)

