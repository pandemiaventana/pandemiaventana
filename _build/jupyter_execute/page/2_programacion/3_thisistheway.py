#!/usr/bin/env python
# coding: utf-8

# # Salida
# 
# ---
# 
# :::{figure-md} markdown-fig
# <img src="../../img/page/2_cover.png" width="80%">
# 
# **Ilustración realizada por Bernardo Dinamarca**.
# :::
# 
# ¡Hola! Este notebook estará basado en recopilar, a través de la Visualización de Datos, las cifras históricas y actuales de la pandemia en Tarapacá. Aún no he indagado cómo hacer que se actualice de forma automática, pero eventualmente, ¡lo lograremos!

# ## Importando paquetes
# 
# Trabajaremos con las librerías del primer notebook y otras. Respecto a las librerías para visualización, no utilizaremos Matplotlib o Seaborn, dado que deseo realizar gráficas interactivas que sean visualmente limpias y atractivas. Además, incorporaremos al equipo Beautiful Soup, que es una librería para manipular lenguaje HTML.
# 
# Todo ésto, será en fin de generar dos salidas:
# 
# - Un reporte para el libro.
# 
# - Una página externa para incrustarse en el sitio de la Universidad Arturo Prat.
# 
# Anteriormente, trabajaba con Infogram, la cual es la misma plataforma que utiliza el Gobierno de Chile en su página de Cifras Oficiales. Sin embargo, la plataforma carece de automatización gratuita, y se debe pagar para lograr esa automatización.
# 
# En ese sentido, exportaremos una página HTML, para poder incrustarse en el sitio de la Universidad Arturo Prat.
# 
# Respecto a nuestro equipo de librerías habitual, sumamos:
# 
# - Plot.ly (librería de visualización dinámica e interactiva a partir de JavaScript).
# 
# :::{figure-md} markdown-fig
# <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Plotly-logo-01-square.png/1200px-Plotly-logo-01-square.png" width="50%">
# 
# **Logo de la librería <a href="https://plotly.com/python/">Plot.ly</a>**.
# :::
# 
# - Beautiful Soup (librería de Python para extraer datos de archivos HTML y XML).
# 
# :::{figure-md} markdown-fig
# <img src="https://funthon.files.wordpress.com/2017/05/bs.png?w=1024" width="50%">
# 
# **Logo de la librería <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup">Beautiful Soup</a>**.
# :::

# In[1]:


# Importando paquetes

### Librería de manipulación de datos 
import pandas as pd
pd.set_option('use_inf_as_na', True)
pd.options.display.float_format = '{:,.2f}'.format

### Librería de álgebra
import numpy as np

### Librerías para graficar
import plotly.graph_objects as go

### Customizamos opciones de Plot.ly
config = {'displayModeBar': False, 'showTips': False, 'scrollZoom': False}
layout = go.Layout(dragmode=False, 
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
        showticklabels=True,
    ),
    autosize=True,
    margin=dict(
        autoexpand=True,
        l=0,
        r=0,
        t=0,
    ),
    showlegend=True,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    legend=dict(
        itemclick="toggleothers",
        itemdoubleclick="toggle",
        orientation="h",
        yanchor="bottom",
        xanchor='right',
        x=1,
        y=1.02
    )
)

### Librería BeautifulSoup para manipular HTML
from bs4 import BeautifulSoup

### Para formato local de fecha
import locale
locale.setlocale(locale.LC_TIME, '')

### Otros paquetes
import math
import os, os.path
import json as json
import datetime
import time
from IPython.display import display, Markdown, HTML, Javascript, IFrame

### Gracias a joelostblom (https://gitlab.com/joelostblom/session_info)
import session_info


# ## Importando datos
# 
# Hacemos el mismo proceso habitual, con la diferencia que importaremos datos ya procesados.

# In[2]:


### Gracias a Daniel Stutzbach y Bruno Bronosky (stackoverflow.com/a/2632251/13746427) ###
sum = 0
for string in [name for name in os.listdir('..//..//out//site//csv//')]:
    sum += string.count('data')

## Cargamos cada uno de los csv (basado en el primer notebook)
x = range(1, sum+1)
data = []
for i in x:
    exec('data += [pd.read_csv("..//..//out//site//csv//data{}.csv", parse_dates=["Fecha"], index_col=["Fecha"])]'.format(i, i))


