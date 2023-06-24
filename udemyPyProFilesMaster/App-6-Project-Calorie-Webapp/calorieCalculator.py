from temperatureGetter import TemperatureGetter


class CalorieCalculator:

    def __init__(self, weight, age, height, temperature):
        self.weight = weight
        self.age = age
        self.height = height
        self.temperature = temperature

    def calculateCalories(self):
        result = 10 * self.weight + 6.5 * self.height + 5 - self.temperature * 10
        return result
    

if __name__ == "__main__":
    temperature = TemperatureGetter(country='italy', city='rome').getTemperature()
    calorie = CalorieCalculator(weight=78, height=175, age=32, temperature=temperature)
    print(calorie.calculateCalories())