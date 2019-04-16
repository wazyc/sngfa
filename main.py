#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf import settings
import django
import RPi.GPIO as GPIO
import datetime
import time
import csv

# from statsmodels.genmod.families.links import sqrt


settings.configure(
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': './db.sqlite3',
        }
    },
    INSTALLED_APPS=['kadoumap.apps.KadoumapConfig']
)
django.setup()


PIN_IN = 17
PIN_OUT = 25
machine_name = 'test01'
csvfile_path = '/home/pi/dev/operationdata.csv'


# CSVファイルをリネームし、新規作成　◆TODO リネーム部分未作成
def make_new_csv():
    with open(csvfile_path, 'w') as new_csv_file:
        fieldnames = ['time', 'state', 'machine']
        writer = csv.DictWriter(new_csv_file, fieldnames=fieldnames)
        writer.writeheader()
        time.sleep(0.5)
        return 0


# CSVファイルにデータを追記する。
def csv_output(new_state, datnow):
    with open(csvfile_path, 'a') as f:
        writer = csv.writer(f)
        writer.writerow([str(datnow), str(new_state), machine_name])
    print(str(datnow) + ' ' + str(new_state) + ' ' + machine_name)
    return 0


# SQLiteにデータをINSERTする。
def sqlite_insert(new_state, datnow):
    d = OpeData(ope_datetime=str(datnow), ope_state=str(new_state), ope_machine=machine_name)
    d.save()
    return 0


# メイン処理
print('start')
try:
    # GPIO準備
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_IN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(PIN_OUT, GPIO.OUT)

    # CSVリネームし、新規作成
    # make_new_csv()
    # 初期値
    old_state = 2

    while True:
        # ステータス取得
        if GPIO.input(PIN_IN) == GPIO.HIGH:
            new_state = 1
        else:
            new_state = 0

        # ステータスに変化があるか比較
        if old_state != new_state:
            # ランプ消灯（処理受付停止サイン）
            GPIO.output(PIN_OUT, GPIO.LOW)

            datnow = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
            # CSVに出力
            csv_output(new_state, datnow)
            # SQLiteにINSERT
            sqlite_insert(new_state, datnow)

            # 新しいステータスを次回比較用に退避
            old_state = new_state

            # チャタリング対策に処理を停止。
            time.sleep(2)
            # ランプ点灯
            GPIO.output(PIN_OUT, GPIO.HIGH)

        # ステータス取得間隔
        time.sleep(0.1)
except KeyboardInterrupt:
    pass

GPIO.output(PIN_OUT, GPIO.LOW)
GPIO.cleanup()
print('\nend')
