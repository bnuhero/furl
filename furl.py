#!/usr/bin/env python
# -*- coding: utf-8 -*-
import gettext
import locale
import os
import re
import sys
import urlparse
import zipfile

import infoq

def set_trans(domain):
	LOC_DIR = os.path.dirname(os.path.abspath(__file__)) + os.sep + 'locale'
	DEF_LANG = 'en_US'

	loc = locale.getdefaultlocale()
	if loc is not None:
		try:
			trans = gettext.translation(domain, LOC_DIR, languages=[loc[0]])			
			trans.install(True, 'gettext')
		except IOError, (err):
			try:
				trans = gettext.translation(domain, LOC_DIR, languages=[DEF_LANG])
				trans.install(True, 'gettext')
			except IOError, (err):
				gettext.install(domain, LOC_DIR, unicode=True, names='gettext')
	else:
		gettext.install(domain, LOC_DIR, unicode=True, names='gettext')

def regulate_url(url):
	host_re = re.compile(r'([a-zA-z0-9]+\.)?[a-zA-z0-9]+\.[a-zA-z]{2,3}')

	scheme = ''
	netloc = ''
	path = ''
	params = ''
	query = ''
	fragment = ''

	if url is not None:
		parts = urlparse.urlparse(url)
		
		scheme = parts.scheme
		if scheme == '':			
			scheme = 'http'
		
		netloc = parts.netloc
		path = parts.path
		if netloc == '':
			pos = path.find('/')
			if pos > -1:
				host = path[0:pos]
				if host_re.match(host):
					netloc = host
					path = path[pos:]

		params = parts.params
		query = parts.query
		fragment = parts.fragment

	return urlparse.urlunparse((scheme, netloc, path, params, query, fragment))

def process(url, server=None, port='80'):	
	InfoQ_Ineterview = re.compile(r'^http://.*\.?infoq\.com/.*/?interviews/.+$', re.I)
	InfoQ_Presentation = re.compile(r'^http://.*\.?infoq\.com/.*/?presentations/.+$', re.I)

	result = InfoQ_Presentation.match(url)
	if result:
		infoq.Presentation(server, port).parse(url)
	else:
		result = InfoQ_Ineterview.match(url)
		if result:
			infoq.Interview(server, port).parse(url)
		else:
			print >> sys.stderr, _('unknown url type')+' '+url
			sys.exit()

def help():
	return '\n'+_('Usage:')+' python /path/to/furl/furl.py [-p server:port] <url>'+'\n\n'+ \
					_('find urls of the video and slides(or transcripts) in an InfoQ presentation(or interview) web page.')+'\n\n'+ \
					_('arguments:')+'\n'+ \
					'-p\t'+_('optional')+'\t'+_('the http proxy server address and port number, e.g., 127.0.0.1:8080')+'\n'+ \
					'url\t'+_('required')+'\t'+_('the url of an InfoQ presentation(or interview) web page')
def check_poxy(proxy):
	port_re = re.compile(r'\d{2,4}')
	parts = proxy.split(':')
	if len(parts)==2:
		if port_re.match(parts[1]):
			return (parts[0], parts[1])
	return None

def parse_args():
	url = None
	server = None
	port = None

	if len(sys.argv) == 2: #with url only
		url = sys.argv[1]
	elif len(sys.argv) == 4: # with -p and url
		if sys.argv[1].lower() == '-p':
			proxy = sys.argv[2]
			url = sys.argv[3]
		elif sys.argv[2].lower() == '-p':
			proxy = sys.argv[3]
			url = sys.argv[1]
		else:
			print >> sys.stdout, help()
			sys.exit()

		parts = check_poxy(proxy)
		if parts is not None:
			server = parts[0]
			port = parts[1]
		else:
			print sys.stderr, _('Invalid proxy setting: ') + proxy
			sys.exit()			

	else: #Invalid number of arguments
		print >> sys.stdout, help()
		sys.exit()

	return (url, server, port)

# Usage: python /path/to/furl/furl.py [-p server:port] <url>
# find urls of the video and slides(or transcripts) in an [InfoQ][2] presentation(or interview) web page.
# arguments:
#   -p    optional    the http proxy proxy server address and port number, e.g. 127.0.0.1:8080
#   url   required    the URL of an InfoQ presentation(or interview) web page
#                     for example, 
#                       http://www.infoq.com/interviews/end-to-end-javascript
#                       http://www.infoq.com/cn/presentations/deep-learning-and-application-to-multimedia
#                       www.infoq.com/presentations/PhoneGap
#                       ...
#
# WHAT'S NEXT?
# A new file named player.html will be created in current directory if we are successful to find the urls.
# Browse player.html for more information.
#

if __name__ == '__main__':
	#Internationalization
	set_trans('messages')

	#parse the arguments
	args = parse_args()
	if len(args)==3:
		process(regulate_url(args[0]), args[1], args[2])
	else:
		print >> sys.stderr, _('Impossible!')
		sys.exit()