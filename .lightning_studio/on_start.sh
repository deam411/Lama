#!/bin/bash

# Interrompe lo script se un comando fallisce
set -e

echo "--- Inizio script di avvio automatico ---"

# Imposta la directory dei modelli Ollama all'interno del progetto per renderli persistenti.
export OLLAMA_MODELS=./ollama_models
mkdir -p $OLLAMA_MODELS
echo "Directory dei modelli Ollama impostata su: $(pwd)/ollama_models"

# 1. Installa le dipendenze Python da requirements.txt
echo "[1/4] Installazione delle dipendenze Python..."
pip3 install -r requirements.txt
echo "Dipendenze Python installate."

# 2. Controlla e installa Ollama se non è presente
if ! command -v ollama &> /dev/null
then
    echo "[2/4] Ollama non trovato. Installazione in corso..."
    curl -fsSL https://ollama.com/install.sh | sh
    echo "Installazione di Ollama completata."
else
    echo "[2/4] Ollama è già installato."
fi

# 3. Assicura che il servizio Ollama sia attivo
echo "[3/4] Verifica del servizio Ollama..."
if ! pgrep -x "ollama" > /dev/null
then
    echo "Servizio Ollama non attivo. Tentativo di avvio manuale..."
    ollama serve &
    sleep 5
else
    echo "Servizio Ollama già attivo."
fi


# 4. Controlla e scarica il modello 'llama3' (8B) se non è presente
if ollama list | grep -q "llama3:latest"
then
    echo "[4/4] Il modello 'llama3' è già presente."
else
    echo "[4/4] Modello 'llama3' non trovato. Download in corso (~4.7GB)..."
    ollama pull llama3
    echo "Download del modello completato."
fi

echo "--- Ambiente pronto! ---"