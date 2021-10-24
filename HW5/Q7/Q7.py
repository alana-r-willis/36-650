import psycopg2
conn = psycopg2.connect(host="localhost", 
                        port="5432", 
                        user="postgres", 
                        password="please175", 
                        database="postgres"
                       )
print("Database opened successfully")
cur = conn.cursor()
dummy= '''insert into employee(id,fname,lname) VALUES
(generate_series(1,500), 
substr(MD5(random()::text), 0, 10), 
substr(MD5(random()::text), 0,10))
'''
cur.execute(dummy)
print("Table successfully created")
conn.commit()
conn.close()