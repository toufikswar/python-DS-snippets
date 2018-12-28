# Import package
import requests

# Specify the url: url
url = 'https://techbeacon.com/complete-guide-data-science-bootcamps'

# Packages the request, send the request and catch the response: r
r = requests.get(url)

# Extract the response: text
text = r.text

# Print the html
print(text)
