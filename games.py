import requests

num = int(input("Enter the character ID: "))  
req = requests.get(f"https://swapi.dev/api/people/{num}")  
print(f"Name: {person['name']}")
print(f"Mass: {person['mass']}")
print("---------------------------------------------------------------------")
print("Films of Star Wars:")

for film in person['films']:
    req = requests.get(film)
    film = req.json()
    print("Film title:", film['title'])

