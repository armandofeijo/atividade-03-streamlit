import streamlit as st
import pandas as pd
import base64
#import seaborn as sns
#
import plotly.express as px
import plotly.graph_objects as go
import plotly.offline as po
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import matplotlib.pyplot as plt
import plotly.express as px
import random
import plotly.figure_factory as ff
from utils import (
    # CESAR_LOGO,
    APP_TITLE,
    PAGE_TITLE,
    LOGO,
    PATH,
    BANDREC,
)

# Aqui onde configuramos o título da página e o logo que aparecerá no Browser!!!
st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=LOGO,
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title(APP_TITLE)

## Data Operations ##
PATH = "data/infrarec.csv"
df = pd.read_csv(PATH, encoding='utf-8', error_bad_lines=False)

def png_to_base64(file_path):
    with open(file_path, "rb") as img_file:
        base64_encoded = base64.b64encode(img_file.read()).decode("utf-8")
        return base64_encoded

# COLUNAS Imgs
mcol1, mcol2, mcol3, mcol4 = st.columns(4)
# COLUNAS flags

with st.sidebar:
    st.image(LOGO)
    #st.write("Visit our Website")
    st.markdown("<h3 style='text-align: center;'>Visite nosso Website</h3>", unsafe_allow_html=True)
    flc1, flc2, flc3, flc4= st.columns(4)
    with flc2:
        # FIXME: note que se usarmos a opção com st.image, não ficará centralizado!
        #        assim, escolho usar a opção de colocar imagens com Markdown.
        #st.image(BR_FLAG, width=30)
        # mc_site_br = "https://www.mcdonalds.com.br/"  # Replace with your desired URL
        # mc_site_us = "https://www.mcdonalds.com/us/en-us.html"

        st.image(BANDREC, width=30)
        pcr_site =  "https://recife.pe.gov.br/"

        st.markdown(
            f'<div style="display: flex; flex-direction: column; align-items: center;">'
            # f'<a href="{mc_site_br}" target="_blank" onclick="open_link(\'{mc_site_br}\')"> '
            # f'<img src="{BR_FLAG}" style="width: 30px;"></a>'
            f'<a href="{pcr_site}" target="_blank" onclick="open_link(\'{pcr_site}\')"> '
            f'<img src="{BANDREC}" style="width: 30px;"></a>'
            f'</div>',
            unsafe_allow_html=True
        )
    with flc3:
        # FIXME: note que se usarmos a opção com st.image, não ficará centralizado!
        #        assim, escolho usar a opção de colocar imagens com Markdown.
        #st.image(US_FLAG, width=30)
        st.markdown(
            f'<div style="display: flex; flex-direction: column; align-items: center;">'
            # f'<a href="{mc_site_br}" target="_blank" onclick="open_link(\'{mc_site_br}\')"> '
            # f'<img src="{BR_FLAG}" style="width: 30px;"></a>'
            f'<a href="{pcr_site}" target="_blank" onclick="open_link(\'{pcr_site}\')"> '
            f'<img src="{BANDREC}" style="width: 30px;"></a>'
            f'</div>',
            unsafe_allow_html=True
        )

