import simplejson as json
import os

if os.path.isfile("./ages.json") and os.stat("./ages.json").st_size != 0:
    old_file = open("./ages.json", "r+")
    data = json.loads(old_file.read())
    print("Current ages is:", data["age"], "--- adding a year.")
    data["age"] += 1
    print("New age is:", data["age"])
else:
    old_file = open("./ages.json", "w+")
    data = {"name": "Luke", "age": 24}
    print("No  age found, setting default age to", data["age"])

old_file.seek(0)
old_file.write(json.dumps(data))
