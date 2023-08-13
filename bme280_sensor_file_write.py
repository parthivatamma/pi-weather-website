import bme280
import smbus2
from time import sleep
import json

port = 1
address = 0x77 # Adafruit BME280 address. Other BME280s may be different
bus = smbus2.SMBus(port)

weatherDict = {
    "temp":0,
    "pressure":0,
    "humidity":0,
    }

bme280.load_calibration_params(bus,address)

while True:
    bme280_data = bme280.sample(bus,address)
    humidity = bme280_data.humidity
    pressure = bme280_data.pressure
    ambient_temperature = bme280_data.temperature
    weatherDict.update(
        {
            "temp":ambient_temperature,
            "pressure":pressure,
            "humidity":humidity
        }
    )
    with open("tests.json", "w") as writeFile:
        json.dump(weatherDict, writeFile)
    print(humidity, pressure, ambient_temperature)
    sleep(20)
