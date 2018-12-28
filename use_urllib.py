
from urllib.request import urlopen, Request

url = 'https://techbeacon.com/complete-guide-data-science-bootcamps'

request = Request(url)

response = urlopen(request)

html = response.read()

print(html)

response.close()