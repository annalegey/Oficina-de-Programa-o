import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

st.title("Consulta de Preços de Livros")

genero = st.selectbox("Selecione o gênero de livro que você deseja:", 
                      options=["Animais de estimação", "Antiguidades & Colecionáveis","Apoio aos estudos","Arquitetura","Arte","Artes Perfomáticas",
                               "Artesanato & Estilo de vida","Autoajuda", "Biografia & autobiografia", "Bíblias","Casa&Lar","Ciências","Ciência Política",
                               "Ciências Sociais", "Coleções Literárias", "Computação & Informática", "Corpo, Mente & Espírito", "Crimes", "Crítica Literária"
                               "Culinária & Gastronomia", "Design", "Direito", "Educação", "Engenharia & Tecnologia", "Esporte & Lazer"
                               "Estudo De Línguas Estrangeiras", "Família & Relacionamentos", "Ficção", "Ficção Infantil", "Ficção Juvenil", "Filosofia",
                               "Fotografia", "História","Humor","Jardinagem","Jogos & Atividades", "Língua, Comunicação & Disciplinas Relacionadas",
                               "Livros Música","Matemática", "Medicina", "Natureza", "Negócios & Economia", "Não Ficção Infantil", "Não Ficção Juvenil", "Poesia",
                               "Psicologia", "Quadrinhos, Mangás & Graphic Novels", "Referência", "Religião", "Saúde & Boa Forma", "Teatro", "Transportes", "Viagem"])
                              
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
        st.title('Faixa de preços')
        st.line_chart(df['Preço do livro'])
    else:
        st.write("Nenhum livro encontrado")
