#!/bin/bash

# Interrompe lo script se un comando fallisce
set -e

echo "--- Inizio script di avvio automatico ---"

# 1. Installa le dipendenze Python da requirements.txt
echo "[1/3] Installazione delle dipendenze Python..."
pip3 install -r requirements.txt
echo "Dipendenze Python installate."

# 2. Controlla e installa Ollama se non è presente
if ! command -v ollama &> /dev/null
then
    echo "[2/3] Ollama non trovato. Installazione in corso..."
    curl -fsSL https://ollama.com/install.sh | sh
    echo "Installazione di Ollama completata."
else
    echo "[2/3] Ollama è già installato."
fi

# L'installer di Ollama ora usa systemd per avviare il server automaticamente,
# quindi non abbiamo più bisogno di 'ollama serve &' qui.

# 3. Controlla e scarica il modello llama3:70b se non è presente
# Usiamo 'ollama list' e 'grep' per vedere se il modello esiste già.
if ollama list | grep -q "llama3:70b"
then
    echo "[3/3] Il modello llama3:70b è già presente."
else
    echo "[3/3] Modello llama3:70b non trovato. Download in corso (~40GB)..."
    ollama pull llama3:70b
    echo "Download del modello completato."
fi

echo "--- Ambiente pronto! ---"