from user_interface import UserInterface

def main():
    ui = UserInterface()
    #main function to run the whole app and utilize the ui
    while True:
        city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
        if city.lower() == 'exit':
            break
        detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
        
        if detailed == 'yes':
            forecast = ui.get_detailed_forecast(city)
            print(forecast)
        else:
            ui.display_weather(city)

if __name__ == "__main__":
    main()