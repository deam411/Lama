import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def scrape_page(url):
    """
    Esegue lo scraping di una singola pagina web per estrarre il testo
    e tutti i link unici e assoluti.

    Args:
        url (str): L'URL della pagina da analizzare.

    Returns:
        tuple: Una tupla contenente (testo_pagina, set_di_link).
               Restituisce (None, set()) se lo scraping fallisce.
    """
    print(f"Analizzando: {url}")
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        # Solleva un'eccezione per status code di errore (4xx o 5xx)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Errore durante il download di {url}: {e}")
        return None, set()

    soup = BeautifulSoup(response.text, 'html.parser')

    # Estrae tutto il testo dalla pagina, pulendolo dagli spazi eccessivi
    page_text = "\n".join(soup.stripped_strings)

    # Estrae tutti i link e li converte in URL assoluti
    links = set()
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        # Crea un URL assoluto partendo da uno relativo (es. /pagina.html)
        absolute_link = urljoin(url, href)
        
        # Semplice validazione per assicurarci che sia un URL http/https
        parsed_link = urlparse(absolute_link)
        if parsed_link.scheme in ['http', 'https']:
            links.add(absolute_link)
            
    return page_text, links

if __name__ == "__main__":
    # Usiamo una pagina di notizie come primo test
    start_url = "https://www.ansa.it/" 

    text, found_links = scrape_page(start_url)

    if text:
        print("\n" + "="*80)
        print(f"ESTRATTO TESTO DALLA PAGINA (primi 1000 caratteri):")
        print("="*80)
        print(text[:1000] + "...")
        
        print("\n" + "="*80)
        print(f"TROVATI {len(found_links)} LINK UNICI (primi 10):")
        print("="*80)
        
        # Stampa solo i primi 10 link per brevità
        for i, link in enumerate(list(found_links)[:10]):
            print(f"{i+1}: {link}")
        if len(found_links) > 10:
            print("...")
