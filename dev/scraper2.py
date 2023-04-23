import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# Set up the webdriver
options = webdriver.ChromeOptions()
options.add_argument('--headless') # Run the browser in headless mode
driver = webdriver.Chrome(options=options)

# Set the URL of the webpage you want to download
url = 'https://www.example.com/'

# Make the request and get the HTML content
response = requests.get(url)
html_content = response.text

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Get all the images on the page
for img in soup.find_all('img'):
    img_url = img.get('src')
    if img_url.startswith('//'):
        img_url = 'http:' + img_url
    elif not img_url.startswith('http'):
        img_url = os.path.join(url, img_url)
    img_response = requests.get(img_url)
    with open(os.path.basename(img_url), 'wb') as f:
        f.write(img_response.content)

# Get all the videos on the page
for vid in soup.find_all('video'):
    vid_url = vid.get('src')
    if vid_url.startswith('//'):
        vid_url = 'http:' + vid_url
    elif not vid_url.startswith('http'):
        vid_url = os.path.join(url, vid_url)
    vid_response = requests.get(vid_url)
    with open(os.path.basename(vid_url), 'wb') as f:
        f.write(vid_response.content)

# Use selenium to get all the dynamically loaded content
driver.get(url)
dynamic_content = driver.page_source
soup = BeautifulSoup(dynamic_content, 'html.parser')

# Get all the images in the dynamically loaded content
for img in soup.find_all('img'):
    img_url = img.get('src')
    if img_url.startswith('//'):
        img_url = 'http:' + img_url
    elif not img_url.startswith('http'):
        img_url = os.path.join(url, img_url)
    img_response = requests.get(img_url)
    with open(os.path.basename(img_url), 'wb') as f:
        f.write(img_response.content)

# Quit the webdriver
driver.quit()