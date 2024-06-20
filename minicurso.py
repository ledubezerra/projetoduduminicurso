import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

def home():

    st.title("Projeto Pokemon")
    st.write("Este é um projeto meu, dudu do bigode, que tem como objetivo mostrar algumas informações de extrema relevancia sobre pokemons através de gráficos. Para tanto foi utilizado um banco de dados público dos jogos de pokemon até a 6ª geração. Você pode acessar os gráficos assim como os codigos usados para crialos atravez da barra de navegação ao lado.")


def carregar_dados():

    data = pd.read_csv("PokemonData.csv")
    return data

def grafico_linhas():

    st.title("Grafico de linhas")

    data = carregar_dados()

    fig = plt.figure(figsize=(10,10))

    data.groupby("Generation")["HP"].mean().plot(marker="o")

    plt.title("Tendencia do hp dos pokemons ao longo das gerações")
    plt.xlabel("Geração")
    plt.ylabel("Média de hp")
    plt.grid()
    st.pyplot(fig)

    with st.expander("codigo para gerar o gráfico de linhas"):
        with st.echo():
                data = carregar_dados()
                fig = plt.figure(figsize=(10,10))
                data.groupby("Generation")["HP"].mean().plot(marker="o")
                plt.title("Tendencia do hp dos pokemons ao longo das gerações")
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

    with st.expander("codigo para gerar o gráfico de barras"):
        with st.echo():
                data=carregar_dados()
                fig=plt.figure(figsize=(10,8))
                type_counts = pd.concat([data["Type1"],data["Type2"]]).value_counts()
                type_counts.plot(kind="bar")
                plt.title("Distribuição de pokemons por tipo")
                plt.xlabel("Tipo")
                plt.ylabel("Quantidade de pokemons")
                plt.grid(axis="y")
                plt.xticks(rotation=45)
        

def main():

    st.sidebar.title("Navegação")
    pages={"Pagina inicial": home, "Tendencia do hp dos pokemons ao longo das gerações(Gráfico de linhas)": grafico_linhas, "Distribuição de pokemons por tipo(Gráfico de Barras": grafico_barras }
    selection = st.sidebar.selectbox("ir para", list(pages.keys()))
    pages[selection]()
    st.sidebar.title("sobre")
    st.sidebar.write("O projeto tem como objeto de estudo os adoráveis monstrinhos de bolso da franquia Pokémon, criada originalmente em 1996 pelo desenvolvedor japonês Satoshi Tajiri e sua equipe na Game Freak. Explorando a fascinante ecologia e diversidade dessas criaturas digitais, a pesquisa mergulha nas intricadas relações entre treinadores e Pokémon, revelando insights profundos sobre a cultura pop e a nostalgia dos fãs. Com uma abordagem meticulosa, o estudo desvenda os segredos por trás dos lendários, os mistérios dos tipos elementais e a influência dos jogos e desenhos animados no imaginário coletivo. Assim, oferece uma perspectiva única sobre como esses seres virtuais transcendem as fronteiras do entretenimento para se tornarem ícones da imaginação global.Espero que tenha capturado o espírito do Lerolero Generator!")
    


if __name__ == "__main__":
    main()  
