# DHT11で計測した温度、湿度をLCDディスプレイAQM0802に表示する
# DHT11はデータピンをGP0, LCDはI2C0に接続する

from machine import I2C, Pin
import time

# I2C初期化
i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=100000)  # I2C0 (GP4, GP5)
LCD_ADDR = 0x3E  # LCDのI2Cアドレス

# LCDにコマンドを送る関数
def lcd_command(cmd):
    i2c.writeto(LCD_ADDR, bytearray([0x00, cmd]))
    time.sleep(0.05)  # 少し待つ

# LCDにデータを送る関数（文字を表示）
def lcd_data(data):
    i2c.writeto(LCD_ADDR, bytearray([0x40, data]))
    #time.sleep(0.05)

# LCDの初期化シーケンス
def lcd_init():
    lcd_command(0x38)  # 8ビットモード
    lcd_command(0x39)  # 拡張コマンドセット
    lcd_command(0x14)  # 内部オシレータ周波数設定
    lcd_command(0x70)  # コントラスト設定
    lcd_command(0x56)  # 電源制御
    lcd_command(0x6C)  # 電圧フォロワー
    time.sleep(0.2)
    lcd_command(0x38)  # 通常モードへ戻す
    lcd_command(0x0C)  # 表示ON, カーソルOFF
    lcd_command(0x01)  # 画面クリア
    time.sleep(0.2)

# LCDに文字を表示
def lcd_print(text):
    for char in text:
        lcd_data(ord(char))

import dht

# dht11 初期化
dht11 = dht.DHT11(machine.Pin(0))
    
# LCD初期化
lcd_init()

while True:
    try:
        dht11.measure()  # 測定
        temp = dht11.temperature()  # 温度 (°C)
        hum = dht11.humidity()  # 湿度 (%)
        lcdstr = '{}C:{}%'.format(temp, hum)
        lcd_print(lcdstr)

    except OSError as e:
        lcd_print("ERROR")

    time.sleep(2)  # 2秒ごとに測定
    lcd_command(0x80) # カーソルをLCD先頭に戻す
    
    #lcd_command(0x01)
    #time.sleep(0.2)