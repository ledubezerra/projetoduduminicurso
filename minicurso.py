import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

def home():

    st.title("projeto pokemon")

def carregar_dados():

    data = pd.read_csv("PokemonData.csv")
    return data

def grafico_linhas():

    st.sidebar.title("Grafico de linhas")

    data = carregar_dados()

    fig = plt.figure(figsize=(10,10))

    data.groupby("generation")["hp"].mean().plot(marker="o")

    plt.title("tendencia de hp dos pokemons ao longo das gerações")
    plt.xlabel("geração")
    plt.ylabel("média de hp")
    plt.grid()
    st.pyplot(fig)

    with st.expander("codigo para gerar o grafico"):
        with st.echo():
            data = carregar_dados()
            fig = plt.figure(figsize=(10,10))
            data.groupby("generation")["hp"].mean().plot(marker="o")
            plt.title("tendencia de hp dos pokemons ao longo das gerações")
            plt.xlabel("geração")
            plt.ylabel("média de hp")
            plt.grid()
            st.pyplot(fig)

def grafico_barras():

    data=carregar_dados()

    st.title("grafico de barras")

    fig=plt.figure(figsize=(10,8))

    plt.title("destribuição de pokemons por tipo")
    plt.xlabel("Tipo")
    plt.ylabel("quantidade de pokemons")
    plt.xticks(rotations=45)
    plt.grid(axis="y")

    typo_counts = pd.concat([data["type1"],data["type2"]]).value_counts()
    st.pyplot(fig)

    with st.expander("codigo para gerar o grafico"):
        with st.echo():
            data=carregar_dados()
            st.title("grafico de barras")
            fig=plt.figure(figsize=(10,8))
            plt.title("destribuição de pokemons por tipo")
            plt.xlabel("Tipo")
            plt.ylabel("quantidade de pokemons")
            plt.xticks(rotations=45)
            plt.grid(axis="y")

def main():

    st.sidebar.title("navegação")
    pages={"Pagina inicial": home, "linhas": grafico_linhas }
    selection = st.sidebar.selectbox("ir para", list(pages.keys()))
    st.sidebar.title("sobre")
    st.sidebar.write("projeto tem como ojeto de estudo os monstrinho de bolso ta ligado")
    


if __name__ == "__main__":
    main()  
