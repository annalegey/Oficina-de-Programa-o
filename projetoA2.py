import requests
from bs4 import BeautifulSoup
import pandas as pd

genêro = st.text_input("Selecione o genêro de livro que você deseja:").replace(' ','-')
url = 'https://leitura.com.br/livros/' + genêro
site = requests.get('https://leitura.com.br/livros/' + genêro)
soup = BeautifulSoup(site.content, 'html.parser')

import requests
from bs4 import BeautifulSoup

lista = []
b = soup.find('div', {'id': 'content'})
livros = b.find_all('div', {'class': 'product-layout'})
for links in livros:
    links_p = links.find('div', 'image')
    link_livro = links_p.find('a')['href']
    conteúdo_site = links.find_all('div', {'class': 'caption'})
    for nome in conteúdo_site:
        nome_livro = nome.find('h4').text
        preços = nome.find_all('p', {'class': 'price'})
        for preço in preços:
            preços_new = preço.find('span', {'class': 'price-new'})
            if preços_new:
               preços_new = preço.find('span', {'class': 'price-new'}).text
            else:
                preços_new = preço.text.strip()

            dados = {'Livro': nome_livro, 'Preço do livro': preços_new, 'Link para compra' : link_livro}
            lista.append(dados)

df = pd.DataFrame(lista).sort_values(by='Preço do livro', ascending=True)
df
