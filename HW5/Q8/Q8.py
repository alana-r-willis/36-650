import psycopg2
conn = psycopg2.connect(host="localhost", 
                        port="5432", 
                        user="postgres", 
                        password="please175", 
                        database="postgres"
                       )
print("Database opened successfully")
cur = conn.cursor()
lines= ''' SELECT * FROM EMPLOYEE LIMIT 10'''
cur.execute(lines)
print("Lines Printed")
conn.commit()
conn.close()