from backend.db.mysql_connector import get_mysql_connection

conn = get_mysql_connection()
cursor = conn.cursor()

cursor.execute("INSERT INTO users (username, email, favorite_league) VALUES (%s, %s, %s)", 
               ("acebvibes", "ace@example.com", "NBA"))

conn.commit()
cursor.close()
conn.close()

print("MySQL seeded successfully.")
