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
    # N_SELECTED,
    # CESAR_LOGO,
    APP_TITLE,
    # SALAD,
    # DRINKS,
    PAGE_TITLE,
    # MC_LOGO,
    LOGO,
    # BREAKFAST_LOGO,
    # BURGERS,
    # CHICKEN,
    # SIDES,
    # BR_FLAG,
    # US_FLAG,
    # MC_CAFE,
    # TREATS,
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
#DATA_PATH = "data/menu.csv"
#df = pd.read_csv(DATA_PATH)
PATH = "data/infrarec.csv"
df = pd.read_csv(PATH, encoding='utf-8', error_bad_lines=False)

## --------------- ##

## GLOBAL ##
# selected_options = []

def png_to_base64(file_path):
    with open(file_path, "rb") as img_file:
        base64_encoded = base64.b64encode(img_file.read()).decode("utf-8")
        return base64_encoded


# ## vars
# LISTA_C = [
#     "Our Menu",
#     "Download App",
#     "MyMcDonalds Rewards",
#     "Exclusive Deals",
#     "About Our Food",
#     "Locate",
#     "Gift Cards",
#]

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

            # Criar gráfico de violino
           # ax = sns.violinplot(y=df_top10_infracoes['quantidade'], x=df_top10_infracoes['descricaoinfracao'], color='lightgray')

            # Adicionar barras ao lado do gráfico de violino
            #barplot = sns.barplot(y=df_top10_infracoes['quantidade'], x=df_top10_infracoes['descricaoinfracao'], ax=ax, color='skyblue')

            # Adicionar título ao gráfico
            #ax.set_title('Distribuição de Infrações por Tipo')

            # Renomear rótulos dos eixos x e y
            # ax.set_xlabel('Infração')
            # ax.set_ylabel('Quantidade')

            # # Girar os rótulos do eixo x em 90 graus
            # ax.set_xticklabels(ax.get_xticklabels(), rotation=90)

            # # Adicionar valores percentuais no topo das barras
            # for p in barplot.patches:
            #     barplot.annotate(f'{p.get_height()/sum(df_top10_infracoes["quantidade"])*100:.2f}%',
            #                     (p.get_x() + p.get_width() / 2., p.get_height()),
            #                     ha='center', va='center', xytext=(0, 10), textcoords='offset points', fontsize=8)

            # # Aumentar o eixo y para 150,000
            # ax.set_ylim(0, 150000)

            # # Exibir o gráfico
            # plt.show()

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

    # Debug na tela das opções selecionadas, lembrando que selected_otions é um var global!
    # selected_options.append("Beef & Pork" if sel_burgers else "")
    # selected_options.append("Smoothies & Shakes" if sel_desserts else "")
    # selected_options.append("Chicken & Fish" if sel_chicken else "")
    # selected_options.append("Beverages" if sel_drinks else "")
    # selected_options.append("Snacks & Sides" if sel_sides else "")
    # selected_options.append("Coffee & Tea" if sel_mccafe else "")
    # selected_options.append("Breakfast" if sel_break else "")
    # selected_options.append("Salads" if sel_salads else "")

    # Filter out empty strings (options not selected)
    # selected_options = [option for option in selected_options if option]

    # print(f"Selected options: {', '.join(selected_options)}")

# with st.container():
#     st.write("------------------------------------------------")
#     scol1, scol2 = st.columns(2)

#     with scol1:
#         tc1, _ = st.columns(2)
#         with tc1:
#             option = st.selectbox(
#                 'Selecione o parâmetro de análise desejado:',
#                 df.columns)
#             # FIltrar daframe!!!
#             dfs = df[df['Category'].isin(selected_options)]
#         # Plot da primeira visualização
#         fig = px.bar(
#             dfs,
#             x="Item",
#             y=option,
#             text=f"{option}",
#             title=f"{option} in Different Foods",
#         )
#         st.plotly_chart(fig, use_container_width=True)



#     with scol2:
#             # Plot da primeira visualização
#             fig = px.bar(
#                 dfs,
#                 x="Item",
#                 y=option,
#                 text=f"{option}",
#                 title=f"{option} in Different Foods",
#             )
#             st.plotly_chart(fig, use_container_width=True)

#     st.write("------------------------------------------------")
        
# Comentario do professor abaixo:

    # st.write(df.head(5))

    # option = st.selectbox(
    #     'Selecione o parâmetro de análise desejado:',
    #     df.columns)

    # print(f" A opção desejada para plot foi {option}")

#

# with st.container():
#     # Variáveis auxiliares para construção do dashboard
#     lista_itens = df["Category"].unique()
#     col1, col2, col3 = st.columns(3)

#     col1.metric("Temperature", "70 °F", "1.2 °F")
#     col2.metric("Wind", "9 mph", "-8%")
#     col3.metric("Humidity", "86%", "4%")
#     # # SELECTBOX dos itens
#     # option_categoria = "Breakfast"
#     # print(f"Você selecionou {option_categoria}")

#     data_df = pd.DataFrame(
#         {
#             "category": [
#                 "📊 Data Exploration",
#                 "📈 Data Visualization",
#                 "📊 Data Exploration",
#             ],
#         }
#     )

#     st.data_editor(
#         data_df,
#         column_config={
#             "category": st.column_config.SelectboxColumn(
#                 "Choose your Visualization",
#                 help="The category of the app",
#                 width="medium",
#                 options=[
#                     "📊 Data Exploration",
#                     "📈 Data Visualization",
#                 ],
#                 required=True,
#             )
#         },
#         hide_index=True,
#     )

    # # Realizar operação de filtrar pela categoria desejada
    # dfs = df[df['Category'].isin(selected_options)]

    # st.write(dfs.head(N_SELECTED))

    # # Plot da primeira visualização
    # fig = px.bar(
    #     dfs,
    #     x="Item",
    #     y="Calories",
    #     text="Calories",
    #     title="Calories in Different Foods",
    # )

    # st.plotly_chart(fig, use_container_width=True)
