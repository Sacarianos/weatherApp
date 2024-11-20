import json
from pathlib import Path
from services import get_weather, display_weather

FAVORITES_FILE = Path("favorites.json")

def load_favorites():
    if FAVORITES_FILE.exists():
        with open(FAVORITES_FILE, "r") as file:
            return json.load(file)
    return []

def save_favorites(favorites):
    """Save favorite cities to a file."""
    with open(FAVORITES_FILE, "w") as file:
        json.dump(favorites, file)

def add_favorite(city, zip):
    favorites = load_favorites()
    city_tuple = (city, zip)
    if city_tuple not in favorites:
        favorites.append(city_tuple)
        save_favorites(favorites)
        print(f"Added {city} (Zip: {zip}) to favorites.")
    else:
        print(f"{city} (Zip: {zip}) is already in favorites.")

def remove_favorite(city, zip):
    favorites = load_favorites()
    city_tuple = (city, zip)
    if city_tuple in favorites:
        favorites.remove(city_tuple)
        save_favorites(favorites)
        print(f"Removed {city} (Zip: {zip}) from favorites.")
    else:
        print(f"{city} (Zip: {zip}) is not in favorites.")
        
def view_favorites():
    """Display the list of favorite cities."""
    favorites = load_favorites()
    if favorites:
        print("Favorite Cities:")
        for i in range(len(favorites)):
            print("")
            weather = get_weather(favorites[i][1])
            print(display_weather(weather))
    else:
        print("No favorite cities yet.")