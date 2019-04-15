import json

# movie2 = {}
# movie2["title"] = "Minority Report"
# movie2["director"] = 'Steven Spielberg'
# movie2["composer"] = "John Williams"
# movie2["is_awesome"] = True
# movie2["budget"] = 1020000
# movie2["cinematographer"] = "Janusz Kami\u0144ski"
#
# file2 = open("movie_2.txt", 'w', encoding='utf-8')
# json.dump(movie2,file2,ensure_ascii=False)
# file2.close()

json_file = open('movie_2.txt','r',encoding='utf-8')
movie = json.load(json_file)
json_file.close()
if movie['is_awesome']:
    x = (movie['director']).split()
print(x)


