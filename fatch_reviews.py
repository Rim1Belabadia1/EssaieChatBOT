import psycopg2

# Détails de la connexion à la base de données
host = "localhost"
database = "reviews_db"
user = "myuser"  # Remplacez par votre nom d'utilisateur PostgreSQL
password = "mypassword"  # Remplacez par votre mot de passe PostgreSQL

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
    
    # Création de la table reviews2 avec les mêmes colonnes que reviews
    create_table_query = """
    CREATE TABLE IF NOT EXISTS reviews2 (
        id SERIAL PRIMARY KEY,
        product_name VARCHAR(255) NOT NULL,
        review_text VARCHAR(255),
        rating VARCHAR(255) NOT NULL,
        text TEXT NOT NULL,
        sentiment VARCHAR(10)
    );
    """
    
    # Exécution de la requête de création de table
    cursor.execute(create_table_query)
    connection.commit()
    print("Table reviews2 créée avec succès.")
    
    # Insertion des données dans la table reviews2
    insert_query = """
    INSERT INTO reviews2 (product_name, review_text, rating, text, sentiment)
    VALUES
    ('Produit A', 'Super produit', '5', 'Test', 'positif'),
    ('Produit B', 'Bon rapport qualité/prix', '4', 'Test', 'positif'),
    ('Produit C', 'Moyenne qualité', '3', 'Test', 'neutre'),
    ('Produit D', 'Produit de mauvaise qualité', '2', 'Test', 'négatif'),
    ('Produit E', 'Ne répond pas à mes attentes', '1', 'Test', 'négatif');
    """
    
    # Exécution de la requête d'insertion
    cursor.execute(insert_query)
    connection.commit()
    print("Données insérées avec succès dans reviews2.")
    
    # Affichage des données de la table reviews2
    select_query = "SELECT * FROM reviews2;"
    cursor.execute(select_query)
    rows = cursor.fetchall()
    
    print("\nDonnées récupérées de la table 'reviews2' :")
    for row in rows:
        print(row)

except Exception as e:
    print(f"Erreur lors de l'opération : {e}")

finally:
    # Fermeture de la connexion
    if connection:
        cursor.close()
        connection.close()
        print("Connexion fermée.")
