import requests
import random

url = "http://localhost/views/hashtag.php"
hash = input("Enter the hashtag (without #): ")
nbr = input("how many hashtag do you want ? ")
nbr = int(nbr)

print ("hashtag being created, this could take a while...")
for i in range(nbr):

    myobj = {'hashtag': '#' + hash}
    x = requests.post(url, data=myobj)

print ("hashtags created !")