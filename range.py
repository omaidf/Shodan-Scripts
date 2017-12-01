import shodan
import ConfigParser
from IPy import IP
config = ConfigParser.RawConfigParser()
config.read("./config.ini")
apikey = config.get('shodan', 'apikey')
api = shodan.Shodan(apikey)

def searchip(ip):
	host = api.host(ip)
	for item in host['data']:
		if item['port'] not in ignoredports:
		        print """
		                Port: %s
		                Banner: %s

		        """ % (item['port'], item['data'])

ip2 = IP('') #add IP range here
print
for x in ip2:
	print x
	searchip(x)

