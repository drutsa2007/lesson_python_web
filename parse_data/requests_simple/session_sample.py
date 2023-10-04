import requests

sess = requests.Session()
sess.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
resp = sess.get('https://httpbin.org/cookies')
print(resp.text)

sess.headers.update({'one': 'true', 'two': 'true'})
resp = sess.get('https://httpbin.org/headers', headers={'one': None})
print(resp.text)