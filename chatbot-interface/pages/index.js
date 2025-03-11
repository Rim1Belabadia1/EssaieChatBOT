import { useState } from 'react';
import axios from 'axios';

export default function Home() {
  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState('');

  // Fonction pour poser la question
  const handleAskQuestion = async () => {
    // Gérer les questions simples de manière pré-définie
    const simpleAnswers = {
      "hello": "Bonjour ! Comment puis-je vous aider ?",
      "hi": "Salut ! Comment puis-je vous assister ?",
      "cv ? ": "Je vais bien, merci de demander ! Et vous ?",
      "how are you ?": "Je vais bien, merci de demander ! Et vous ?",
      "who are you ?": "Je suis un chatbot conçu pour vous aider à trouver des informations et des réponses pertinentes concernant les avis de produits. Mon rôle est de faciliter votre expérience en ligne en répondant à vos questions sur les produits, en vous fournissant des résumés d'avis, en filtrant les avis positifs ou négatifs, et même en vous aidant à analyser des avis de manière plus détaillée.",
    };

    // Vérifier si la question fait partie des réponses simples
    const lowerCaseQuestion = question.trim().toLowerCase();
    if (simpleAnswers[lowerCaseQuestion]) {
      setAnswer(simpleAnswers[lowerCaseQuestion]);
      return;  // Arrêter la fonction ici si la question est simple
    }

    try {
      const response = await axios.post('/api/ask', { question });
      setAnswer(response.data.answer);  // Affichage de la réponse
    } catch (error) {
      console.error("Erreur lors de l'appel au backend:", error);
      setAnswer("Désolé, une erreur est survenue.");
    }
  };

  return (
    <>
      {/* Styles CSS en ligne */}
      <style>
        {`
          * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
          }

          body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f4f7fa;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
          }

          .container {
            background-color: #ffffff;
            border-radius: 15px;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
            padding: 30px;
            width: 100%;
            max-width: 500px;
            text-align: center;
          }

          h1 {
            font-size: 2.5rem;
            color: #4A90E2;
            margin-bottom: 1.5rem;
            font-weight: 700;
          }

          .input-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-bottom: 2rem;
          }

          input[type="text"] {
            width: 80%;
            padding: 0.9rem;
            margin-bottom: 1rem;
            border: 2px solid #ddd;
            border-radius: 8px;
            font-size: 1rem;
            color: #333;
            background-color: #f9f9f9;
            transition: border-color 0.3s ease;
          }

          input[type="text"]:focus {
            outline: none;
            border-color: #4A90E2;
          }

          button {
            background-color: #4A90E2;
            color: white;
            padding: 1rem 3rem;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 1.1rem;
            transition: background-color 0.3s ease;
            width: 80%;
            margin-top: 1rem;
          }

          button:hover {
            background-color: #357ab7;
          }

          p {
            background-color: #e6f7ff;
            padding: 1.2rem;
            border-radius: 8px;
            margin-top: 1.5rem;
            text-align: left;
            color: #333;
            font-size: 1.1rem;
            font-weight: 500;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
          }

          .response {
            white-space: pre-wrap;
          }
        `}
      </style>

      <div className="container">
        <h1>Chatbot</h1>
        <div className="input-container">
          <input
            type="text"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            placeholder="Posez une question"
          />
          <button onClick={handleAskQuestion}>Poser la question</button>
        </div>

        {answer && <p className="response"><strong>Réponse:</strong> {answer}</p>}
      </div>
    </>
  );
}
