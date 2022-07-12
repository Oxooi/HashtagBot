import requests
import math

url = "http://localhost/views/hashtag.php"                          # url to post request
hash = input("Enter the hashtag (without #): ")                     # get hashtag from user
nbr = input("how many hashtag do you want ? ")                      # get number of hashtag
nbr = int(nbr)                                                      # convert nbr to int


def progress_bar(progress, total):                                  # progress bar function
    percent = (progress/total)*100                                  # calculate percentage
    bar = '█' * int(percent) + '-' * int(100-percent)               # create progress bar
    print ('\r', bar, '{:.2f}%'.format(percent), end='')            # print progress bar


def create_Hashtag():                                               # create hashtag function
                                                                    # print init message
    print ("hashtag being created, this could take a while...")
    progress_bar(0, nbr)                                            # call progress bar function
    for i in range(nbr):                                            # loop for nbr of hashtag

        myobj = {'hashtag': '#' + hash}                             # create json object
        x = requests.post(url, data=myobj)                          # post request with json object
        progress_bar(i+1, nbr)                                      # call progress bar function


create_Hashtag()
