from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os

search = input("Enter 'search' or 'images' ")

if search == 'search':
    search = input("Enter your search term: ")
    payload = {'q': search}
    r = requests.get('http://www.bing.com/search', params=payload)

    soup = BeautifulSoup(r.text, "html.parser")
    results = soup.find("ol", {"id": "b_results"})
    links = results.findAll("li", {"class": "b_algo"})

    for item in links:
        item_text = item.find("a").text
        item_href = item.find("a").attrs["href"]

        if item_text and item_href:
            print(item_text)
            print(item_href)
elif search == 'images':
    search = input("Search for: ")
    params = {"q": search}
    dir_name = search.replace(" ", "_").lower()

    if not os.path.isdir("./image_searches/" + dir_name):
        os.makedirs("./image_searches/" + dir_name)

    r = requests.get("http://www.bing.com/images/search", params=params)

    soup = BeautifulSoup(r.text, "html.parser")
    links = soup.findAll("a", {"class": "thumb"})

    for item in links:
        try:
            img_obj = requests.get(item.attrs["href"])
            print("Getting:", item.attrs["href"])
            title = item.attrs["href"].split("/")[-1]
            try:
                img = Image.open(BytesIO(img_obj.content))
                img.save('./image_searches/' + dir_name + '/' + title, img.format)
            except:
                print("Could not save image")
        except:
            print("Could not load image")
