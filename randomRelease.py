import discogs_client
import random
import re

d = discogs_client.Client('kareemTest')
user = d.user("kdudemaster")
collection = user.collection_folders
all = collection[0].releases
size = all.count - 1
selection = random.randint(0, size)
result = all[selection].release


artistName = re.search("(?<=')[^']+(?=')", str(result.artists)).group(0)

print(result.title)

print(artistName)

#print(result.images)