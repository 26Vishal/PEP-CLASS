import psycopg2
conn = psycopg2.connect(
    host="localhost",
    database= "pep_learn",
    user = "postgres",
    password="9811"
)
print("connection done")
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS employees(
    id INT,
    name VARCHAR(50),
    salary REAL NOT NULL
)
""")
conn.commit()
cur.execute("""SELECT * from employees""")
rows=cur.fetchall()
for i in rows:
    print(row)
    
conn.close()