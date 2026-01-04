
movies_2025 = {}

d_cast = ["Ranbir singh","Akshay khanna","sanjay dutt","sara Arjun"]
movies_2025["Dhurandhar"] = d_cast

c_cast = ["vicky kaushal","rashmika mandanna","akshay khanna"]
movies_2025["chhava"] = c_cast

s_cast =["aneet padda","ahaan panday","shaad ranadhawa"]
movies_2025["saiyara"] = s_cast

dashavatar_cast =["dilip prabhavlkar","priyadarshini indalkar","siddharth menon"]
movies_2025["dashavtar"] = dashavatar_cast

print(" movies 2025 dictionary :" ,movies_2025)



def actors_name(movies_2025):
    for i in movies_2025:
        if i == "actors":
        
            print("actors",  movies_2025)
        
        
ot=actors_name(movies_2025)   
print(ot)     

movie names
def print_movie(data):
    for movie in data:
        print(movie)
        
print_movie(movies_2025)                        

Dhurandhar
chhava
saiyara
dashavtar


find actor for specific movie


def actors_of_movie(data,movie_name):
    if movie_name in data:
        return data[movie_name]
    else:
        return "movie not found"
    
print(actors_of_movie(movies_2025,"chhava"))   

['vicky kaushal', 'rashmika mandanna', 'akshay khanna']  


def movies_of_actor(data,actor_name):
    movies = []
    for movie, actors in data.items():
        movies.append(movie)
    return movies

print(movies_of_actor(movies_2025,"Akshay Khanna"))                 # ['Dhurandhar', 'chhava', 'saiyara', 'dashavtar']
