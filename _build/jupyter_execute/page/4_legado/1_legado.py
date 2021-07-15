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
from markdownify import markdownify as md
from natsort import natsorted


# ## Archivos CSV

# In[2]:


get_ipython().run_cell_magic('capture', 'archivocsv', '\n### Mostrando archivos CSV\n\n### Ser perfeccionista es terrible ###\ndatas = [name for name in os.listdir(\'./../../out/site/csv\')]\ndatas = natsorted(datas)\ndatas = datas[-1:] + datas[:-1]\n\nfor string in datas:\n    \n    ### Título\n    \n    display(Markdown(\'<a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/{}">"{}"</a>\'.format(string, string.upper())))\n    ### Leemos\n    \n    csv = pd.read_csv(\'./../../out/site/csv/{}\'.format(string))\n    \n    ### Info de pandas\n    \n    display(Markdown(\'Tiene las siguientes columnas (**{}** sin el índice):\'.format(len(csv.columns) - 1)))\n    \n    for col in csv.columns:\n        \n        display(Markdown(\'- \' + col + \' con **{}** datos válidos.\'.format(len(csv.index) - csv[col].isnull().sum())))\n    \n    display(Markdown(\'<hr>\'))')


# In[3]:


### Visualizamos
for outputs in archivocsv.outputs:
    display(outputs)


# ## Salida para Markdown

# In[4]:


txt1 = '''# La pandemia por la ventana \n

![Ilustración por Bernardo Dinamarca](https://github.com/pandemiaventana/pandemiaventana/blob/main/img/page/2_cover.png?raw=true)

*Ilustración por Bernardo Dinamarca*

## Intro

[La pandemia por la ventana es un sitio](https://pandemiaventana.github.io/pandemiaventana/), realizado con formato de *libro* gracias a Jupyter Books, hecho por Alejandro Dinamarca, que recaba el trabajo de Numeral.lab en la Región de Tarapacá.

La página posee los siguientes ejes:

- Reunir antecedentes del trabajo de Numeral.lab en la Región de Tarapacá en la pandemia del COVID-19.

- Recopilar experiencias personales de Alejandro Dinamarca en el trabajo voluntario en Numeral.lab.

- Monitoreo de la pandemia del COVID-19 en la Región de Tarapacá de forma automática.

- Recabar información del repositorio del MICITEC en GitHub, específicamente, de la Región de Tarapacá.

- Procesar datos recabados.

- Generar informes (epidemiológicos, avance en campaña de vacunación y predictor de fase del Paso a Paso).

- Generar concientización en ciudadanía bajo tendencias de la pandemia.

> Agradecimientos al Equipo Futuro del MICITEC por la democratización de los datos de la pandemia en Chile, a los desarrolladores de Jupyter Notebook, Jupyter Book y a todas las librerías de Python implicadas en los scripts, como también, a los propios desarrolladores de Python.

Favor, cualquier sugerencia o comentario, hacerlo llegar mediante [Issues de GitHub](https://github.com/pandemiaventana/pandemiaventana/issues/new).

## Funcionamiento

Básicamente, a través de Notebooks de Jupyter y un poco de Markdown. Python, por contraparte, genera los CSV, y Jupyter Books se encarga de generar la página web a partir de los Notebooks y el Markdown.

El despliegue del libro en [gh-pages](https://github.com/pandemiaventana/pandemiaventana/tree/gh-pages) se realiza cada vez que:

- Desencadeno un cambio en [main](https://github.com/pandemiaventana/pandemiaventana)

- Periódicamente desde las 11:30 hrs. a las 19:30 hrs. (hora de Santiago de Chile).

A través del action [actualiza_libro](https://github.com/pandemiaventana/pandemiaventana/actions/workflows/book.yml).

## Estado

[![deploy-book](https://github.com/pandemiaventana/pandemiaventana/actions/workflows/book.yml/badge.svg)](https://github.com/pandemiaventana/pandemiaventana/actions/workflows/book.yml)

## DOI

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5044609.svg)](https://doi.org/10.5281/zenodo.5044609)

## Archivos CSV generados

Disponibles en [el siguiente enlace](https://github.com/pandemiaventana/pandemiaventana/tree/main/out/site/csv), los cuales se adjuntan a continuación:

'''

