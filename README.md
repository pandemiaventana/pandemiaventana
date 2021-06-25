# La pandemia por la ventana 


![Ilustración por Bernardo Dinamarca](https://github.com/pandemiaventana/pandemiaventana/blob/main/img/page/2_cover.png?raw=true)

La pandemia por la ventana es un sitio, realizado con formato de *libro* gracias a Jupyter Books, hecho por Alejandro Dinamarca, que recaba el trabajo de Numeral.lab en la Región de Tarapacá.

Favor, cualquier sugerencia o comentario, hacerlo llegar mediante [Issues de GitHub](https://github.com/pandemiaventana/pandemiaventana/issues/new).

## Funcionamiento

Básicamente, a través de Notebooks de Jupyter y un poco de Markdown. Python, por contraparte, genera los CSV, y Jupyter Books se encarga de generar la página web a partir de los Notebooks y el Markdown.

El despliegue del libro en [gh-pages](https://github.com/pandemiaventana/pandemiaventana/tree/gh-pages) se realiza cada vez que desencadeno un cambio en [main](https://github.com/pandemiaventana/pandemiaventana) a través del action [deploy-book](https://github.com/pandemiaventana/pandemiaventana/actions/workflows/book.yml).

## Estado

[![deploy-book](https://github.com/pandemiaventana/pandemiaventana/actions/workflows/book.yml/badge.svg)](https://github.com/pandemiaventana/pandemiaventana/actions/workflows/book.yml)

## Archivos CSV generados

Disponibles en [el siguiente enlace](https://github.com/pandemiaventana/pandemiaventana/tree/main/out/site/csv), los cuales se adjuntan a continuación:

<html><body><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><p>Encontré los <strong>siguientes archivos CSV</strong>:</p>
</div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><h3><a href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data1.csv">"data1.csv"</a></h3></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><p>Tiene las siguientes columnas (<strong>3</strong> sin el índice):</p>
</div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>&lt;class 'pandas.core.frame.DataFrame'&gt;
RangeIndex: 7 entries, 0 to 6
Data columns (total 4 columns):
 #   Column                                 Non-Null Count  Dtype  
---  ------                                 --------------  -----  
 0   Fecha                                  7 non-null      object 
 1   Casos nuevos últimos siete días        7 non-null      float64
 2   Recuperados nuevos últimos siete días  7 non-null      float64
 3   Fallecidos nuevos últimos siete días   7 non-null      float64
dtypes: float64(3), object(1)
memory usage: 765.0 bytes
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><hr/></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><h3><a href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data10.csv">"data10.csv"</a></h3></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><p>Tiene las siguientes columnas (<strong>8</strong> sin el índice):</p>
</div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>&lt;class 'pandas.core.frame.DataFrame'&gt;
RangeIndex: 479 entries, 0 to 478
Data columns (total 9 columns):
 #   Column                                  Non-Null Count  Dtype  
---  ------                                  --------------  -----  
 0   Fecha                                   479 non-null    object 
 1   Casos acumulados en Alto Hospicio       131 non-null    float64
 2   Casos acumulados en Camiña              131 non-null    float64
 3   Casos acumulados en Colchane            131 non-null    float64
 4   Casos acumulados en Huara               131 non-null    float64
 5   Casos acumulados en Iquique             131 non-null    float64
 6   Casos acumulados en Pica                131 non-null    float64
 7   Casos acumulados en Pozo Almonte        131 non-null    float64
 8   Casos acumulados en Comuna desconocida  105 non-null    float64
dtypes: float64(8), object(1)
memory usage: 61.4 KB
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><hr/></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><h3><a href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data11.csv">"data11.csv"</a></h3></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><p>Tiene las siguientes columnas (<strong>7</strong> sin el índice):</p>
</div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>&lt;class 'pandas.core.frame.DataFrame'&gt;
RangeIndex: 479 entries, 0 to 478
Data columns (total 8 columns):
 #   Column                     Non-Null Count  Dtype  
---  ------                     --------------  -----  
 0   Fecha                      479 non-null    object 
 1   Positividad Alto Hospicio  302 non-null    float64
 2   Positividad Camiña         302 non-null    float64
 3   Positividad Colchane       302 non-null    float64
 4   Positividad Huara          302 non-null    float64
 5   Positividad Iquique        302 non-null    float64
 6   Positividad Pica           302 non-null    float64
 7   Positividad Pozo Almonte   302 non-null    float64
dtypes: float64(7), object(1)
memory usage: 57.7 KB
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><hr/></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><h3><a href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data12.csv">"data12.csv"</a></h3></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><p>Tiene las siguientes columnas (<strong>8</strong> sin el índice):</p>
</div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>&lt;class 'pandas.core.frame.DataFrame'&gt;
RangeIndex: 479 entries, 0 to 478
Data columns (total 9 columns):
 #   Column                               Non-Null Count  Dtype  
---  ------                               --------------  -----  
 0   Fecha                                479 non-null    object 
 1   Casos activos en Alto Hospicio       125 non-null    float64
 2   Casos activos en Camiña              125 non-null    float64
 3   Casos activos en Colchane            125 non-null    float64
 4   Casos activos en Huara               125 non-null    float64
 5   Casos activos en Iquique             125 non-null    float64
 6   Casos activos en Pica                125 non-null    float64
 7   Casos activos en Pozo Almonte        125 non-null    float64
 8   Casos activos en Comuna desconocida  105 non-null    float64
dtypes: float64(8), object(1)
memory usage: 61.4 KB
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><hr/></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><h3><a href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data13.csv">"data13.csv"</a></h3></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><p>Tiene las siguientes columnas (<strong>9</strong> sin el índice):</p>
</div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>&lt;class 'pandas.core.frame.DataFrame'&gt;
RangeIndex: 479 entries, 0 to 478
Data columns (total 10 columns):
 #   Column                         Non-Null Count  Dtype  
---  ------                         --------------  -----  
 0   Fecha                          479 non-null    object 
 1   Fallecidos Alto Hospicio       375 non-null    float64
 2   Fallecidos Camiña              375 non-null    float64
 3   Fallecidos Colchane            375 non-null    float64
 4   Fallecidos Huara               375 non-null    float64
 5   Fallecidos Iquique             375 non-null    float64
 6   Fallecidos Pica                375 non-null    float64
 7   Fallecidos Pozo Almonte        375 non-null    float64
 8   Fallecidos Comuna desconocida  368 non-null    float64
 9   Fallecidos total comunal       375 non-null    float64
dtypes: float64(9), object(1)
memory usage: 65.1 KB
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><hr/></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><h3><a href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data14.csv">"data14.csv"</a></h3></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><p>Tiene las siguientes columnas (<strong>7</strong> sin el índice):</p>
</div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>&lt;class 'pandas.core.frame.DataFrame'&gt;
RangeIndex: 479 entries, 0 to 478
Data columns (total 8 columns):
 #   Column                                     Non-Null Count  Dtype  
---  ------                                     --------------  -----  
 0   Fecha                                      479 non-null    object 
 1   Fallecidos confirmados DEIS Alto Hospicio  288 non-null    float64
 2   Fallecidos confirmados DEIS Camiña         288 non-null    float64
 3   Fallecidos confirmados DEIS Colchane       288 non-null    float64
 4   Fallecidos confirmados DEIS Huara          288 non-null    float64
 5   Fallecidos confirmados DEIS Iquique        288 non-null    float64
 6   Fallecidos confirmados DEIS Pica           288 non-null    float64
 7   Fallecidos confirmados DEIS Pozo Almonte   288 non-null    float64
dtypes: float64(7), object(1)
memory usage: 57.7 KB
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><hr/></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><h3><a href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data15.csv">"data15.csv"</a></h3></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><p>Tiene las siguientes columnas (<strong>7</strong> sin el índice):</p>
</div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>&lt;class 'pandas.core.frame.DataFrame'&gt;
RangeIndex: 479 entries, 0 to 478
Data columns (total 8 columns):
 #   Column                                   Non-Null Count  Dtype  
---  ------                                   --------------  -----  
 0   Fecha                                    479 non-null    object 
 1   Fallecidos probables DEIS Alto Hospicio  288 non-null    float64
 2   Fallecidos probables DEIS Camiña         288 non-null    float64
 3   Fallecidos probables DEIS Colchane       288 non-null    float64
 4   Fallecidos probables DEIS Huara          288 non-null    float64
 5   Fallecidos probables DEIS Iquique        288 non-null    float64
 6   Fallecidos probables DEIS Pica           288 non-null    float64
 7   Fallecidos probables DEIS Pozo Almonte   288 non-null    float64
dtypes: float64(7), object(1)
memory usage: 57.7 KB
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><hr/></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><h3><a href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data16.csv">"data16.csv"</a></h3></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><p>Tiene las siguientes columnas (<strong>2</strong> sin el índice):</p>
</div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>&lt;class 'pandas.core.frame.DataFrame'&gt;
RangeIndex: 479 entries, 0 to 478
Data columns (total 3 columns):
 #   Column                                   Non-Null Count  Dtype  
---  ------                                   --------------  -----  
 0   Fecha                                    479 non-null    object 
 1   Media móvil real de ocupación UCI        429 non-null    float64
 2   Media móvil hipotética de ocupación UCI  431 non-null    float64
dtypes: float64(2), object(1)
memory usage: 39.0 KB
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><hr/></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><h3><a href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data17.csv">"data17.csv"</a></h3></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><p>Tiene las siguientes columnas (<strong>2</strong> sin el índice):</p>
</div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>&lt;class 'pandas.core.frame.DataFrame'&gt;
RangeIndex: 479 entries, 0 to 478
Data columns (total 3 columns):
 #   Column                   Non-Null Count  Dtype  
---  ------                   --------------  -----  
 0   Fecha                    479 non-null    object 
 1   Cupos en residencias     391 non-null    float64
 2   Usuarios en residencias  391 non-null    float64
dtypes: float64(2), object(1)
memory usage: 39.0 KB
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><hr/></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><h3><a href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data18.csv">"data18.csv"</a></h3></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><p>Tiene las siguientes columnas (<strong>2</strong> sin el índice):</p>
</div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>&lt;class 'pandas.core.frame.DataFrame'&gt;
RangeIndex: 479 entries, 0 to 478
Data columns (total 3 columns):
 #   Column                                        Non-Null Count  Dtype  
---  ------                                        --------------  -----  
 0   Fecha                                         479 non-null    object 
 1   PCR informados nuevos                         434 non-null    float64
 2   Media móvil semanal de PCR informados nuevos  427 non-null    float64
dtypes: float64(2), object(1)
memory usage: 39.0 KB
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><hr/></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><h3><a href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data19.csv">"data19.csv"</a></h3></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><p>Tiene las siguientes columnas (<strong>2</strong> sin el índice):</p>
</div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>&lt;class 'pandas.core.frame.DataFrame'&gt;
RangeIndex: 479 entries, 0 to 478
Data columns (total 3 columns):
 #   Column                                              Non-Null Count  Dtype  
---  ------                                              --------------  -----  
 0   Fecha                                               479 non-null    object 
 1   Antígenos informados nuevos                         20 non-null     float64
 2   Media móvil semanal de antígenos informados nuevos  14 non-null     float64
dtypes: float64(2), object(1)
memory usage: 39.0 KB
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><hr/></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><h3><a href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data2.csv">"data2.csv"</a></h3></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><p>Tiene las siguientes columnas (<strong>2</strong> sin el índice):</p>
</div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>&lt;class 'pandas.core.frame.DataFrame'&gt;
RangeIndex: 7 entries, 0 to 6
Data columns (total 3 columns):
 #   Column                                        Non-Null Count  Dtype  
---  ------                                        --------------  -----  
 0   Fecha                                         7 non-null      object 
 1   Casos activos confirmados últimos siete días  7 non-null      float64
 2   Casos activos probables últimos siete días    7 non-null      float64
dtypes: float64(2), object(1)
memory usage: 709.0 bytes
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><hr/></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><h3><a href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data20.csv">"data20.csv"</a></h3></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><p>Tiene las siguientes columnas (<strong>4</strong> sin el índice):</p>
</div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>&lt;class 'pandas.core.frame.DataFrame'&gt;
RangeIndex: 479 entries, 0 to 478
Data columns (total 5 columns):
 #   Column                        Non-Null Count  Dtype  
---  ------                        --------------  -----  
 0   Fecha                         479 non-null    object 
 1   Casos nuevos con síntomas     479 non-null    float64
 2   Casos nuevos sin síntomas     422 non-null    float64
 3   Casos nuevos por laboratorio  372 non-null    float64
 4   Casos nuevos por antígeno     120 non-null    float64
dtypes: float64(4), object(1)
memory usage: 46.4 KB
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><hr/></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><h3><a href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data21.csv">"data21.csv"</a></h3></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><p>Tiene las siguientes columnas (<strong>1</strong> sin el índice):</p>
</div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>&lt;class 'pandas.core.frame.DataFrame'&gt;
RangeIndex: 479 entries, 0 to 478
Data columns (total 2 columns):
 #   Column                             Non-Null Count  Dtype  
---  ------                             --------------  -----  
 0   Fecha                              479 non-null    object 
 1   Casos con sospecha de reinfección  120 non-null    float64
dtypes: float64(1), object(1)
memory usage: 35.2 KB
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><hr/></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><h3><a href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data22.csv">"data22.csv"</a></h3></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><p>Tiene las siguientes columnas (<strong>1</strong> sin el índice):</p>
</div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>&lt;class 'pandas.core.frame.DataFrame'&gt;
RangeIndex: 479 entries, 0 to 478
Data columns (total 2 columns):
 #   Column                                                        Non-Null Count  Dtype  
---  ------                                                        --------------  -----  
 0   Fecha                                                         479 non-null    object 
 1   Tasa de casos nuevos de casos nuevos por cien mil habitantes  473 non-null    float64
dtypes: float64(1), object(1)
memory usage: 35.2 KB
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><hr/></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><h3><a href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data23.csv">"data23.csv"</a></h3></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><p>Tiene las siguientes columnas (<strong>1</strong> sin el índice):</p>
</div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>&lt;class 'pandas.core.frame.DataFrame'&gt;
RangeIndex: 479 entries, 0 to 478
Data columns (total 2 columns):
 #   Column                                         Non-Null Count  Dtype  
---  ------                                         --------------  -----  
 0   Fecha                                          479 non-null    object 
 1   Mortalidad específica por cien mil habitantes  460 non-null    float64
dtypes: float64(1), object(1)
memory usage: 35.2 KB
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><hr/></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><h3><a href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data24.csv">"data24.csv"</a></h3></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><p>Tiene las siguientes columnas (<strong>7</strong> sin el índice):</p>
</div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>&lt;class 'pandas.core.frame.DataFrame'&gt;
RangeIndex: 479 entries, 0 to 478
Data columns (total 8 columns):
 #   Column                                         Non-Null Count  Dtype  
---  ------                                         --------------  -----  
 0   Fecha                                          479 non-null    object 
 1   Mortalidad especifica comunal Alto Hospicio *  288 non-null    float64
 2   Mortalidad especifica comunal Camiña *         288 non-null    float64
 3   Mortalidad especifica comunal Colchane *       288 non-null    float64
 4   Mortalidad especifica comunal Huara *          288 non-null    float64
 5   Mortalidad especifica comunal Iquique *        288 non-null    float64
 6   Mortalidad especifica comunal Pica *           288 non-null    float64
 7   Mortalidad especifica comunal Pozo Almonte *   288 non-null    float64
dtypes: float64(7), object(1)
memory usage: 57.7 KB
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><hr/></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><h3><a href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data25.csv">"data25.csv"</a></h3></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><p>Tiene las siguientes columnas (<strong>3</strong> sin el índice):</p>
</div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>&lt;class 'pandas.core.frame.DataFrame'&gt;
RangeIndex: 479 entries, 0 to 478
Data columns (total 4 columns):
 #   Column                            Non-Null Count  Dtype  
---  ------                            --------------  -----  
 0   Fecha                             479 non-null    object 
 1   Vacunados acumulados 1° dosis     182 non-null    float64
 2   Vacunados acumulados 2° dosis     182 non-null    float64
 3   Vacunados acumulados unica dosis  182 non-null    float64
dtypes: float64(3), object(1)
memory usage: 42.7 KB
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><hr/></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><h3><a href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data3.csv">"data3.csv"</a></h3></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><p>Tiene las siguientes columnas (<strong>3</strong> sin el índice):</p>
</div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>&lt;class 'pandas.core.frame.DataFrame'&gt;
RangeIndex: 479 entries, 0 to 478
Data columns (total 4 columns):
 #   Column                         Non-Null Count  Dtype  
---  ------                         --------------  -----  
 0   Fecha                          479 non-null    object 
 1   Casos nuevos históricos        479 non-null    float64
 2   Recuperados nuevos históricos  443 non-null    float64
 3   Fallecidos nuevos históricos   459 non-null    float64
dtypes: float64(3), object(1)
memory usage: 42.7 KB
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><hr/></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><h3><a href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data4.csv">"data4.csv"</a></h3></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><p>Tiene las siguientes columnas (<strong>2</strong> sin el índice):</p>
</div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>&lt;class 'pandas.core.frame.DataFrame'&gt;
RangeIndex: 369 entries, 0 to 368
Data columns (total 3 columns):
 #   Column                     Non-Null Count  Dtype  
---  ------                     --------------  -----  
 0   Fecha                      369 non-null    object 
 1   Casos activos confirmados  369 non-null    float64
 2   Casos activos probables    369 non-null    float64
dtypes: float64(2), object(1)
memory usage: 30.0 KB
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><hr/></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><h3><a href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data5.csv">"data5.csv"</a></h3></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><p>Tiene las siguientes columnas (<strong>4</strong> sin el índice):</p>
</div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>&lt;class 'pandas.core.frame.DataFrame'&gt;
RangeIndex: 479 entries, 0 to 478
Data columns (total 5 columns):
 #   Column                        Non-Null Count  Dtype  
---  ------                        --------------  -----  
 0   Fecha                         479 non-null    object 
 1   Casos confirmados acumulados  479 non-null    float64
 2   Casos recuperados acumulados  444 non-null    float64
 3   Casos activos confirmados     459 non-null    float64
 4   Casos fallecidos acumulados   460 non-null    float64
dtypes: float64(4), object(1)
memory usage: 46.4 KB
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><hr/></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><h3><a href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data6.csv">"data6.csv"</a></h3></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><p>Tiene las siguientes columnas (<strong>3</strong> sin el índice):</p>
</div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>&lt;class 'pandas.core.frame.DataFrame'&gt;
RangeIndex: 479 entries, 0 to 478
Data columns (total 4 columns):
 #   Column                                     Non-Null Count  Dtype  
---  ------                                     --------------  -----  
 0   Fecha                                      479 non-null    object 
 1   Media móvil semanal de casos nuevos        473 non-null    float64
 2   Media móvil semanal de recuperados nuevos  437 non-null    float64
 3   Media móvil semanal de fallecidos nuevos   453 non-null    float64
dtypes: float64(3), object(1)
memory usage: 42.7 KB
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><hr/></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><h3><a href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data7.csv">"data7.csv"</a></h3></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><p>Tiene las siguientes columnas (<strong>2</strong> sin el índice):</p>
</div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>&lt;class 'pandas.core.frame.DataFrame'&gt;
RangeIndex: 479 entries, 0 to 478
Data columns (total 3 columns):
 #   Column                     Non-Null Count  Dtype  
---  ------                     --------------  -----  
 0   Fecha                      479 non-null    object 
 1   Positividad diaria         430 non-null    float64
 2   Positividad media movil *  416 non-null    float64
dtypes: float64(2), object(1)
memory usage: 39.0 KB
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><hr/></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><h3><a href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data8.csv">"data8.csv"</a></h3></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><p>Tiene las siguientes columnas (<strong>3</strong> sin el índice):</p>
</div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>&lt;class 'pandas.core.frame.DataFrame'&gt;
RangeIndex: 479 entries, 0 to 478
Data columns (total 4 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   Fecha         479 non-null    object 
 1   Re regional   469 non-null    float64
 2   Re Iquique    466 non-null    float64
 3   Re Tamarugal  466 non-null    float64
dtypes: float64(3), object(1)
memory usage: 42.7 KB
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><hr/></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><h3><a href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data9.csv">"data9.csv"</a></h3></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><p>Tiene las siguientes columnas (<strong>2</strong> sin el índice):</p>
</div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>&lt;class 'pandas.core.frame.DataFrame'&gt;
RangeIndex: 479 entries, 0 to 478
Data columns (total 3 columns):
 #   Column                 Non-Null Count  Dtype  
---  ------                 --------------  -----  
 0   Fecha                  479 non-null    object 
 1   Crecimiento diario *   453 non-null    float64
 2   Crecimiento semanal *  452 non-null    float64
dtypes: float64(2), object(1)
memory usage: 39.0 KB
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><hr/></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><h3><a href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/numeralab.csv">"numeralab.csv"</a></h3></div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><p>Tiene las siguientes columnas (<strong>140</strong> sin el índice):</p>
</div></div><div class="output_area"><div class="run_this_cell"></div><div class="output_subarea output_text output_stream output_stdout" dir="auto"><pre>&lt;class 'pandas.core.frame.DataFrame'&gt;
RangeIndex: 479 entries, 0 to 478
Data columns (total 141 columns):
 #    Column                                         Non-Null Count  Dtype  
---   ------                                         --------------  -----  
 0    Fecha                                          479 non-null    object 
 1    Casos confirmados acumulados                   479 non-null    float64
 2    Casos recuperados acumulados                   444 non-null    float64
 3    Casos fallecidos acumulados                    460 non-null    float64
 4    Casos activos confirmados                      459 non-null    float64
 5    Casos activos probables                        369 non-null    float64
 6    Casos nuevos                                   479 non-null    float64
 7    Casos nuevos con sintomas                      479 non-null    float64
 8    Casos nuevos sin sintomas                      422 non-null    float64
 9    Casos nuevos por laboratorio                   372 non-null    float64
 10   Casos nuevos por antigeno                      120 non-null    float64
 11   Casos con sospecha de reinfeccion              120 non-null    float64
 12   Casos recuperados nuevos                       443 non-null    float64
 13   Casos fallecidos nuevos                        459 non-null    float64
 14   Antigenos informados nuevos                    20 non-null     float64
 15   Antigenos informados acumulados                20 non-null     float64
 16   PCR informados nuevos                          434 non-null    float64
 17   PCR informados acumulados                      434 non-null    float64
 18   Cupos en residencias                           391 non-null    float64
 19   Usuarios en residencias                        391 non-null    float64
 20   Numero de residencias                          391 non-null    float64
 21   UCI habilitadas                                435 non-null    float64
 22   UCI ocupadas por confirmados                   450 non-null    float64
 23   UCI ocupadas por no confirmados                435 non-null    float64
 24   UCI ocupacion media movil real                 429 non-null    float64
 25   Re regional                                    469 non-null    float64
 26   Re Iquique                                     466 non-null    float64
 27   Re Tamarugal                                   466 non-null    float64
 28   Positividad diaria                             430 non-null    float64
 29   Vacunados acumulados 1° dosis                  182 non-null    float64
 30   Vacunados acumulados 2° dosis                  182 non-null    float64
 31   Vacunados acumulados unica dosis               182 non-null    float64
 32   Casos acumulados en Alto Hospicio              131 non-null    float64
 33   Casos acumulados en Camiña                     131 non-null    float64
 34   Casos acumulados en Colchane                   131 non-null    float64
 35   Casos acumulados en Huara                      131 non-null    float64
 36   Casos acumulados en Iquique                    131 non-null    float64
 37   Casos acumulados en Pica                       131 non-null    float64
 38   Casos acumulados en Pozo Almonte               131 non-null    float64
 39   Casos acumulados en Comuna desconocida         105 non-null    float64
 40   Casos activos en Alto Hospicio                 125 non-null    float64
 41   Casos activos en Camiña                        125 non-null    float64
 42   Casos activos en Colchane                      125 non-null    float64
 43   Casos activos en Huara                         125 non-null    float64
 44   Casos activos en Iquique                       125 non-null    float64
 45   Casos activos en Pica                          125 non-null    float64
 46   Casos activos en Pozo Almonte                  125 non-null    float64
 47   Casos activos en Comuna desconocida            105 non-null    float64
 48   Paso a Paso Alto Hospicio                      332 non-null    float64
 49   Paso a Paso Camiña                             332 non-null    float64
 50   Paso a Paso Colchane                           332 non-null    float64
 51   Paso a Paso Huara                              332 non-null    float64
 52   Paso a Paso Iquique                            332 non-null    float64
 53   Paso a Paso Pica                               332 non-null    float64
 54   Paso a Paso Pozo Almonte                       332 non-null    float64
 55   Paso a Paso (dias) Alto Hospicio               332 non-null    float64
 56   Paso a Paso (dias) Camiña                      332 non-null    float64
 57   Paso a Paso (dias) Colchane                    332 non-null    float64
 58   Paso a Paso (dias) Huara                       332 non-null    float64
 59   Paso a Paso (dias) Iquique                     332 non-null    float64
 60   Paso a Paso (dias) Pica                        332 non-null    float64
 61   Paso a Paso (dias) Pozo Almonte                332 non-null    float64
 62   Movilidad Iquique                              435 non-null    float64
 63   Movilidad Pica                                 435 non-null    float64
 64   Movilidad Alto Hospicio                        435 non-null    float64
 65   Movilidad Pozo almonte                         435 non-null    float64
 66   Movilidad Huara                                435 non-null    float64
 67   Notificacion PCR Alto Hospicio                 302 non-null    float64
 68   Notificacion PCR Camiña                        302 non-null    float64
 69   Notificacion PCR Colchane                      302 non-null    float64
 70   Notificacion PCR Huara                         302 non-null    float64
 71   Notificacion PCR Iquique                       302 non-null    float64
 72   Notificacion PCR Pica                          302 non-null    float64
 73   Notificacion PCR Pozo Almonte                  302 non-null    float64
 74   BAC Alto Hospicio                              302 non-null    float64
 75   BAC Camiña                                     302 non-null    float64
 76   BAC Colchane                                   302 non-null    float64
 77   BAC Huara                                      302 non-null    float64
 78   BAC Iquique                                    302 non-null    float64
 79   BAC Pica                                       302 non-null    float64
 80   BAC Pozo Almonte                               302 non-null    float64
 81   Positividad Alto Hospicio                      302 non-null    float64
 82   Positividad Camiña                             302 non-null    float64
 83   Positividad Colchane                           302 non-null    float64
 84   Positividad Huara                              302 non-null    float64
 85   Positividad Iquique                            302 non-null    float64
 86   Positividad Pica                               302 non-null    float64
 87   Positividad Pozo Almonte                       302 non-null    float64
 88   Cobertura de testeo Alto Hospicio              302 non-null    float64
 89   Cobertura de testeo Camiña                     302 non-null    float64
 90   Cobertura de testeo Colchane                   302 non-null    float64
 91   Cobertura de testeo Huara                      302 non-null    float64
 92   Cobertura de testeo Iquique                    302 non-null    float64
 93   Cobertura de testeo Pica                       302 non-null    float64
 94   Cobertura de testeo Pozo Almonte               302                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   Fallecidos confirmados DEIS Colchane           288 non-null    float64
 114  Fallecidos confirmados DEIS Huara              288 non-null    float64
 115  Fallecidos confirmados DEIS Iquique            288 non-null    float64
 116  Fallecidos confirmados DEIS Pica               288 non-null    float64
 117  Fallecidos confirmados DEIS Pozo Almonte       288 non-null    float64
 118  Fallecidos probables DEIS Alto Hospicio        288 non-null    float64
 119  Fallecidos probables DEIS Camiña               288 non-null    float64
 120  Fallecidos probables DEIS Colchane             288 non-null    float64
 121  Fallecidos probables DEIS Huara                288 non-null    float64
 122  Fallecidos probables DEIS Iquique              288 non-null    float64
 123  Fallecidos probables DEIS Pica                 288 non-null    float64
 124  Fallecidos probables DEIS Pozo Almonte         288 non-null    float64
 125  Positividad media movil *                      416 non-null    float64
 126  Mortalidad especifica *                        460 non-null    float64
 127  Crecimiento semanal *                          452 non-null    float64
 128  Crecimiento diario *                           453 non-null    float64
 129  UCI ocupacion media movil aprox *              431 non-null    float64
 130  UCI error abs *                                429 non-null    float64
 131  Tasa casos nuevos *                            473 non-null    float64
 132  Positividad antigeno *                         20 non-null     float64
 133  Positividad antigeno media movil *             14 non-null     float64
 134  Mortalidad especifica comunal Alto Hospicio *  288 non-null    float64
 135  Mortalidad especifica comunal Camiña *         288 non-null    float64
 136  Mortalidad especifica comunal Colchane *       288 non-null    float64
 137  Mortalidad especifica comunal Huara *          288 non-null    float64
 138  Mortalidad especifica comunal Iquique *        288 non-null    float64
 139  Mortalidad especifica comunal Pica *           288 non-null    float64
 140  Mortalidad especifica comunal Pozo Almonte *   288 non-null    float64
dtypes: float64(140), object(1)
memory usage: 555.4 KB
</pre></div></div><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_markdown rendered_html" dir="auto"><hr></div></div>