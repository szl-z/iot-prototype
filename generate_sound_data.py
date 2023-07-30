import json
import random

dictionaryList = []

for i in range(100):
  soundLevel = random.randint(1, 1000)
  timestampMilliseconds = i * 5000
  dictionary = {
    "soundLevel": soundLevel,
    "timestamp": timestampMilliseconds
  }
  dictionaryList.append(dictionary)

json_object = json.dumps(dictionaryList, indent=2)

with open("generated_sound_data.json", "w") as outfile:
  outfile.write(json_object)
