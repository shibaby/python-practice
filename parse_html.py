from html.parser import HTMLParser
from urllib import request

class MyHtmlParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		print('<%s>' % tag)
	
	def handle_endtag(self, tag):
		print('</%s>' % tag)
	
	def handle_startendtag(self, tag, attrs):
		print('<%s/>' % tag)
	
	def handle_data(self, data):
		print(data.strip())
	
	def handle_comment(self, data):
		#print('<!--', data, '-->')
		pass
		
	def handle_entityref(self, name):
		print('&%s' % name)
		
	def handle_charref(self, name):
		print('&#%s' % name)
	
with request.urlopen('https://www.python.org/events/python-events/') as f:
	html = f.read()
parser = MyHtmlParser()
parser.feed(html.decode('utf-8'))
