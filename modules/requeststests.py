import requests
from io import BytesIO
from PIL import Image
import simplejson as json

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

my_data = {"name": "Luke", "email": "luke@example.io"}
r = requests.post("http://www.w3schools.com/php/welcome.php", data=my_data)

f = open("./myfile.html", "w+")
f.write(r.text)

url = "https://www.googleapis.com/urlshortener/v1/url"
payload = {"longUrl": "http://www.example.com"}
headers = {"Content-Type": "application/json"}
r = requests.post(url, json=payload, headers=headers)

print("\n" + r.text + "\n")
print(json.loads(r.text)["error"]["code"])
print(r.headers)
