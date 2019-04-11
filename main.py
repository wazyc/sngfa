#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import datetime
import time
import csv

PIN_IN = 17
PIN_OUT = 25
machine_name = 'test01'
csvfile_path='/home/pi/dev/test.csv'

# CSVファイルの新規作成
# 既存ファイｒは上書きされる。
def make_new_csv():
    with open(csvfile_path, 'w') as new_csv_file:
        fieldnames = ['time', 'state', 'machine']
        writer = csv.DictWriter(new_csv_file, fieldnames=fieldnames)
        writer.writeheader()
        time.sleep(0.5)
        return 0


# CSVファイルにデータを追記する。
# また、2秒間ランプを消灯、処理を停止する。
def csv_output(now_state):
    GPIO.output(PIN_OUT, GPIO.LOW)
    datnow = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    with open(csvfile_path, 'a') as f:
        writer = csv.writer(f)
        writer.writerow([str(datnow), str(now_state), machine_name])
    print(str(datnow) + ' ' + str(now_state) + ' ' + machine_name)
    time.sleep(2)
    GPIO.output(PIN_OUT, GPIO.HIGH)
    return 0


# メイン処理
print('start')
try:
    # GPIO準備
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_IN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(PIN_OUT, GPIO.OUT)

    # CSV新規作成
    make_new_csv()
    # 初期値
    old_state = 2

    while True:
        if GPIO.input(PIN_IN) == GPIO.HIGH:
            new_state = 1
        else:
            new_state = 0

        if old_state != new_state:
            csv_output(new_state)
            old_state = new_state

        time.sleep(0.1)
except KeyboardInterrupt:
    pass

GPIO.output(PIN_OUT, GPIO.LOW)
GPIO.cleanup()
print('\nend')
