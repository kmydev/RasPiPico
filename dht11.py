import machine
import dht
import time

# DHT11 を GPIO4 (Pin 6) に接続
dht11 = dht.DHT11(machine.Pin(4))

while True:
    try:
        dht11.measure()  # 測定
        temp = dht11.temperature()  # 温度 (°C)
        hum = dht11.humidity()  # 湿度 (%)

        print("温度: {}°C, 湿度: {}%".format(temp, hum))

    except OSError as e:
        print("DHT11 読み取りエラー:", e)

    time.sleep(2)  # 2秒ごとに測定
