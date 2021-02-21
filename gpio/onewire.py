"""
Reading temperature via Dallas DS18B20 Onewire sensors.

Sensor:
    red: Vdd +
    black: GND
    yellow: DQ data

GPIO:
    pin 1 (3.3 V +) Vdd
    pin 4 DQ
    pin GND GND

Resistor 4k7 between pin 1 and 4.

Example reading from sys file:

0f 00 4b 46 ff ff 06 10 0c : crc=0c YES
0f 00 4b 46 ff ff 06 10 0c t=7375

-> parsing CRC YES
-> parsing temperature (last entry) and by 1000 division.

"""


import os
import time


BASE_PATH = "/sys/bus/w1/devices"
SENSORS = {
    "28-011912631a74": "BT13",
    "28-0119126bb7a1": "BT14",
    "28-01191272a40c": "BT15",
}
INPUT_FILE = "w1_slave"

CRC_OK = "YES"
TEMPERATURE_PREFIX = "t="
DIVIDER = 1000
DEGREES = f"{chr(176)}C"


def read_temperature(sensor_addr):
    with open(os.path.join(BASE_PATH, sensor_addr, INPUT_FILE), "r")  as ifile:
        lines = ifile.readlines()
        try:
            if not lines[0].strip().endswith(CRC_OK):
                return None
            temp = lines[1].strip().rsplit(" ", maxsplit=1)[-1]
            temp = temp.replace(TEMPERATURE_PREFIX, "")
            return float(temp) / DIVIDER
        except Exception as exc:
            print(f"Exception while reading, reason: {exc}")
            return None


def read_temperatures():
    while True:
        for sensor_addr, sensor_name in SENSORS.items():
            temp = read_temperature(sensor_addr)
            print(f"temperature from {sensor_name}: {temp} {DEGREES}")
            time.sleep(0.2)
        time.sleep(1)
        print()


def main():
    read_temperatures()


if __name__ == "__main__":
    main()
