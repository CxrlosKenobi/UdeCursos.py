from collections import deque

import sqlite3
import csv
import time as t

conn = sqlite3.connect('data.db')
cur = conn.cursor()
print('\n[ ok ] Now connected to the database!')
t.sleep(1)

cur.execute(
"""
CREATE TABLE data (
    code VARCHAR(8),
    name VARCHAR(40),
    credits INTEGER NOT NULL,
    teacher VARCHAR(40),
    career VARCHAR(40),
    schedule VARCHAR(40),
    PRIMARY KEY (code),
    UNIQUE (code)
);
"""
)
conn.commit()
cur.close()

print('[ ok ] Succesfully db created!')
