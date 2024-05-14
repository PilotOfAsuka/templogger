import time
from datetime import datetime
from temp_module import get_mi_sensor_data
from func import load_json, save_in_json

temp_file = "temp.json"

# Словарь для хранения температуры
temperature_log = load_json(temp_file)

# Функция для записи температуры в словарь
def log_temperature():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    temperature, humidity, battery_level = get_mi_sensor_data()
    temperature_log[current_time] = temperature
    save_in_json(temperature_log, temp_file)
    print(f"Temperature logged at {current_time}: {temperature}°C")

# Основной цикл
while True:
    log_temperature()
    time.sleep(1800)  # Ожидание 30 минут (1800 секунд)
