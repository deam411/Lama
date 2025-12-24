# main.py
import litellm

class Lama:
    """
    Un'AI personale per la programmazione e le attività quotidiane.
    """
    def __init__(self, model="ollama/llama3"):
        """
        Inizializza l'AI personale con un modello locale tramite Ollama.

        Args:
            model (str): Il nome del modello di linguaggio da utilizzare.
        """
        self.model = model
        print(f"Lama inizializzata con il modello locale: {self.model}")
        print("Assicurati che il server Ollama sia in esecuzione in background.")

    def chat(self, user_input):
        """
        Avvia una conversazione con l'AI.

        Args:
            user_input (str): L'input dell'utente.

        Returns:
            str: La risposta dell'AI.
        """
        messages = [{"role": "user", "content": user_input}]
        
        try:
            # Chiamata a Litellm per ottenere la risposta del modello locale
            response = litellm.completion(
                model=self.model, 
                messages=messages
            )
            
            ai_response = response.choices[0].message.content
            return ai_response
        except Exception as e:
            return f"Si è verificato un errore. Assicurati che Ollama sia in esecuzione. Dettagli: {e}"

if __name__ == "__main__":
    lama_ai = Lama()
    
    # Inizia una semplice chat a riga di comando
    print("\nLama è pronta. Scrivi 'esci' per terminare la chat.")
    print("-