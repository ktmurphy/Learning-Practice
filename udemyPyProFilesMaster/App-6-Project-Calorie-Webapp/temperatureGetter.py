import requests
from selectorlib import Extractor
class TemperatureGetter:
    yamlPath = 'temperature.yaml'
    def __init__(self, city, country):
        self.city = city.replace(" ", "-")
        self.country = country.replace(" ", "-")

    def getTemperature(self):
        request = requests.get(f'https://www.timeanddate.com/weather/{self.country}/{self.city}')
        extractor = Extractor.from_yaml_file(self.yamlPath)
        raw_result = extractor.extract(request.text)
        temp = raw_result['temp'].replace('\xa0°F',"").strip()
        return float(temp)

if __name__ == "__main__":
    temp = TemperatureGetter(country = 'Rome', city = 'Italy')
    print(temp.getTemperature())

