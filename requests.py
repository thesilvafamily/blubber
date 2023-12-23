import requests

# this is the URL we want to request 
url = "https://raw.githubusercontent.com/thesilvafamily/blubber/lab/test.txt"

# request the URL from the web server 
response = requests.get(url)

# test for success (should be 200)
assert(response.status_code == 200)

# print the content of the response 
print(response.content)
