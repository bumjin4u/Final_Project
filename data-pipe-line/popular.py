## 영화 id만 출력 -> 영화 디테일로 영화 정보 detail.py
import requests
import pickle
import time

def getURL(page,lang="ko-KR",region="KR"):
    return f"https://api.themoviedb.org/3/movie/popular?language={lang}&page={page}&region={region}"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMWNmYWRjNTI2NjkwNzcxNDQ1YzU4YWY1NWVjMWU3ZCIsInN1YiI6IjYzZDMxODA2ZTcyZmU4MDBlOWU2YTU1YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.QX0Tk_RtXEBQcwdsCVO__ZPTgJGmOBjTRlf2yPdXDUU"
}
## 페이지 설정 (가져올 영화 수 = page x 20)
pages = 1
data = []
for page in range(1,pages+1):
    movies = requests.get(getURL(page), headers=headers).json().get('results')

    for movie in movies:
        data.append(movie['id'])

    time.sleep(1)

file_path = './data/popular_movie_ids.p'
with open(file_path, 'wb') as f:
    pickle.dump(data, f)
f.close()

print("DONE!")