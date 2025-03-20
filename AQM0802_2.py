from machine import I2C, Pin
import time

# I2Cの設定 (I2C0: SDA=GP4, SCL=GP5)
i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=400000)

# AE-AQM0802のI2Cアドレス
LCD_ADDR = 0x3E  # ST7032のデフォルトアドレス

# LCDにコマンドを送信する関数
def lcd_command(cmd):
    i2c.writeto(LCD_ADDR, bytearray([0x00, cmd]))
    time.sleep_ms(1)

# LCDにデータを送信する関数（文字表示用）
def lcd_data(data):
    i2c.writeto(LCD_ADDR, bytearray([0x40, data]))
    time.sleep_ms(1)

# LCDの初期化
def lcd_init():
    time.sleep_ms(50)  # 電源ON後の待機
    lcd_command(0x38)  # 8ビットモード, 2行表示
    lcd_command(0x39)  # 拡張コマンドセット
    lcd_command(0x14)  # 内部クロック設定
    lcd_command(0x70)  # コントラスト設定 (下位4ビット)
    lcd_command(0x56)  # コントラスト設定 (上位2ビット) + 電源制御
    lcd_command(0x6C)  # フォロワー制御
    time.sleep_ms(200)
    lcd_command(0x38)  # ノーマル指令セットへ戻す
    lcd_command(0x0C)  # 表示ON, カーソルOFF
    lcd_command(0x01)  # 画面クリア
    time.sleep_ms(2)

# LCDに文字列を表示する関数
def lcd_print(text):
    for char in text:
        lcd_data(ord(char))

# メイン処理
lcd_init()
lcd_print("Hello, Pico!")
