# -*- coding:utf-8 -*-

import pymysql
from apscheduler.schedulers.blocking import BlockingScheduler

def job():
    conn = pymysql.Connect(
        host='49.4.21.123',
        port=3306,
        user='root',
        passwd='Admin123;',
        db='allinone',
        charset='utf8'
    )

    conn_one = pymysql.Connect(
        host='49.4.21.123',
        port=3306,
        user='root',
        passwd='Admin123;',
        db='allinone',
        charset='utf8'
    )

    print('连接成功')
    cur = conn.cursor()
    sql = 'select * from kh_order_master'
    cur.execute(sql)
    all = cur.fetchall()
    for ins in all:
        print(ins)
    conn.close()
    conn_one.close()
    print('连接关闭')

scheduler = BlockingScheduler(daemon=True)
scheduler.add_job(job, "cron", hour=1, minute=10, timezone='Asia/Shanghai')
try:
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()