from services import get_weather, display_weather

def main():
    print("  ***Welcome to the Weather App***   \n\n")
    

    zip = input("Enter the zip code for your location: ")
    units = input("Choose temperature units (C for Celsius, F for Fahrenheit): ").lower()
    units = 'metric' if units == 'c' else 'imperial'  # default to Celsius if invalid input
    print(display_weather(get_weather(zip, "imperial")))


if __name__ == "__main__":
    main()