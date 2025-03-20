from machine import I2C, Pin
import time

# I2Cの設定 (I2C0: SDA=GP4, SCL=GP5)
i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=400000)

# LCDのI2Cアドレス
LCD_ADDR = 0x3E

# コマンド送信関数
def lcd_command(cmd):
    i2c.writeto(LCD_ADDR, bytearray([0x00, cmd]))
    time.sleep_ms(1)

# データ送信関数
def lcd_data(data):
    i2c.writeto(LCD_ADDR, bytearray([0x40, data]))
    time.sleep_ms(1)

# LCD初期化関数
def lcd_init():
    time.sleep_ms(50)  # 電源ON後の待機
    lcd_command(0x38)  # 8bitモード
    lcd_command(0x39)  # 拡張コマンドモード
    lcd_command(0x14)  # 内部OSC設定
    lcd_command(0x70)  # コントラスト設定（調整可）
    lcd_command(0x56)  # 電源電圧調整
    lcd_command(0x6C)  # フォロワー制御
    time.sleep_ms(200)
    lcd_command(0x38)  # 通常動作モード
    lcd_command(0x0C)  # 表示ON, カーソルOFF
    lcd_command(0x01)  # 画面クリア
    time.sleep_ms(2)

# 文字列を表示する関数
def lcd_print(message):
    for char in message:
        lcd_data(ord(char))

# LCDの初期化 & 文字表示
lcd_init()
lcd_print("Hello!")
