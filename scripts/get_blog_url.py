import requests
from bs4 import BeautifulSoup

sitemap_url = "https://www.artefact.com/blog-sitemap.xml"
output_file = "data/url_list.txt"

# Send a GET request to the sitemap URL
response = requests.get(sitemap_url)

# Parse the XML response using BeautifulSoup
soup = BeautifulSoup(response.content, "xml")

# Find all the <url> tags in the sitemap
url_tags = soup.find_all("url")

# Extract the URLs and write them to the output file
with open(output_file, "w") as file:
    for i, url_tag in enumerate(url_tags):
        if i >= 100:
            break
        url = url_tag.find("loc").text
        file.write(url + "\n")
