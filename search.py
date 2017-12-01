import shodan
import ConfigParser
config = ConfigParser.RawConfigParser()
config.read("./config.ini")

apikey = config.get('shodan', 'apikey')
api = shodan.Shodan(apikey)
ignoredports = [80,443,8080,8081]

def searchip(ip):
	host = api.host(ip)
	for item in host['data']:
		if item['port'] not in ignoredports:
		        print """
		                Port: %s
		                Banner: %s

		        """ % (item['port'], item['data'])

def searchorg(org):
	try:
	        results = api.search(org)
	        print 'Results found: %s' % results['total']
	        for result in results['matches']:
	                print 'IP: %s' % result['ip_str']
	                print ''
	                searchip(result['ip_str'])
	except shodan.APIError, e:
	        print 'Error: %s' % e

searchorg('') #add org here