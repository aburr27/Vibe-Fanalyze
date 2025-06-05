from backend.db.mysql_connector import get_mysql_connection

conn = get_mysql_connection()
cursor = conn.cursor()

# Insert users
cursor.execute("""
INSERT INTO users (username, email, favorite_league)
VALUES ('acebvibes', 'ace@example.com', 'NBA')
""")

# Insert favorites (example: LeBron’s ID from Mongo = 23)
cursor.execute("""
INSERT INTO favorites (user_id, type, reference_id)
VALUES (1, 'player', 23)
""")

conn.commit()
cursor.close()
conn.close()

print("✅ MySQL seeded with test user and favorite.")
