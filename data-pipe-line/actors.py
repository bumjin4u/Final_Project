# [
#     {
#         "model": "movies.actor",
#         "pk": 1,
#         "fields": {
#             "name": "Case imagine simple shake ahead try."
#         }
#     },
# ]

import requests
import json
import pickle
from googletrans import Translator

translator = Translator()

with open('./data/actor_ids.p','rb') as f:
    actor_ids = pickle.load(f)
f.close()


def getURL(actor_id, lang="ko-KR"):
    return f"https://api.themoviedb.org/3/person/{actor_id}?language={lang}"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMWNmYWRjNTI2NjkwNzcxNDQ1YzU4YWY1NWVjMWU3ZCIsInN1YiI6IjYzZDMxODA2ZTcyZmU4MDBlOWU2YTU1YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.QX0Tk_RtXEBQcwdsCVO__ZPTgJGmOBjTRlf2yPdXDUU"
}

print(len(actor_ids))
actors = []
cnt = 0
for actor_id in actor_ids:
    actor = requests.get(getURL(actor_id), headers=headers).json()
    newActor = {"model":"movies.actor"}
    newActor["pk"] = actor_id
    fields = {}
    fields["name"] = actor["name"]
    for aka in actor["also_known_as"]:
        if translator.detect(aka) == "ko":
            fields["name"]  = aka
            break
    fields["birthday"] = actor["birthday"]
    fields["deathday"] = actor["deathday"]
    fields["profile_path"] = actor["profile_path"]

    newActor["fields"] = fields

    actors.append(newActor)
    cnt += 1
    if cnt == 40:
        break
file_path = './data/actors.json'
with open(file_path,'w') as f:
    json.dump(actors, f, indent=4)
f.close()

print("DONE")
