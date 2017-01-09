import requests
from io import BytesIO
from PIL import Image

payload = {'q': 'pizza'}
r = requests.get('http://www.bing.com/search', params=payload)

print("Status:", r.status_code)

print(r.url)
print(r.text)

f = open("./page.html", "w+")
f.write(r.text)

r = requests.get('http://wallpapercave.com/wp/TuVhQdr.jpg')

print("\n\nStatus code:", r.status_code)

image = Image.open(BytesIO(r.content))

print(image.size, image.format, image.mode)

path = "./Image." + image.format

try:
    image.save(path, image.format)
except IOError:
    print("Cannot save image.")
