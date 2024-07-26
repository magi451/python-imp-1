import requests

def get_character_info(character_id):
    url = f"https://swapi.dev/api/people/{character_id}/"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        name = data.get('name', 'Unknown')
        mass = data.get('mass', 'Unknown')
        height = data.get('height', 'Unknown')
        hair_color = data.get('hair_color', 'Unknown')
        skin_color = data.get('skin_color', 'Unknown')
        films = data.get('films', [])

        print(f"Name: {name}")
        print(f"Mass: {mass}")
        print(f"Height: {height}")
        print(f"Hair color: {hair_color}")
        print(f"Skin color: {skin_color}")
        print("---------------------------------------------------------------------")
        print("Films of Star Wars:")
        for film_url in films:
            film_response = requests.get(film_url)
            if film_response.status_code == 200:
                film_data = film_response.json()
                print("Film title:", film_data.get('title', 'Unknown'))
            else:
                print(f"Error fetching film data for {film_url}")
    else:
        print(f"Error fetching character data for ID {character_id}")
try:
    char_id = int(input("Enter the ID of the Star Wars character you'd like to learn more about: "))
    get_character_info(char_id)
except ValueError:
    print("Invalid input. Please enter a valid numeric character ID.")
