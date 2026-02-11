import psycopg2
conn = psycopg2.connect(
    host="localhost",
    database= "pep_learn",
    user = "postgres",
    password="9811"
)