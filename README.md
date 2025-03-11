# EssaieChatBOT
Ceci est un repo, d'un model entrainé avec une base de données SQLpostgre avec backend python et un frontend Nextjs
![image](https://github.com/user-attachments/assets/156d7c37-a377-40a2-9f2c-2cd5cfa196ae)
Voici un modèle de `README.md` pour votre projet de chatbot basé sur les avis de produits, intégré avec FastAPI et un frontend React :
# Product Review Chatbot

Ce projet est un chatbot conçu pour répondre à des questions concernant les avis de produits. Il permet aux utilisateurs de poser des questions sur des avis, de filtrer les avis en fonction de leur sentiment (positif ou négatif), et d'obtenir des réponses sur divers produits en fonction des avis de consommateurs. Le chatbot est intégré avec un backend FastAPI qui interroge une base de données PostgreSQL contenant des avis et un frontend React permettant une interaction simple et intuitive avec l'utilisateur.

## Fonctionnalités

- **Ajouter des avis** : Les utilisateurs peuvent ajouter des avis sur différents produits.
- **Poser des questions** : Le chatbot répond à des questions simples comme "Bonjour", "Qui êtes-vous ?", et à des questions sur les produits comme "Quels avis sont positifs ?".
- **Filtrage des avis** : Les utilisateurs peuvent filtrer les avis en fonction du sentiment (positif ou négatif).
- **Base de données PostgreSQL** : Utilisation d'une base de données pour stocker les avis des utilisateurs.
- **Frontend React** : Interface utilisateur moderne et responsive pour poser des questions et afficher les réponses.

## Installation

### Prérequis

- [Node.js](https://nodejs.org/) pour le frontend React
- [Python 3.x](https://www.python.org/) et [FastAPI](https://fastapi.tiangolo.com/) pour le backend
- [PostgreSQL](https://www.postgresql.org/) pour la base de données

### Backend (FastAPI)

1. Clonez ce repository :

   ```bash
   git clone https://github.com/votre-utilisateur/EssaieChatBOT.git
   cd EssaieChatBOT
   ```

2. Créez un environnement virtuel et installez les dépendances :

   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur Windows : venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Configurez la base de données PostgreSQL :

   - Créez une base de données PostgreSQL nommée `reviews_db`.
   - Modifiez l'URL de connexion dans `EssaieChatBOT/main.py` avec vos informations de connexion PostgreSQL.

4. Lancez l'application backend :

   ```bash
   uvicorn main:app --reload
   ```

   Le backend sera accessible à `http://localhost:8000`.

### Frontend (React)

1. Allez dans le répertoire du frontend :

   ```bash
   cd ../chatbot-interface
   ```

2. Installez les dépendances :

   ```bash
   npm install
   ```

3. Lancez le serveur de développement :

   ```bash
   npm start
   ```

   Le frontend sera accessible à `http://localhost:3000`.

## Usage

1. Ouvrez votre navigateur et allez à `http://localhost:3000` pour interagir avec le chatbot.
2. Vous pouvez poser des questions comme :
   - "Qui êtes-vous ?"
   - "Quels avis sont positifs ?"
   - "Quel est le sentiment des avis ?"
3. Le chatbot répondra en fonction des avis présents dans la base de données PostgreSQL.

## Technologies utilisées

- **Backend** :
  - FastAPI
  - SQLAlchemy (pour interagir avec PostgreSQL)
  - PostgreSQL
- **Frontend** :
  - React
  - Axios (pour communiquer avec le backend)
  - CSS (pour le design)
- **Autres** :
  - NLTK pour le traitement du langage naturel

## Contribuer

Si vous souhaitez contribuer à ce projet, voici comment faire :

1. Fork ce repository.
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/nom-de-fonctionnalité`).
3. Faites vos modifications et commitez-les (`git commit -am 'Ajout de fonctionnalité'`).
4. Poussez votre branche (`git push origin feature/nom-de-fonctionnalité`).
5. Ouvrez une pull request.

## Auteurs

- **Rim Belabadia**


