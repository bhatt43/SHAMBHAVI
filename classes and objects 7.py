class Weather:
    def __init__(self, parameters):
        self.parameters = parameters  

    def __contains__(self, item):
        return item in self.parameters

    def display(self):
        print("Weather Parameters:", ", ".join(self.parameters))

if __name__ == "__main__":
    today_weather = Weather(["temperature", "humidity", "wind", "pressure"])

    today_weather.display()

    print("\nChecking weather parameters:")
    print("Is 'humidity' in weather data?", 'humidity' in today_weather) 
    print("Is 'rainfall' in weather data?", 'rainfall' in today_weather)  
