#!/usr/bin/env python
# coding: utf-8

# # Lo nuevo
# 
# De forma rápida, los datos procesados.

# In[1]:


### Los paquetes amigos
import os, os.path
from IPython.display import Markdown, HTML
import pandas as pd


# ## Archivos CSV

# In[2]:


### Algo de Markdown
display(Markdown('Encontré los **siguientes archivos CSV**:'))

### Mostrando archivos CSV
for string in [name for name in os.listdir('./../../out/site/csv')]:
    
    ### Título
    
    display(Markdown('<h3><a href="../../../../out/site/csv/{}">"{}"</a></h3>'.format(string, string)))
    
    ### Leemos
    
    csv = pd.read_csv('./../../out/site/csv/{}'.format(string))
    
    ### Info de pandas
    
    display(Markdown('Tiene las siguientes columnas (**{}** sin el índice):'.format(len(csv.columns) - 1)))
    
    display(csv.info(max_cols=len(csv.columns)))
    
    display(Markdown('<hr>'))


# ## Archivos HTML

# In[3]:


### Algo de Markdown
display(Markdown('Encontré las **siguientes gráficas interactivas en HTML**:'))
    
### Mostrando gráficas HTML
for string in [name for name in os.listdir('./../../out/site/graph')]:
    display(Markdown('- <a href="../../../../out/site/graph/{}">"{}"</a>.'.format(string, string)))

