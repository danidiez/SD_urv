from pyactor.context import set_context, create_host, serve_forever 
import sys

if __name__ == "__main__":
	set_context()
	ip_port = sys.argv[1]
	ip_portR = sys.argv[2]
	nameHost = 'http://%s' % ip_port
    	host = create_host(nameHost)
	regisIp = 'http://%s/regis' % ip_portR
	registry = host.lookup_url(regisIp, 'Registry','master')
	registry.bind(host)

	serve_forever()
