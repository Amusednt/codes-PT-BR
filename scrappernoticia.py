import requests
from bs4 import BeautifulSoup

def extrair_noticias_hacker_news():
    """
    Faz o scraping da primeira página do Hacker News para obter
    os títulos das notícias e seus respectivos links.
    """
    url = "https://news.ycombinator.com/"
    
    try:
        # Envia uma requisição GET para o site
        resposta = requests.get(url)
        # Transforma o HTML bruto em um objeto BeautifulSoup navegável
        soup = BeautifulSoup(resposta.text, 'html.parser')

        # No Hacker News, os links das notícias ficam em elementos <span> com a classe 'titleline'
        noticias = soup.find_all('span', class_='titleline')

        print(f"--- Top Notícias do Hacker News ({len(noticias)} encontradas) ---")
        
        for i, item in enumerate(noticias, 1):
            # O link real está dentro da tag <a> dentro do span
            link_tag = item.find('a')
            titulo = link_tag.text
            link = link_tag['href']
            
            print(f"{i}. {titulo}")
            print(f"   Link: {link}\n")

    except Exception as e:
        print(f"Ocorreu um erro ao acessar o site: {e}")

# Execução do script
if __name__ == "__main__":
    extrair_noticias_hacker_news()
