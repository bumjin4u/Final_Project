import requests
import json

url = "https://api.themoviedb.org/3/genre/movie/list?language=ko"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMWNmYWRjNTI2NjkwNzcxNDQ1YzU4YWY1NWVjMWU3ZCIsInN1YiI6IjYzZDMxODA2ZTcyZmU4MDBlOWU2YTU1YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.QX0Tk_RtXEBQcwdsCVO__ZPTgJGmOBjTRlf2yPdXDUU"
}
data = []
genres = requests.get(url, headers=headers).json().get('genres') # [{id: , name : }]

for genre in genres:
    newGenre = {}
    newGenre["model"] = "movies.genre"
    newGenre["pk"] = genre['id']
    newGenre["fields"] = {"name":genre['name']}
    data.append(newGenre)

file_path = './data/genres.json'
with open(file_path,'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

f.close()
