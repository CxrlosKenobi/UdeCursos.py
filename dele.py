import management as mt 
import sqlite3 

conn = sqlite3.connect('data.db')
cur = conn.cursor()

code = '510140-8'
name = 'Física I[8]'
credits = 1
teacher = 'false'
workday = 'X-V'
schedule = '2-3_4'

# cur.execute('''
#     INSERT INTO data (code, name, credits, teacher, workday, schedule) 
#     VALUES (?,?,?,?,?,?)''', code, name, credits, teacher, workday, schedule)

cur.execute('''INSERT INTO data (code, name, credits, teacher, workday, schedule) VALUES ('510140-8', 'Física I[8]', 1, 'false', 'X-V','2-3_4')''')
conn.commit()
cur.close()
