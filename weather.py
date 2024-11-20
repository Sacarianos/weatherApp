from services import get_weather, display_weather, display_forecast, get_forecast

def main():
    print("\n  ***Welcome to the Weather App***   \n\n")

    print("                MENU         ")
    menu = 0 
    while menu not in [1,2,3,4,5]:
        menu = int(input("1. Check current weather \n2. Check 5 day forecast\n3. Favorite cities\n4. add Favorite citiy \n5. Delete favorite city\n"))
        if menu not in [1,2,3,4,5]:
            print("\nWrong input\n")
        
        match menu:
            case 1:
                zip = input("Enter the zip code for your location: ")
                units = input("Choose temperature units (C for Celsius, F for Fahrenheit): ").lower()
                units = 'metric' if units == 'c' else 'imperial'  # default to Celsius if invalid input
                print(display_weather(get_weather(zip, units)))
            case 2:
                zip = input("Enter the zip code for your location: ")
                units = input("Choose temperature units (C for Celsius, F for Fahrenheit): ").lower()
                units = 'metric' if units == 'c' else 'imperial'  # default to Celsius if invalid input
                print(display_forecast(get_forecast(zip, units)))
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
    
    


if __name__ == "__main__":
    main()