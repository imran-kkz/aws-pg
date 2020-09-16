import requests

def handler(event, context):
	r = requests.get('https://auburnalley.io')
	print(r.text[0:50])
	if r.status_code == 200:
		return 'Success!'
	else:
		return 'Failure!'
