# Import requests package
import requests

# Assign URL to variable: url
url = 'http://www.omdbapi.com/?apikey=ff21610b&t=social+network'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Print the text of the response
print(r.text)

# Decode the JSON data into a dictionary: json_data
json_data = r.json()


# We get a dictionany called json_data -  we iterate over :
for k, value in json_data.items():
    print (k, value, sep=": ")


###################################################################################################

url2 = "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza"

r = requests.get(url2)

json_data = r.json()

print(json_data)
print('\n')



print(json_data['query']['pages']['24768']['extract'])