# Program by Abhinav Kumar
# Email abhisri1997@gmail.com
# Github http://github.com/dev-elixir

import random
import urllib.request

print("Input URL of the picture to download!\n")
site = input("Input the URL here!\n")


def download_url(url):
    f_name = random.randrange(1, 1000)
    name = str(f_name) + ".jpeg"
    urllib.request.urlretrieve(url, name)
    print("Your photo is now downloading!")


download_url(site)
