import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

def home():

    st.title("Projeto Pokemon")
    st.write("Este é um projeto meu, dudu do bigode, que tem como objetivo mostrar algumas informações de extrema relevancia sobre pokemons através de gráficos. Você pode acessar esses gráficos atravez da barra de navegação ao lado.")


def carregar_dados():

    data = pd.read_csv("PokemonData.csv")
    return data

def grafico_linhas():

    st.title("Grafico de linhas")

    data = carregar_dados()

    fig = plt.figure(figsize=(10,10))

    data.groupby("Generation")["HP"].mean().plot(marker="o")

    plt.title("Tendencia de hp dos pokemons ao longo das gerações")
    plt.xlabel("Geração")
    plt.ylabel("Média de hp")
    plt.grid()
    st.pyplot(fig)

    with st.expander("codigo para gerar o grafico"):
        with st.echo():
                data = carregar_dados()
                fig = plt.figure(figsize=(10,10))
                data.groupby("Generation")["HP"].mean().plot(marker="o")
                plt.title("Tendencia de hp dos pokemons ao longo das gerações")
                plt.xlabel("Geração")
                plt.ylabel("Média de hp")
                plt.grid()
            

def grafico_barras():

    st.title("Gráfico de barras")
    
    data=carregar_dados()

    fig=plt.figure(figsize=(10,8))

    type_counts = pd.concat([data["Type1"],data["Type2"]]).value_counts()
    type_counts.plot(kind="bar")
    
    plt.title("Distribuição de pokemons por tipo")
    plt.xlabel("Tipo")
    plt.ylabel("Quantidade de pokemons")
    plt.grid(axis="y")
    plt.xticks(rotation=45)
    st.pyplot(fig)

    with st.expander("codigo para gerar o grafico"):
        with st.echo():
                st.title("Gráfico de barras")
                data=carregar_dados()
                fig=plt.figure(figsize=(10,8))
                type_counts = pd.concat([data["Type1"],data["Type2"]]).value_counts()
                type_counts.plot(kind="bar")
                plt.title("Distribuição de pokemons por tipo")
                plt.xlabel("Tipo")
                plt.ylabel("Quantidade de pokemons")
                plt.grid(axis="y")
                plt.xticks(rotation=45)
                st.pyplot(fig)

def main():

    st.sidebar.title("Navegação")
    pages={"Pagina inicial": home, "Tendencia de hp dos pokemons ao longo das gerações(Gráfico de linhas)": grafico_linhas, "Distribuição de pokemons por tipo(Gráfico de Barras": grafico_barras }
    selection = st.sidebar.selectbox("ir para", list(pages.keys()))
    pages[selection]()
    st.sidebar.title("sobre")
    st.sidebar.write("projeto tem como ojeto de estudo os monstrinho de bolso ta ligado")
    


if __name__ == "__main__":
    main()  
