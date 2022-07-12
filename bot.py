import requests
import math
import colorama

url = "http://localhost/views/hashtag.php"                          # url to post request
hash = input("Enter the hashtag (without #): ")                     # get hashtag from user
nbr = input("how many hashtag do you want ? ")                      # get number of hashtag
nbr = int(nbr)                                                      # convert nbr to int


def progress_bar(progress, total, color=colorama.Fore.YELLOW):      # progress bar function with Yellow font color
    percent = (progress/total)*100                                  # calculate percentage
    bar = '█' * int(percent) + '-' * int(100-percent)               # create progress bar
    print (color + f'\r', bar, '{:.2f}%'.format(percent), end='')   # print progress bar with color
    if progress == total:                                           # if progress is equal to total
        print(colorama.Fore.GREEN + 
        f'\r', bar, '{:.2f}%'.format(percent), end='')              #then print progress bar with green color                     


def create_Hashtag():                                               # create hashtag function
                                                                    # print init message
    print ("hashtag being created, this could take a while...")
    progress_bar(0, nbr)                                            # call progress bar function
    for i in range(nbr):                                            # loop for nbr of hashtag

        myobj = {'hashtag': '#' + hash}                             # create json object
        x = requests.post(url, data=myobj)                          # post request with json object
        progress_bar(i+1, nbr)                                      # call progress bar function


create_Hashtag()
print(colorama.Fore.RESET)