from machine import I2C, Pin
import time

# I2C初期化
i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=100000)  # I2C1 (GP6, GP7)
LCD_ADDR = 0x3E  # LCDのI2Cアドレス

# LCDにコマンドを送る関数
def lcd_command(cmd):
    i2c.writeto(LCD_ADDR, bytearray([0x00, cmd]))
    time.sleep(0.05)  # 少し待つ

# LCDにデータを送る関数（文字を表示）
def lcd_data(data):
    i2c.writeto(LCD_ADDR, bytearray([0x40, data]))
    time.sleep(0.05)

# LCDの初期化シーケンス
def lcd_init():
    lcd_command(0x38)  # 8ビットモード
    lcd_command(0x39)  # 拡張コマンドセット
    lcd_command(0x14)  # 内部オシレータ周波数設定
    lcd_command(0x70)  # コントラスト設定（試しに0x78や0x7Fも）
    lcd_command(0x56)  # 電源制御（試しに0x6Cも）
    lcd_command(0x6C)  # 電圧フォロワー（試しに0x56も）
    time.sleep(0.2)
    lcd_command(0x38)  # 通常モードへ戻す
    lcd_command(0x0C)  # 表示ON, カーソルOFF
    lcd_command(0x01)  # 画面クリア
    time.sleep(0.2)

# LCDに文字を表示
def lcd_print(text):
    for char in text:
        lcd_data(ord(char))

# LCD初期化 & "HELLO" を表示
lcd_init()

# 最初の行に "HELLO" を表示
lcd_print("Hello")

# 2行目に移動
lcd_command(0xC0)  # 2行目の先頭に移動

# 2行目に "WORLD" を表示
lcd_print("Pico")
