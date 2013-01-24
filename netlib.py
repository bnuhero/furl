import socket
import sys
import urllib2

IPAD_UA = 'Mozilla/5.0 (iPad; U; CPU OS 4_3_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8G4 Safari/6533.18.5'

def urlfetch(url, timeout=30, ua=None, server=None, port='80'):
	if server is not None:
		proxy_str = server + ':' + port
		proxy = urllib2.ProxyHandler({'http': proxy_str, 'https': proxy_str})
		opener = urllib2.build_opener(proxy)
	else:
		opener = urllib2.build_opener()

	if ua is not None:
		opener.addheaders = [('User-agent', ua)]

	urllib2.install_opener(opener)

	try:
		file = urllib2.urlopen(url, timeout=timeout)
		return file
	except (urllib2.URLError, socket.error, socket.herror, socket.gaierror, socket.timeout), (err):
		print >> sys.stderr, err
		return None
