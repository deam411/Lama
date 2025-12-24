### utente inesperto
scrivo pochissimo codice ed è da tanto che non scrivo.

### intelligenza artificiale personale
il problema che vogliamo risolvere è che desideri avere un'AI personale con cui interagire, che ti supporti nelle tue attività quotidiane e che possa essere integrata nei tuoi progetti per aiutarti a programmare. attualmente usi Claude o Gemini 3, ma vuoi eliminare la necessità di affidarti ad altre AI esterne per queste funzioni.

### causando 2 problemi
attualmente, usi troppe AI che non offrono token illimitati e che non puoi personalizzare o usare liberamente come vorresti, limitando la tua flessibilità e aumentando i costi. inoltre, non puoi usarli e cambiarli a tuo piacimento, il che ti toglie il controllo sulla tua esperienza AI.

### assistente AI per la programmazione e la vita quotidiana
il risultato ideale è avere un'AI personale che puoi integrare in un'applicazione in stile antigravity per la programmazione, che ti permetta anche di chattare normalmente e che possa accedere a internet per fornirti informazioni, e soprattutto: **posso usarla e cambiarla a mio piacimento.**

### i vantaggi includono:
potrai programmare più facilmente e velocemente, migliorando la tua produttività e l'efficienza del tuo lavoro.

### capacità richieste:
*   **comprensione e generazione in italiano:** l'AI deve essere in grado di comunicare fluidamente in italiano, sia capendo le tue richieste che generando risposte.
*   **assistenza alla programmazione superiore:** deve poter aiutarti a scrivere codice, capire errori e suggerire miglioramenti, con una qualità e un'efficienza **superiore a quella di modelli come Gemini 3 o Claude 4.5**.
*   **generazione di semplici script python:** l'AI deve essere in grado di scrivere script python di base.
*   **traduzione multilingue:** deve poter tradurre testi da e verso diverse lingue.
*   **riassunto:** capacità di sintetizzare testi lunghi in concetti chiave.
*   **generazione creativa:** deve essere in grado di produrre testi come temi, articoli o contenuti simili.
*   **accesso a internet:** per fornire informazioni aggiornate e ricercare dati online.

### stack tecnologico raccomandato:
*   **Python** – useremo questo linguaggio per tutta la logica principale. è molto versatile e la scelta standard per lo sviluppo AI, inoltre è abbastanza facile da leggere e capire anche per chi è alle prime armi.
*   **LitAI** – questa è una nostra libreria che rende super facile parlare con qualsiasi modello di intelligenza artificiale (come ChatGPT, Claude, ecc.) con poche righe di codice. gestisce tutte le cose complicate come gli errori, le traduzioni e ti permette di scegliere il modello più adatto per la programmazione, anche quelli più performanti. la capacità di essere "migliore" di Gemini o Claude dipenderà molto dal modello specifico che sceglieremo di usare tramite LitAI e da quanto lo personalizzeremo, ma LitAI ci dà la flessibilità per farlo.
*   **requests / BeautifulSoup** – queste sono librerie Python per accedere a internet e "leggere" le pagine web, così la tua AI potrà fare ricerche online.
*   **Lightning Studio** – questo è l'ambiente dove costruiremo e faremo girare la tua AI. immaginalo come un computer potentissimo nel cloud, già configurato con tutto quello che serve, quindi non dovrai installare nulla e tutto sarà salvato automaticamente.

### milestones e piano di lavoro

#### fase 0 - mvp
obiettivo: la priorità assoluta per questa fase è che l'AI possa comunicare efficacemente in italiano, capendo le tue domande e fornendo risposte pertinenti e utili, e che possa **scrivere semplici script python** come richiesto.

### come implementarlo
*   **su una macchina dedicata (cpu):** per ora useremo una macchina dedicata che funziona solo con la CPU. questo significa che la tua AI utilizzerà il "cervello" del computer senza usare la "scheda grafica". Lightning imposterà tutto in modo che questa macchina rimanga accesa 24 ore su 24, 7 giorni su 7, così avrai sempre risposte istantanee e l'AI sarà sempre attiva quando ne avrai bisogno.