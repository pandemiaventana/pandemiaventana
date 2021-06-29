#!/usr/bin/env python
# coding: utf-8

# # Lo nuevo
# 
# De forma rápida, los datos procesados.

# In[1]:


### Los paquetes amigos
import os, os.path
from IPython.display import Markdown, HTML, Javascript, IFrame
import pandas as pd
import session_info
from bs4 import BeautifulSoup
import numpy as np


# ## Archivos CSV

# In[2]:


### Mostrando archivos CSV
for string in [name for name in os.listdir('./../../out/site/csv')]:
    
    ### Título
    
    display(Markdown('<h3><a href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/{}">"{}"</a></h3>'.format(string, string)))
    
    ### Leemos
    
    csv = pd.read_csv('./../../out/site/csv/{}'.format(string))
    
    ### Info de pandas
    
    display(Markdown('Tiene las siguientes columnas (**{}** sin el índice):'.format(len(csv.columns) - 1)))
    
    csv.info(max_cols=len(csv.columns), memory_usage='deep')
    
    display(Markdown('<hr>'))


# ## Salida para Markdown

# In[3]:


txt = '''# La pandemia por la ventana \n

![Ilustración por Bernardo Dinamarca](https://github.com/pandemiaventana/pandemiaventana/blob/main/img/page/2_cover.png?raw=true)

**Ilustración por Bernardo Dinamarca**

La pandemia por la ventana es un sitio, realizado con formato de *libro* gracias a Jupyter Books, hecho por Alejandro Dinamarca, que recaba el trabajo de Numeral.lab en la Región de Tarapacá.

Favor, cualquier sugerencia o comentario, hacerlo llegar mediante [Issues de GitHub](https://github.com/pandemiaventana/pandemiaventana/issues/new).

## Funcionamiento

Básicamente, a través de Notebooks de Jupyter y un poco de Markdown. Python, por contraparte, genera los CSV, y Jupyter Books se encarga de generar la página web a partir de los Notebooks y el Markdown.

El despliegue del libro en [gh-pages](https://github.com/pandemiaventana/pandemiaventana/tree/gh-pages) se realiza cada vez que:

- Desencadeno un cambio en [main](https://github.com/pandemiaventana/pandemiaventana)

- Periódicamente desde las 11:30 hrs. a las 19:30 hrs. (hora de Santiago de Chile).

A través del action [actualiza_libro](https://github.com/pandemiaventana/pandemiaventana/actions/workflows/book.yml).

## Estado

[![deploy-book](https://github.com/pandemiaventana/pandemiaventana/actions/workflows/book.yml/badge.svg)](https://github.com/pandemiaventana/pandemiaventana/actions/workflows/book.yml)

## Archivos CSV generados

Disponibles en [el siguiente enlace](https://github.com/pandemiaventana/pandemiaventana/tree/main/out/site/csv), los cuales se adjuntan a continuación:

'''

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
    IPython.notebook.kernel.execute("soup = BeautifulSoup(cell_outputs[3])")
    IPython.notebook.kernel.execute("removals = soup.find_all(attrs={'class': 'prompt'})")
    IPython.notebook.kernel.execute("for removal in removals: removal.decompose()")
    IPython.notebook.kernel.execute("soup = str(soup)")   
    IPython.notebook.kernel.execute("op = open('../../README.md' , 'w', encoding='utf-16')")
    IPython.notebook.kernel.execute("full = txt + soup")
    IPython.notebook.kernel.execute("op.writelines(full)")
    IPython.notebook.kernel.execute("op.close()")
}''')


# ## Archivos PDF

# In[4]:


### Gracias a Daniel Stutzbach y Bruno Bronosky (stackoverflow.com/a/2632251/13746427) ###
sum_ = []
dirr = ['diario', 'vacuna', 'indicadorfase']
names = ['Reporte diario', 'Balance de vacunas', 'Indicador de Fase']
p = 0
display(Markdown('<h1>Reportes históricos</h1>'))
for reporte in dirr:
    display(Markdown('<h2>{}</h2>'.format(names[p])))
    display(Markdown('Encontré los siguientes PDF:'.format(names[p])))
    exec('sum_{} = []'.format(reporte))
    for string in [name for name in os.listdir('../../out/{}/pdf'.format(reporte))]:
        if os.path.isdir('../../out/diario/pdf/{}'.format(string)):
            pass
        else:
            exec('sum_{} += [string]'.format(reporte))
    exec('''for ipdf in sum_{}:
        display(Markdown("- <a href='https://docs.google.com/gview?url=https://github.com/pandemiaventana/pandemiaventana/raw/main/out/" + reporte + "/pdf/" + ipdf + "&embedded=true'>" + ipdf + "</a>"))'''.format(reporte))
    p += 1


# ## Salida de archivos PDF

# In[5]:


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
    IPython.notebook.kernel.execute("soup = BeautifulSoup(cell_outputs[7])")
    IPython.notebook.kernel.execute("removals = soup.find_all(attrs={'class': 'prompt'})")
    IPython.notebook.kernel.execute("for removal in removals: removal.decompose()")
    IPython.notebook.kernel.execute("soup = str(soup)")   
    IPython.notebook.kernel.execute("op = open('../5_reportes/4_reportes.md' , 'w', encoding='utf-16')")
    IPython.notebook.kernel.execute("full = soup")
    IPython.notebook.kernel.execute("op.writelines(full)")
    IPython.notebook.kernel.execute("op.close()")
}''')


# ## Información de sesión

# In[6]:


session_info.show(cpu=True, jupyter=True, std_lib=True, write_req_file=True, dependencies=True, req_file_name='4_requeriments.txt')

