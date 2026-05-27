from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["movieReviewDB"]

movies = db["movies"]
reviews = db["reviews"]

print("Movies Collection:\n")

for movie in movies.find():
    print(movie)

print("\nReviews Collection:\n")

for review in reviews.find():
    print(review)

movies.insert_one({
    "title": "Avatar",
    "genre": "Sci-Fi",
    "year": 2009,
    "director": "James Cameron",
    "rating": 8.5
})

movie = movies.find_one({"title": "Inception"})
print(movie)