# ## Visualizando los datos
# 
# La diferencia de nuestras publicaciones (en contraste a la forma en que se entregaba información en otras páginas informativas en Instagram) se basaban en la visualización de datos, y en particular, en las tendencias semanales. También, se agregaban cálculos o datos que, en los reportes del Minsal, no se encontraban procesados.
# 
# Imaginemos que, lo único que hiciéramos fuese entregar cifras aisladas. ¿Qué retratan? ¿De dónde venimos? No es correcto que, por un día, debamos ser positivistas o negativistas. De hecho, esos pensamientos deparan en sesgos, y lo peor, en sesgos que no contemplan la integralidad de la pandemia. Por eso es relevante formar una mirada holística en la visualización de los datos. Las cifras de un día $X$ pueden ser sumamente variables al día $X+1$ en función de depender de la muestra (cantidad de exámenes PCR informados en el día $X$ o $X+1$). Por ello, es importante regirse por las tendencias, o por los estadísticos.
# 
# El problema es que, al ser Instagram, una plataforma homogénea, el storytelling debe ser accesible para todo público (con estudios matemáticos o no). De esa forma, los reportes tenían una alta presencia de tendencias a través de gráficas, y no así de estadísticos (a excepción de medias móviles semanales).
# 
# La comprensión de la pandemia debía partir desde el mejor storytelling (el contar una historia detrás de los datos). El tomar una idea, o un incidente, y contarla como una historia: Cada día particular de la pandemia es una hoja de esa historia (<i>una hoja del "libro" COVID-19 en Tarapacá</i>). Por esa razón, desarrollamos el reporte diario no solo con datos duros, sino también con gráficas de tendencia semanal.

# ### ¿Cuántos gráficos se visualizarán?

# In[3]:


display(Markdown('> Se visualizarán un total de **{} gráficos**.'.format(sum)))


# ### Automatizando salida de gráficos
# 
# A continuación, se desarrolla un código que recorre cada uno de los archivos .CSV que generamos en el primer notebook, del cual, realiza una "especie" de resumen de los estadísticos, visualiza los datos en un gráfico en Plot.ly y culmina con información adicional sobre:
# 
# - Descarga de los datos (solo funciona al presionar desde el libro publicado, no desde el notebook).
# 
# - La fecha de inicio y fin del gráfico.

# In[4]:


x = 0
### Título y otras cosas
display(Markdown('<h2 style="font-size:60px;">REPORTE DIARIO</h2>'))
display(Markdown('<h3 style="font-size:20px;">Región de Tarapacá, {}</h3>'.format(data[0].last_valid_index().strftime('%d de %B de %Y'))))

