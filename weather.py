from services import get_weather

def main():

    zip = input("Enter the zip code: ")
    print(get_weather(zip, "imperial"))


if __name__ == "__main__":
    main()