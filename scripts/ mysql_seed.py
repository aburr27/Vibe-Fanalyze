# scripts/mysql_seed.py
from app.db.mysql_connector import get_mysql_connection

def seed_mysql():
    conn = get_mysql_connection()
    cursor = conn.cursor()

    # Insert a test user if not exists
    cursor.execute("""
        INSERT INTO users (username, email, favorite_league)
        VALUES ('acebvibes', 'ace@example.com', 'NBA')
        ON DUPLICATE KEY UPDATE email = VALUES(email), favorite_league = VALUES(favorite_league)
    """)

    # Insert a favorite (LeBron James ID = 23 in Mongo)
    cursor.execute("""
        INSERT INTO favorites (user_id, type, reference_id)
        VALUES (1, 'player', 23)
        ON DUPLICATE KEY UPDATE reference_id = VALUES(reference_id)
    """)

    conn.commit()
    cursor.close()
    conn.close()

    print("✅ MySQL seeded with test user and favorite.")


if __name__ == "__main__":
    seed_mysql()

