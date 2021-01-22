from wsgiref.simple_server import make_server
from cgi import parse_qs, escape

def application(environ, start_response):
	status = '200 OK'
	headers = [
		('Content-Type', 'text/plain')
	]
	body = ''
	d = parse_qs(environ['QUERY_STRING'])
	for key in d:
		body += key+'='+d[key]+'\n'
	start_response(status, headers)
	return [ body ]