import psycopg2

try:
    conn = psycopg2.connect(
        dbname="reviews_db",
        user="myuser",
        password="mypassword",
        host="localhost",
        port="5432"
    )
    print("✅ Connexion réussie à PostgreSQL !")
    conn.close()
except Exception as e:
    print("❌ Erreur de connexion :", e)
