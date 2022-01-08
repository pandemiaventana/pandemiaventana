#!/usr/bin/env python
# coding: utf-8

# ## Variantes de COVID-19 en Chile
# 
# En relación al [ISSUE #1089 de la base de datos COVID-19 del Ministerio de Ciencia, Tecnología, Conocimiento e Innovación](https://github.com/MinCiencia/Datos-COVID19/issues/1089), quise aportar con mi granito de arena a incorporar las variantes a nivel nacional (en caso de disponer a nivel Regional, informarlo en este mismo repositorio).
# 
# > ¿Qué fuente utilizaremos? La página [Covariants](https://covariants.org/), que entrega información sobre las variantes del Coronavirus de distintos países, realizada por Emma Hodcroft y otros autores.
# 
# > Para los archivos generados en la presente sección, [recurrir al siguiente vínculo](https://github.com/pandemiaventana/pandemiaventana/tree/main/out/variants).

# In[1]:


# Manejo de datos
import pandas as pd
# Módulo para obtener datos y módulo JSON
import requests, json, locale
# Módulo para graficar
import plotly.graph_objects as go
locale.setlocale(locale.LC_TIME, 'es_ES') 


# In[2]:


# Pedimos datos de texto con formato JSON con módulo tradicional de Python
data = requests.get('https://raw.githubusercontent.com/hodcroftlab/covariants/master/web/data/perCountryData.json')
# Transformamos datos anteriores a salida JSON
variants = data.json()
# En record_path se colocan obs. objetivos, y en meta información añadida, en orden jerárquico según JSON
variants_nested = pd.json_normalize(variants, record_path = ['regions', 'distributions', 'distribution'], meta=[['regions', 'distributions', 'country']])
# Renombramos algunas columnas
variants_nested = variants_nested.rename(columns = {'total_sequences':'Secuencias', 'week': 'Semana', 'regions.distributions.country': 'Pais'})
# Mejoramos la legibilidad de las columnas de variantes
variants_nested.columns = variants_nested.columns.str.replace(
    'cluster_counts.', '', regex=False)
# Colocamos índice como datetime
variants_nested.index = pd.to_datetime(variants_nested['Semana'])
variants_nested.drop('Semana', axis=1, inplace=True)
# Guardamos un archivo global
variants_nested.to_csv('variantesglobales.csv')


# In[35]:


# Filtramos datos de chilito
variants_nested_cl = variants_nested.loc[variants_nested['Pais'] == 'Chile']
# Eliminamos columas innecesarias
variants_nested_cl = variants_nested_cl.drop('Pais', axis=1)
variants_nested_cl.dropna(axis=1, how='all', inplace=True)
# Guardamos archivo de variantes en Chile
variants_nested_cl.to_csv('varianteschile.csv')


# In[95]:


fig = go.Figure()
for variante in variants_nested_cl.loc[:, '20B/S:732A':]:
    fig.add_trace(go.Scatter(x=variants_nested_cl.index.strftime('%d %b %Y'), y=variants_nested_cl[variante],
                    mode='lines',
                    name=variante))
fig.update_layout(title='Variantes de Coronavirus en Chile',
    xaxis=dict(
        showline=True,
        showgrid=True,
        showticklabels=True,
        linecolor='rgb(204, 204, 204)',
        linewidth=2,
        ticks='outside',
        tickfont=dict(
            family='Arial',
            size=12,
            color='rgb(82, 82, 82)',
        ),
    ),
    yaxis=dict(
        showgrid=True,
        zeroline=True,
        showline=True,
        showticklabels=True,
    ),
    plot_bgcolor='white'
)
fig.update_xaxes(
        tickangle = 20,
nticks=15)

