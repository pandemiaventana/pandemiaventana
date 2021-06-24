#!/usr/bin/env python
# coding: utf-8

# # Lo nuevo
# 
# De forma rápida, los datos procesados.

# In[1]:


### Los paquetes amigos
import os, os.path
from IPython.display import Markdown, HTML, Javascript
import pandas as pd


# ## Archivos CSV

# In[2]:


### Algo de Markdown
display(Markdown('Encontré los **siguientes archivos CSV**:'))

### Mostrando archivos CSV
for string in [name for name in os.listdir('./../../out/site/csv')]:
    
    ### Título
    
    display(Markdown('<h3><a href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/{}">"{}"</a></h3>'.format(string, string)))
    
    ### Leemos
    
    csv = pd.read_csv('./../../out/site/csv/{}'.format(string))
    
    ### Info de pandas
    
    display(Markdown('Tiene las siguientes columnas (**{}** sin el índice):'.format(len(csv.columns) - 1)))
    
    display(csv.info(max_cols=len(csv.columns)))
    
    display(Markdown('<hr>'))


# ## Salida para Markdown

# In[3]:


### Gracias a BenVida (stackoverflow.com/a/64495269/13746427) ###
Javascript('''{
    let outputs=[...document.querySelectorAll(".cell")].map(
        cell=> {
            let output=cell.querySelector(".output")
            if(output) return output.innerHTML
            output=cell.querySelector(".rendered_html")
            if(output) return output.innerHTML
            return ""
        }
    )
    
    IPython.notebook.kernel.execute("cell_outputs="+JSON.stringify(outputs)) 
}''')


# In[4]:


cell_outputs[3]


# In[58]:


### Gracias a Daniel Stutzbach y Bruno Bronosky (stackoverflow.com/a/2632251/13746427) ###
for string in [name for name in os.listdir('..//..')]:
    if string == 'README.md':
        md = open('..//..//{}'.format(string))
        txt = md.read()
        full = txt + cell_outputs[3]


# In[55]:


full


# In[56]:


display(Markdown(full))

