# [
#   {
#     "model": "movies.movie",
#     "pk": 2,
#     "fields": {
#         "": "Mean everybody treatment.",
#         "overview": "Majority factor break treatment sense. Republican community green gun generation care.\nFly under travel couple small foot see. Manage wish court ground.",
#         "release_date": "2013-09-19T00:06:55Z",
#         "poster_path": "Throw identify ball born. He with wide future.\nLearn training child. Hundred off tree benefit none. Instead it hot tend focus.",
#         "actors": [
#             6,
#             9
#         ]
#     }
#   },
# ]

## 영화 id만 출력 -> 영화 디테일로 영화 정보
import requests
import pickle
import json
import time

with open('./data/popular_movie_ids.p','rb') as f:
    ids = pickle.load(f)
f.close()

def getDetailURL(movie_id,lang="ko-KR"):
    return f"https://api.themoviedb.org/3/movie/{movie_id}?language={lang}"

def getCreditURL(movie_id,lang="ko-KR"):
    return f"https://api.themoviedb.org/3/movie/{movie_id}/credits?language={lang}"


headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMWNmYWRjNTI2NjkwNzcxNDQ1YzU4YWY1NWVjMWU3ZCIsInN1YiI6IjYzZDMxODA2ZTcyZmU4MDBlOWU2YTU1YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.QX0Tk_RtXEBQcwdsCVO__ZPTgJGmOBjTRlf2yPdXDUU"
}
movie_data = []
actor_ids = set()
cnt = 0
N = len(ids)
for movie_id in ids:
    actors = []
    movie = requests.get(getDetailURL(movie_id), headers=headers).json()
    newMovie = {"model":"movies.movie"}
    newMovie["pk"] = movie_id
    fields = {}
    fields["title"] = movie["title"]
    fields["original_title"] = movie["original_title"]
    fields['adult'] = movie["adult"]
    if fields['adult']:
        print("True 나옴")
    fields["overview"] = movie["overview"]
    fields["genres"] = [ genre["id"] for genre in movie["genres"]]
    fields["tagline"] = movie["tagline"]
    fields["runtime"] = movie["runtime"]
    fields["release_date"] = movie["release_date"]
    fields["backdrop_path"] = movie["backdrop_path"]
    fields["poster_path"] = movie["poster_path"]
    fields["status"] = movie["status"]
    fields["vote_average"] = movie["vote_average"]
    fields["vote_count"] = movie["vote_count"]

    actor_reponse = requests.get(getCreditURL(movie_id), headers=headers).json().get("cast")
    actors = [ actor["id"] for actor in actor_reponse if actor["profile_path"] ]
    fields["actors"] = actors
    
    newMovie["fields"] = fields
    movie_data.append(newMovie)
    actor_ids.update(actors)
    cnt += 1
    print(f"{cnt}/{N}")

print(len(actor_ids))
movies_file_path = './data/movies.json'
with open(movies_file_path, 'w') as f:
    json.dump(movie_data, f, indent=4)
f.close()

actor_ids = list(actor_ids)
actor_ids_file_path = './data/actor_ids.p'
with open(actor_ids_file_path, 'wb') as w:
    pickle.dump(actor_ids, w)
w.close()

print("DONE!")