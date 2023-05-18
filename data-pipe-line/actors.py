import requests
import json
import pickle
import langid

with open('./data/actor_ids.p','rb') as f:
    actor_ids = pickle.load(f)
f.close()


def getURL(actor_id, lang="ko-KR"):
    return f"https://api.themoviedb.org/3/person/{actor_id}?language={lang}"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMWNmYWRjNTI2NjkwNzcxNDQ1YzU4YWY1NWVjMWU3ZCIsInN1YiI6IjYzZDMxODA2ZTcyZmU4MDBlOWU2YTU1YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.QX0Tk_RtXEBQcwdsCVO__ZPTgJGmOBjTRlf2yPdXDUU"
}

actors = []
cnt = 0
N = len(actor_ids)
for actor_id in actor_ids:
    actor = requests.get(getURL(actor_id), headers=headers).json()
    newActor = {"model":"movies.actor"}
    newActor["pk"] = actor_id
    fields = {}
    fields["name"] = actor["name"]
    for aka in actor["also_known_as"]:
        if langid.classify(aka)[0] == 'ko':
            fields["name"]  = aka
            break
    fields["birthday"] = actor["birthday"]
    fields["deathday"] = actor["deathday"]
    fields["profile_path"] = actor["profile_path"]

    newActor["fields"] = fields

    actors.append(newActor)
    cnt += 1
    print(f"{cnt}/{N}")
    
file_path = './data/actors.json'
with open(file_path,'w') as f:
    json.dump(actors, f, indent=4)
f.close()

print("DONE")
