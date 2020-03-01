# Importing necessary packages

import tmdbsimple as tmdb
import requests
import json
import os
import shutil

# Define path to your movies and arrange them into list
main_dir = "E:\\Movies\\Hollywood\\"
movie_list = os.listdir(main_dir)

# url to make GET request in order to get the genre ids and names
url = 'https://api.themoviedb.org/3/genre/movie/list?api_key=6e9e0b5c921ae73efecc38ec4c381d09&language=en-US'
r = requests.get(url)

# converting data into json
json_data = json.loads(r.text)
genre_id = (json_data['genres'])

# define your API key here
tmdb.API_KEY = '6e9e0b5c921ae73efecc38ec4c381d09'

# initialising search instance 
search = tmdb.Search()

# loop in the movie list extracted from local disk
for movie_name in movie_list:
	try:
		# searching for movie, but remember to remove any file extensions (.mkv, .mp4, etc)

		response = search.movie(query=movie_name.split('.')[0])

		# get the first dictionary from the list
		movie_result = search.results[0]

		# get first genre id
		movie_genre = movie_result['genre_ids'][0]

		# we got movie genre id, now we need to get the genre name

		for gid in genre_id:
			# we got the genre id, if this id is of Action, then make the Actoin folder and move the movie into that folder
			# if folder is already created, it will pass and ignore

			# same steps will be repeated for Drama genre
			# if movie does not belong to any of the genre, then it will be left in the same folder

			# I decided to sort movies into two categories only
			# because most of the movies in my collection belongs to these two categories,
			# rest of the movies are left in the same folder

			if gid['id'] == movie_genre:
				if gid['name'] == 'Action':
					try:
                        os.mkdir('E:\\Movies\\Hollywood\\Action')
                    except (FileExistsError):
                        pass
                       print(movie_name+ ' ' +gid['name'])
					os.mkdir('E:\\Movies\\Hollywood\\Action')
					shutil.move('E:\\Movies\\Hollywood\\'+movie_name, 'E:\\Movies\\Hollywood\\Action\\'+movie_name)
				elif gid['name'] == 'Drama':
                    try:
                        os.mkdir('E:\\Movies\\Hollywood\\Drama')
                    except (FileExistsError):
                        pass
                    print(movie_name+ ' ' +gid['name'])
                    shutil.move('E:\\Movies\\Hollywood\\'+movie_name, 'E:\\Movies\\Hollywood\\Drama\\'+movie_name)
                else:
                    print('Passed',movie_name)
				print(movie_name+ ' ' +gid['name'])

			# if movie not found in search.movie(),
			# most probably because of spelling mistake, 
			# it will throw IndexError which can be handled using except block
	except (IndexError):
		print('Movie Not Found')
        