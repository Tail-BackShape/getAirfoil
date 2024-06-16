import requests
from bs4 import BeautifulSoup
import os
import time
import random

# make directory for saving .dat files
download_dir = 'dat_files'
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

# URL of the airfoil database
base_url = 'https://m-selig.ae.illinois.edu/ads/coord_database.html'
base_site = 'https://m-selig.ae.illinois.edu/ads/'

# get the HTML content of the URL
response = requests.get(base_url)
soup = BeautifulSoup(response.content, 'html.parser')

# get all links in the HTML content
links = soup.find_all('a')

# download all .dat files
for link in links:
    href = link.get('href')
    if href and href.endswith('.dat'):
        file_url = base_site + href
        file_name = os.path.join(download_dir, href.split('/')[-1])

        # save the file
        file_response = requests.get(file_url)
        with open(file_name, 'wb') as file:
            file.write(file_response.content)

        print(f'Downloaded: {file_name}')

        # sleep for a random time between 1 and 3 seconds
        time.sleep(random.uniform(1, 3))
