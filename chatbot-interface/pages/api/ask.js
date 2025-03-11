import axios from 'axios';

export default async function handler(req, res) {
  if (req.method === 'POST') {
    try {
      const { question } = req.body;
      
      // Appel au backend FastAPI pour obtenir la réponse à la question
      const response = await axios.post('http://localhost:5000/ask', 
        { question },
        { headers: { 'Content-Type': 'application/json' } }
      );
      
      // Envoi de la réponse obtenue à l'interface frontend
      res.status(200).json({ answer: response.data.answer });
    } catch (error) {
      console.error("Erreur lors de l'appel du backend:", error);
      res.status(500).json({ error: "Erreur lors de l'appel au backend" });
    }
  } else {
    // Si la méthode n'est pas POST, renvoyer une erreur
    res.status(405).json({ error: 'Méthode non autorisée' });
  }
}
