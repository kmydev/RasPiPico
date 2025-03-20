from machine import I2C, Pin
import time

# I2Cの設定 (I2C0: SDA=GP4, SCL=GP5)
i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=100000)

# LCDのI2Cアドレス
LCD_ADDR = 0x3E

# コマンド送信関数
def lcd_command(cmd):
    i2c.writeto(LCD_ADDR, bytearray([0x00, cmd]))
    time.sleep(0.01)

# データ送信関数
def lcd_data(data):
    i2c.writeto(LCD_ADDR, bytearray([0x40, data]))
    time.sleep(0.01)

# LCD初期化関数
def lcd_init():
    time.sleep(0.5)  # 初期化待ち
    lcd_command(0x38)  # 8bitモード
    time.sleep(0.2)  # 初期化後待ち
    lcd_command(0x39)  # 拡張コマンドモード
    lcd_command(0x14)  # 内部OSC設定
    lcd_command(0x7A)  # コントラスト設定（調整可）
    lcd_command(0x54)  # 電源電圧調整
    lcd_command(0x6C)  # フォロワー制御
    time.sleep(0.2)
    lcd_command(0x38)  # 通常動作モード
    lcd_command(0x0F)  # 表示ON, カーソルOFF
    lcd_command(0x01)  # 画面クリア
    time.sleep(0.2)

# 文字列を表示する関数
def lcd_print(message):
    for char in message:
        lcd_data(ord(char))

# LCDの初期化 & 文字表示
lcd_init()
lcd_print("Hello!")