### Recorremos el vector que almacena los DataFrames, uno a uno
for dataframe in data:
    
    ### Para guardar el número del gráfico (un poco ordinario el método, lo sé)
    
    x += 1
    
    ### Definimos una nueva figura
    
    fig = go.Figure(layout=layout)
    
    ### Algunos datos y título
    
    display(Markdown('<h3> Gráfico {}</h3>'.format(x)))
    display(Markdown('El gráfico contiene las siguientes **columnas**: '))
    
    ### Recorremos cada una de las columnas del DataFrame anterior
    
    for col in dataframe.columns:
        
        ### Vector de fechas desde primer y último dato válido por cada columna
        
        index = dataframe[col].first_valid_index()
        index_ = dataframe[col].last_valid_index()
            
        ### DataFrame según filtro de primer dato válido
        
        _df = dataframe[index:]
            
        ### Índice de DataFrame según filtro anterior
            
        fecha = dataframe[index:].index
    
        ### Columna específica
        
        _col = dataframe[index:][col]
        
        ### Añadimos un trazado por cada columna, conectamos los valores para no tener discontinuidad y
        ### suavizamos por interpolación spline
        
        fig.add_trace(go.Scatter(x=_df.index.strftime('%d %b %Y'),
                                 y=_col,
                    mode='lines',
                    name=col,
                    connectgaps=True,
                    line_shape='linear',
                    hovertemplate =
                    '<b>{}</b>: '.format(col) + '%{y:.2f}'+'<br><b>Fecha</b>: %{x}<br>' + "<extra></extra>"))
        
        ### Para colocar en 35° las etiquetas del eje X, con el número de etiquetas proporcional al número de meses
        ### desde el primer dato válido
        
        fig.update_layout(xaxis = go.layout.XAxis(tickangle = 35,
                                                  nticks=len(_df.index.month.unique())))
        ### Más datos
        
        display(Markdown(' - <b>{}</b>.'.format(col)))
        display(Markdown("""El mayor valor es de **{}**, registrado el {}. 
        Asimismo, la mediana es de **{}**.
        Respecto a la dispersión de los datos, la desviación estándar es del **{}**. """
                         .format(dataframe[col].max(), dataframe[dataframe[col] == dataframe[col].max()].index[0].strftime('%d de %B de %Y'),
                                 round(dataframe[col].mean(), 2), round(dataframe[col].std(), 2))))
        display(Markdown('> El valor en base al último reporte diario o epidemiológico ({}) es de **{}**.'.format(dataframe[index_:].index[0].strftime('%d de %B de %Y'), dataframe[col][index_])))
    
    ### Mostramos la figura procesada en el ciclo anterior y otros datos. Añadimos espaciado
    display(Markdown('<h4>Visualización del gráfico {}</h4> <br> El gráfico, visualizado en <a href="https://plotly.com/python/">Plot.ly</a>: <br>'.format(x)))
    fig.show(config=config)
    
    ### Exportamos el gráfico a HTML
    fig.write_html("..//..//out//site//graph//data{}.html".format(x), config=config)
    
    
    display(Markdown("""> **Notas**: 
    <br> - El gráfico **inicia en el {}** y **termina el {}** en base a los datos disponibles.
    <br> - Para aislar una curva, presionar en el nombre o color en la leyenda. 
    <br> - Para remover una curva, seguir instrucción anterior, con la diferencia de presionar dos veces.""".format(\
                    _df.index[0].strftime('%d de %B de %Y'),
                    dataframe[index_:].index[0].strftime('%d de %B de %Y'))))
    display(Markdown('<h4>Información adicional sobre el gráfico {}</h4> <br>'.format(x)))
    display(Markdown(
    """<br>El **gráfico {}** utilizó los datos procesados en <a href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data{}.csv">data{}.csv</a>.
    La tabla de datos resumida:""".format(x, x, x, x)))
    display(dataframe)


# ### Automatizando salida para asistenciacovid19
# 
# En razón de brindar una página web que se pueda incrustar en el sitio de la Universidad Arturo Prat, generamos las siguientes líneas de codigo. ¿Cómo funciona?
# 
# - La salida completa de la celda anterior es capturada como lenguaje HTML, pero solo el cuerpo de la página {cite}```benvida```.
# 
# En este sentido, **dar gracias al usuario Benvida, de Stackoverflow** {footcite}```benvida```. El código original que desarrolló se encuentra a continuación, el cual modificaremos.
# 
# ```
# %%js
# {
#     let outputs=[...document.querySelectorAll(".cell")].map(
#         cell=> {
#             let output=cell.querySelector(".output_text")
#             if(output) return output.innerText
#             output=cell.querySelector(".rendered_html")
#             if(output) return output.innerHTML
#             return ""
#         }
#     )
#     
#     IPython.notebook.kernel.execute("cell_outputs="+JSON.stringify(outputs))    
# }
# 
# ```