with st.container():
    with mcol1:
        st.image(BANDREC)

        scol1, scol2 = st.columns(2)

        with scol1:
            df = pd.read_csv(PATH, sep=';', encoding='latin-1')
            # Análise exploratória das infrações de trânsito
            df['infracao_texto'] = df['infracao'].astype(str)
            top_infracoes = df.groupby(by=['descricaoinfracao'])['descricaoinfracao'].count().sort_values(ascending=False).head(10)

            # Criar DataFrame com as top 10 infrações
            df_top10_infracoes = top_infracoes.reset_index(name='quantidade')
            total_outros = top_infracoes[10:].sum()
            df_top10_infracoes.loc[len(df_top10_infracoes)] = ['Outros tipos de Infrações', total_outros]

            # Plotar gráfico usando Seaborn
            plt.figure(figsize=(10, 6))
            #ax = sns.barplot(y='descricaoinfracao', x='quantidade', data=df_top10_infracoes)
            # ax.set_title('Top 10 tipos de Infrações de Trânsito em Recife - PE, no ano de 2023')
            # ax.set_xlabel('Qtde. de Infrações')
            # ax.set_ylabel('Infração')

            # Plotar gráfico usando Plotly
            fig = go.Figure(data=[go.Pie(labels=df_top10_infracoes['descricaoinfracao'], values=df_top10_infracoes['quantidade'])])
            fig.update_layout(title="Top 10 Infrações de Trânsito mais recorrentes em 2023 na cidade de Recife")
            fig.show()



            df['infracao_texto'] = df['infracao'].astype(str)

            df1 = df['infracao'].value_counts()
            df1.head()

            df2 = df['descricaoinfracao'].unique()
            df2.shape
            # como o resultado aqui deu 255 e é diferente do df3 e df4 (abaixo), que são 182,
            # muito provavelmente a coluna 'descricaoinfracao' tem valores diferentes
            # para um mesmo código de infracao (coluna 'infracao')

            df3 = df['infracao'].unique()
            df3.shape

            df4 = df['infracao_texto'].unique()
            df4.shape

            top_infracoes = df.groupby(by=['descricaoinfracao'])['descricaoinfracao'].count().sort_values(ascending=False)

            top_infracoes.head(10) # top 10, 80% do total de infrações 20% dos tipos de infrações

            # Criar um novo DataFrame com as primeiras 35 linhas de top_infracoes
            df_top10_infracoes = top_infracoes.head(10).reset_index(name='quantidade')

            # Exiba o novo DataFrame
            print(df_top10_infracoes)

            #Calcule o total das demais linhas de top_infracoes
            total_outros = top_infracoes[10:].sum()

            # Adicione uma nova linha ao final do df_top35_infracoes
            df_top10_infracoes.loc[len(df_top10_infracoes)] = ['Outros tipos de Infrações', total_outros]

            # Exiba o DataFrame atualizado
            print(df_top10_infracoes)

            """#5. Plotar Gráfico usando Seaborn"""

           

            """#6. Plotar Gráfico usando Plotly"""

            plt.figure(figsize=(12, 6))
            plt.barh(df_top10_infracoes.descricaoinfracao, df_top10_infracoes.quantidade)  # Corrigido aqui

            plt.xticks(rotation=45, ha='right', fontsize=8)

            plt.title("Top 10 tipos de Infrações de Trânsito em Recife - PE, no ano de 2023")
            plt.xlabel("Qtde. de Infrações")

            plt.tight_layout()
            plt.show()

            """## Gráfico de Pizza das Top 10 Infrações de Trânsito mais recorrentes em 2023 na cidade de Recife"""

            y_val = df_top10_infracoes['quantidade']

            data = [
                go.Pie(
                    labels=df_top10_infracoes['descricaoinfracao'].astype(str),
                    values=y_val,
                    insidetextorientation='radial',
                    #textinfo='label+percent',
                    hole=0.5,
                    marker=dict(colors=['#483D8B', '#DB7093', '#8FBC8F', '#E9967A', '#CD853F', '#00FFFF'])
                )
            ]

            layout = go.Layout(
                title="Top 10 Infrações de Trânsito mais recorrentes em 2023 na cidade de Recife",
                plot_bgcolor='#00ff00'
            )

            fig = go.Figure(data=data, layout=layout)

            fig.show()
           

    with mcol2:
        st.image(BANDREC)
        # sel_chicken = st.toggle("Select Chicken")
        # st.image(DRINKS)
        # sel_drinks = st.toggle("Select Drinks")

    with mcol3:
        st.image(BANDREC)
        # sel_sides = st.toggle("Select Sides")
        # st.image(MC_CAFE)
        # sel_mccafe  = st.toggle("Select McCafe Coffes")

    with mcol4:
        st.image(BANDREC)
        # sel_break = st.toggle("Select Breakfast")
        # st.image(SALAD)
        # sel_salads = st.toggle("Select Salads")

   