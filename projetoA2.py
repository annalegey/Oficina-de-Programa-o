import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

st.title("Consulta de Preços de Livros")

genero = st.text_input("Selecione o gênero de livro que você deseja:")
genero = genero.replace(' ', '-')

if st.button("Consultar"):
    url = 'https://leitura.com.br/livros/' + genero
    site = requests.get(url)
    soup = BeautifulSoup(site.content, 'html.parser')

    lista = []
    b = soup.find('div', {'id': 'content'})
    livros = b.find_all('div', {'class': 'product-layout'})
    for links in livros:
        links_p = links.find('div', 'image')
        link_livro = links_p.find('a')['href']
        conteudo_site = links.find_all('div', {'class': 'caption'})
        for nome in conteudo_site:
            nome_livro = nome.find('h4').text
            precos = nome.find_all('p', {'class': 'price'})
            for preco in precos:
                preco_new = preco.find('span', {'class': 'price-new'})
                if preco_new:
                    preco_new = preco.find('span', {'class': 'price-new'}).text
                else:
                    preco_new = preco.text.strip()

                dados = {'Livro': nome_livro, 'Preço do livro': preco_new, 'Link para compra': link_livro}
                lista.append(dados)
    if lista:
        df = pd.DataFrame(lista).sort_values(by='Preço do livro', ascending=True)
        st.write(df)
        df.set_index('Livro', inplace=True)
        st.line_chart(df['Preço do livro'])
    else:
        st.write("Nenhum livro encontrado")
