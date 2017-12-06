import shodan
import ConfigParser
from IPy import IP
from time import sleep
config = ConfigParser.RawConfigParser()
config.read("./config.ini")
apikey = config.get('shodan', 'apikey')
api = shodan.Shodan(apikey)

#Range of all GAP IP addresses
gaprange=['127.0.0.1/24',
'192.168.0.1/24']

def searchip(ip):
	sleep(1.1) #Shodan Rate-limiting FTL
	try:
		host = api.host(ip)
		for item in host['data']:
			if item['port'] not in ignoredports:
			        print """
			                Port: %s
			                Banner: %s

			        """ % (item['port'], item['data'])
	except Exception as e: print(e)," - ",ip

def searchrange(range):
	ips = IP(range)
	for ip in ips:
		print ip
		searchip(str(ip))

for iprange in gaprange:
	print "Searching ",iprange
	searchrange(iprange)