from collections import deque

import sqlite3
import csv
import time as t
import os
os.system('rm -rf data.db && touch data.db')
conn = sqlite3.connect('data.db')
cur = conn.cursor()
print('\n[ ok ] Now connected to the database!')
t.sleep(1)

cur.execute(
"""
CREATE TABLE data(
    code VARCHAR(8),
    name VARCHAR(40),
    credits INTEGER NOT NULL,
    teacher VARCHAR(40),
    workday VARCHAR(10),
    schedule VARCHAR(10),
    days VARCHAR(10),
    PRIMARY KEY (code),
    UNIQUE (code)
);
"""
)
conn.commit()
cur.close()

print('[ ok ] Db has been sucesfully created!')
