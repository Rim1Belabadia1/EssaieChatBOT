import joblib
import psycopg2
import pandas as pd

# Charger le modèle et le vectoriseur
model = joblib.load('sentiment_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# Détails de la connexion à la base de données
host = "localhost"
database = "reviews_db"
user = "myuser"  # Remplacez par votre nom d'utilisateur PostgreSQL
password = "mypassword"  # Remplacez par votre mot de passe PostgreSQL

def ask_question(question):
    # Convertir la question en vecteur
    question_vect = vectorizer.transform([question])

    # Prédire le sentiment
    sentiment = model.predict(question_vect)
    
    return sentiment[0]

# Connexion à la base de données
try:
    connection = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )
    cursor = connection.cursor()
    print("Connexion réussie à la base de données.")

    # Exemple de question
    question = input("Posez une question sur les critiques des produits: ")

    # Poser la question au modèle
    sentiment = ask_question(question)
    print(f"Réponse du modèle : {sentiment}")

except Exception as e:
    print(f"Erreur lors de l'opération : {e}")
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Connexion fermée.")
