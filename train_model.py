import psycopg2
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import joblib

# Détails de la connexion à la base de données
host = "localhost"
database = "reviews_db"
user = "myuser"  # Remplacez par votre nom d'utilisateur PostgreSQL
password = "mypassword"  # Remplacez par votre mot de passe PostgreSQL

# Connexion à la base de données
try:
    print("Tentative de connexion à la base de données...")
    connection = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )
    cursor = connection.cursor()
    print("Connexion réussie à la base de données.")

    # Récupérer les données de la table reviews2
    query = "SELECT review_text, sentiment FROM reviews2;"
    cursor.execute(query)
    rows = cursor.fetchall()

    # Vérification des données récupérées
    print(f"Nombre de lignes récupérées : {len(rows)}")
    if len(rows) == 0:
        print("Aucune donnée récupérée, vérifiez votre table.")

    # Transformer les données en DataFrame
    df = pd.DataFrame(rows, columns=['review_text', 'sentiment'])

    # Vérification du DataFrame
    print(f"Exemple de données récupérées : \n{df.head()}")

    # Préparation des données pour l'entraînement
    X = df['review_text']  # Texte des avis
    y = df['sentiment']  # Sentiment

    # Convertir le texte en vecteurs numériques avec TF-IDF
    vectorizer = TfidfVectorizer(stop_words='english')
    X_vect = vectorizer.fit_transform(X)

    # Diviser les données en ensembles d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(X_vect, y, test_size=0.3, random_state=42)

    # Créer un modèle de classification (Naive Bayes)
    model = MultinomialNB()

    # Entraîner le modèle
    print("Entraînement du modèle...")
    model.fit(X_train, y_train)

    # Prédire sur l'ensemble de test
    y_pred = model.predict(X_test)

    # Calculer la précision du modèle
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Précision du modèle : {accuracy * 100:.2f}%")

    # Sauvegarder le modèle et le vectoriseur pour les utiliser plus tard
    joblib.dump(model, 'sentiment_model.pkl')
    joblib.dump(vectorizer, 'vectorizer.pkl')

    print("Modèle et vectoriseur sauvegardés avec succès.")

except Exception as e:
    print(f"Erreur lors de l'opération : {e}")
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Connexion fermée.")