outputs_ = archivocsv.outputs

vec_out = []
for outs_ in outputs_:
    ### Convertimos a lista los outputs
    vec_out += list(outs_.data.values())

### Nuestro string
vec_ = ''
### Recorremos la lista de outputs
for vec in vec_out:
    vec = str(vec)
    ### Quitamos el str de datos de tabla sin formato
    if vec.startswith("            "):
        pass
    else:
        ### Quitamos el str del tipo de variable
        vec = vec.replace('<IPython.core.display.Markdown object>', '')
        ### Finalmente, añadimos al vector
        vec_ += '<br>' + vec

### Abrimos y modificamos el HTML
with open('../../README.md', 'w', encoding='UTF-8') as f:
    f.write(txt1 + vec_)


# In[5]:


with open('../6_basedatos/2_basedatos.md', 'w', encoding='UTF-8') as f:
    f.write('''# Archivos
    
''' + vec_)


# ## Archivos PDF

# In[6]:


get_ipython().run_cell_magic('capture', 'archivopdf', '\n### Gracias a Daniel Stutzbach y Bruno Bronosky (stackoverflow.com/a/2632251/13746427) ###\nsum_ = []\ndirr = [\'diario\', \'vacuna\', \'indicadorfase\']\nnames = [\'Reporte diario\', \'Balance de vacunas\', \'Indicador de Fase\']\np = 0\nfor reporte in dirr:\n    display(Markdown(\'<h2>{}</h2>\'.format(names[p])))\n    display(Markdown(\'Encontré los siguientes PDF:\'.format(names[p])))\n    exec(\'sum_{} = []\'.format(reporte))\n    for string in [name for name in os.listdir(\'../../out/{}/pdf\'.format(reporte))]:\n        if os.path.isdir(\'../../out/diario/pdf/{}\'.format(string)):\n            pass\n        else:\n            exec(\'sum_{} += [string]\'.format(reporte))\n            exec(\'sum_{} = natsorted(sum_{})\'.format(reporte, reporte))\n    exec(\'\'\'for ipdf in sum_{}:\n        display(Markdown(" <a href=\'https://docs.google.com/gview?url=https://github.com/pandemiaventana/pandemiaventana/raw/main/out/" + reporte + "/pdf/" + ipdf + "&embedded=true\'>" + ipdf + "</a>"))\'\'\'.format(reporte))\n    p += 1\n    \ntxt2 = """# Archivo\n\n"""')


# In[7]:


### Visualizamos
for outputs in archivopdf.outputs:
    display(outputs)


# ## Salida de archivos PDF

# In[8]:


outputs_ = archivopdf.outputs

vec_out = []
for outs_ in outputs_:
    ### Convertimos a lista los outputs
    vec_out += list(outs_.data.values())

### Nuestro string
vec_ = ''
### Recorremos la lista de outputs
for vec in vec_out:
    vec = str(vec)
    ### Quitamos el str de datos de tabla sin formato
    if vec.startswith("            "):
        pass
    else:
        ### Quitamos el str del tipo de variable
        vec = vec.replace('<IPython.core.display.Markdown object>', '')
        ### Finalmente, añadimos al vector
        vec_ += '<br>' + vec

### Abrimos y modificamos el MD
with open('../../page/5_reportes/4_reportes.md', 'w', encoding='UTF-8') as f:
    f.write('''# Reportes históricos
A continuación, dispongo los reportes históricos a partir de la fecha de publicación de la página. En caso de requerir otras ediciones, consultar <a href="https://www.instagram.com/numeral.lab/">Instagram</a>.
''' + vec_)


# ## Información de sesión

# In[9]:


session_info.show(cpu=True, jupyter=True, std_lib=True, write_req_file=True, dependencies=True, req_file_name='4_requeriments.txt')