# ### Inconvenientes
# 
# En primer lugar, el lenguaje de marcado (HTML) solo brinda la estructura básica del sitio, que se compone de texto, imágenes y scripts. Para que funcionen los scripts, en este caso, Plot.ly, se tienen múltiples dependencias de otras librerías de JavaScript.
# 
# JavaScript es un lenguaje de programación de alto nivel, el cual, tal como Python, tiene múltiples librerías que se especializan en distintas tareas y funciones. Plot.ly depende de otras librerías para funcionar, por lo que, para que el script de JavaScript, realizado por los creadores de Plot.ly, funcione, debemos no solo incorporar el código de los gráficos, sino también sus **dependencias**.
# 
# Para ello, incorporamos en el ```<head>``` las CDN. Estos son servidores, a partir de los cuales descargamos los archivos que tienen las dependencias.
# 
# Cabe recalcar que, además de código JavaScript, también incorporamos lenguaje de hojas de estilo en cascada (CSS), el cual le da formato y estilo al solitario HTML.
# 
# En analogía, y para simple comprensión, **HTML es el esqueleto (estructura), JS es la musculación (animaciones y movimiento) y CSS es la apariencia externa (piel y atributos físicos)**.
# 
# ### Algunos arreglos
# 
# - La función por BenVida es ejecutada una vez se terminó de ejecutar todas las celdas, y por ende, los outputs no son recopilados hasta que el Kernel culmina su ejecución.
# 
# Aquí se nos genera el siguiente problema: La variable ```cell_outputs``` no es asignada hasta que el Kernel termina su ejecución, por lo que si deséaramos actualizar el archivo HTML, en base a la celda anterior de código (donde están los gráficos Plot.ly), no podríamos, porque la variable ```cell_outputs```, y en concreto, ```cell_outputs[9]``` todavía no está asignada. ¿La solución? Ejecutar el código Python tras la ejecución del código JavaScript, y de esta forma, no tenemos inconvenientes. Para ello, utilizaremos la misma función que utilizó BenVida, `IPython.notebook.kernel.execute("")` donde en ```" "``` debe ir el código Python.
# 
# Por otro lado, al ser código JavaScript con Python, ¡se debe tener cuidado al utilizar comillas sobre doble comillas o viceversa! De otra forma, tendremos un error. Por esta razón, utilizamos la función ```format()``` de Python (ya que las URL deben ir entre comillas, le decimos a Python que se encargue de esa situación, sin que el input de JavaScript nos resulte en error).
# 
# ### Detalles
# 
# El sitio se encuentra en el directorio ``./file/site``. Respecto al funcionamiento del código para procesarlo:
# 
# - Modificamos al función para no solamente obtener el texto, sino que todo el HTML.
# 
# 
#  - Para no desperdiciar los estilos CSS que utiliza Jupyter Notebooks, copié los mismos archivos CSS en la carpeta del sitio (``ipython.min.css`` y ``style.min.css``). Los archivos se pueden encontrar en el directorio de Anaconda, ``usuario/anaconda3/Lib/site-packages/notebook/static/style``.
# 
# 
#  - Además, en el mismo directorio se encuentra el archivo JavaScript, ``plotly.js``, que debe estar en el directorio para que funcionen los gráficos interactivos.
# 
# 
#  - Se remueven los ``<div>`` con clase ``prompt``, que es lo que brinda el margen a la izquierda en Jupyter Notebooks.
# 
# 
# ```IPython.notebook.kernel.execute("soup = BeautifulSoup(cell_outputs[9])")
#     IPython.notebook.kernel.execute("removals = soup.find_all(attrs={'class': 'prompt'})")
#     IPython.notebook.kernel.execute("for removal in removals: removal.decompose()")
#     IPython.notebook.kernel.execute("soup = str(soup)")
# ```

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
    IPython.notebook.kernel.execute("soup = BeautifulSoup(cell_outputs[9])")
    IPython.notebook.kernel.execute("removals = soup.find_all(attrs={'class': 'prompt'})")
    IPython.notebook.kernel.execute("for removal in removals: removal.decompose()")
    IPython.notebook.kernel.execute("soup = str(soup)")   
    IPython.notebook.kernel.execute("html = open('../../out/site/balance.html','w')")
    IPython.notebook.kernel.execute("html.write(\
    '<html><head><link rel={} href={}><link rel={} href={}><link rel={} href={}><script src={}></script><script src={}></script></head><body>'\
    .format('stylesheet', 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css', \
    'stylesheet', './style.min.css', \
    'stylesheet', './ipython.min.css', \
    'https://cdn.plot.ly/plotly-latest.min.js', 'https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.6/require.js')\
    + soup +'</body></html>')")
    IPython.notebook.kernel.execute("html.close()")
}''')


# ### Peligro
# 
# Si hubiésemos utilizado solo Python, habríamos tenido el siguiente error (descomentar la línea de código).

# In[6]:


#html = open('balance.html','w')
#html.write('''<html><head><link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css'><script src='https://cdn.plot.ly/plotly-latest.min.js'></script><script src='https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.6/require.js'></script></head><body>''' +cell_outputs[9] +'''</body></html>''')
#html.close()


# ## Información de sesión

# In[7]:


session_info.show(cpu=True, jupyter=True, std_lib=True, write_req_file=True)


# ## Bibliografía de esta página
# 
# ```{footbibliography}
# ```
# 
# 
