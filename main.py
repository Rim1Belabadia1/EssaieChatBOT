from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from fastapi.middleware.cors import CORSMiddleware
import nltk
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Télécharger les ressources NLTK
nltk.download('punkt')

# Configuration PostgreSQL
DATABASE_URL = "postgresql://myuser:mypassword@localhost/reviews_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Modèle SQLAlchemy pour la table "reviews"
class Review(Base):
    __tablename__ = "reviews2"  # Assurez-vous que la table est 'reviews2' dans votre BDD

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)
    sentiment = Column(String(10), nullable=False)

# Créer les tables dans la BDD
Base.metadata.create_all(bind=engine)

# FastAPI application
app = FastAPI()

# Configuration CORS pour autoriser le frontend à accéder au backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Autoriser toutes les origines, ou spécifier ["http://localhost:3000"] pour Next.js
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dépendance de session pour interagir avec la BDD
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Route pour ajouter un avis
@app.post("/reviews/")
def add_review(text: str, sentiment: str, db: Session = Depends(get_db)):
    if sentiment not in ["positif", "négatif"]:
        raise HTTPException(status_code=400, detail="Sentiment invalide")
    
    new_review = Review(text=text, sentiment=sentiment)
    db.add(new_review)
    db.commit()
    db.refresh(new_review)
    return new_review

# Route pour récupérer tous les avis
@app.get("/reviews/")
def get_reviews(db: Session = Depends(get_db)):
    reviews = db.query(Review).all()
    return reviews

# Route pour poser une question au modèle
class QuestionRequest(BaseModel):
    question: str
@app.post("/ask")
def ask_question(request: QuestionRequest, db: Session = Depends(get_db)):
    question = request.question  # Accédez à la question envoyée
    reviews = db.query(Review).all()

    relevant_reviews = [review for review in reviews if question.lower() in review.text.lower()]
    
    if not relevant_reviews:
        return {"answer": "Désolé, je n'ai trouvé aucun avis pertinent."}
    
    answer = "Voici quelques avis pertinents :\n" + "\n".join([review.text for review in relevant_reviews])
    return {"answer": answer}