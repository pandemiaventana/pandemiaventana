# La pandemia por la ventana 


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

## DOI

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5044609.svg)](https://doi.org/10.5281/zenodo.5044609)

## Archivos CSV generados

Disponibles en [el siguiente enlace](https://github.com/pandemiaventana/pandemiaventana/tree/main/out/site/csv), los cuales se adjuntan a continuación:

["DATA1.CSV"](https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data1.csv)


Tiene las siguientes columnas (**3** sin el índice):



```
<class 'pandas.core.frame.DataFrame'>
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

```


---

["DATA10.CSV"](https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data10.csv)


Tiene las siguientes columnas (**8** sin el índice):



```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 486 entries, 0 to 485
Data columns (total 9 columns):
 #   Column                                  Non-Null Count  Dtype  
---  ------                                  --------------  -----  
 0   Fecha                                   486 non-null    object 
 1   Casos acumulados en Alto Hospicio       132 non-null    float64
 2   Casos acumulados en Camiña              132 non-null    float64
 3   Casos acumulados en Colchane            132 non-null    float64
 4   Casos acumulados en Huara               132 non-null    float64
 5   Casos acumulados en Iquique             132 non-null    float64
 6   Casos acumulados en Pica                132 non-null    float64
 7   Casos acumulados en Pozo Almonte        132 non-null    float64
 8   Casos acumulados en Comuna desconocida  106 non-null    float64
dtypes: float64(8), object(1)
memory usage: 62.3 KB

```


---

["DATA11.CSV"](https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data11.csv)


Tiene las siguientes columnas (**7** sin el índice):



```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 486 entries, 0 to 485
Data columns (total 8 columns):
 #   Column                     Non-Null Count  Dtype  
---  ------                     --------------  -----  
 0   Fecha                      486 non-null    object 
 1   Positividad Alto Hospicio  302 non-null    float64
 2   Positividad Camiña         302 non-null    float64
 3   Positividad Colchane       302 non-null    float64
 4   Positividad Huara          302 non-null    float64
 5   Positividad Iquique        302 non-null    float64
 6   Positividad Pica           302 non-null    float64
 7   Positividad Pozo Almonte   302 non-null    float64
dtypes: float64(7), object(1)
memory usage: 58.5 KB

```


---

["DATA12.CSV"](https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data12.csv)


Tiene las siguientes columnas (**8** sin el índice):



```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 486 entries, 0 to 485
Data columns (total 9 columns):
 #   Column                               Non-Null Count  Dtype  
---  ------                               --------------  -----  
 0   Fecha                                486 non-null    object 
 1   Casos activos en Alto Hospicio       126 non-null    float64
 2   Casos activos en Camiña              126 non-null    float64
 3   Casos activos en Colchane            126 non-null    float64
 4   Casos activos en Huara               126 non-null    float64
 5   Casos activos en Iquique             126 non-null    float64
 6   Casos activos en Pica                126 non-null    float64
 7   Casos activos en Pozo Almonte        126 non-null    float64
 8   Casos activos en Comuna desconocida  106 non-null    float64
dtypes: float64(8), object(1)
memory usage: 62.3 KB

```


---

["DATA13.CSV"](https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data13.csv)


Tiene las siguientes columnas (**9** sin el índice):



```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 486 entries, 0 to 485
Data columns (total 10 columns):
 #   Column                         Non-Null Count  Dtype  
---  ------                         --------------  -----  
 0   Fecha                          486 non-null    object 
 1   Fallecidos Alto Hospicio       379 non-null    float64
 2   Fallecidos Camiña              379 non-null    float64
 3   Fallecidos Colchane            379 non-null    float64
 4   Fallecidos Huara               379 non-null    float64
 5   Fallecidos Iquique             379 non-null    float64
 6   Fallecidos Pica                379 non-null    float64
 7   Fallecidos Pozo Almonte        379 non-null    float64
 8   Fallecidos Comuna desconocida  372 non-null    float64
 9   Fallecidos total comunal       379 non-null    float64
dtypes: float64(9), object(1)
memory usage: 66.1 KB

```


---

["DATA14.CSV"](https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data14.csv)


Tiene las siguientes columnas (**7** sin el índice):



```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 486 entries, 0 to 485
Data columns (total 8 columns):
 #   Column                                     Non-Null Count  Dtype  
---  ------                                     --------------  -----  
 0   Fecha                                      486 non-null    object 
 1   Fallecidos confirmados DEIS Alto Hospicio  292 non-null    float64
 2   Fallecidos confirmados DEIS Camiña         292 non-null    float64
 3   Fallecidos confirmados DEIS Colchane       292 non-null    float64
 4   Fallecidos confirmados DEIS Huara          292 non-null    float64
 5   Fallecidos confirmados DEIS Iquique        292 non-null    float64
 6   Fallecidos confirmados DEIS Pica           292 non-null    float64
 7   Fallecidos confirmados DEIS Pozo Almonte   292 non-null    float64
dtypes: float64(7), object(1)
memory usage: 58.5 KB

```


---

["DATA15.CSV"](https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data15.csv)


Tiene las siguientes columnas (**7** sin el índice):



```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 486 entries, 0 to 485
Data columns (total 8 columns):
 #   Column                                   Non-Null Count  Dtype  
---  ------                                   --------------  -----  
 0   Fecha                                    486 non-null    object 
 1   Fallecidos probables DEIS Alto Hospicio  292 non-null    float64
 2   Fallecidos probables DEIS Camiña         292 non-null    float64
 3   Fallecidos probables DEIS Colchane       292 non-null    float64
 4   Fallecidos probables DEIS Huara          292 non-null    float64
 5   Fallecidos probables DEIS Iquique        292 non-null    float64
 6   Fallecidos probables DEIS Pica           292 non-null    float64
 7   Fallecidos probables DEIS Pozo Almonte   292 non-null    float64
dtypes: float64(7), object(1)
memory usage: 58.5 KB

```


---

["DATA16.CSV"](https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data16.csv)


Tiene las siguientes columnas (**2** sin el índice):



```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 486 entries, 0 to 485
Data columns (total 3 columns):
 #   Column                                   Non-Null Count  Dtype  
---  ------                                   --------------  -----  
 0   Fecha                                    486 non-null    object 
 1   Media móvil real de ocupación UCI        436 non-null    float64
 2   Media móvil hipotética de ocupación UCI  437 non-null    float64
dtypes: float64(2), object(1)
memory usage: 39.5 KB

```


---

["DATA17.CSV"](https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data17.csv)


Tiene las siguientes columnas (**2** sin el índice):



```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 486 entries, 0 to 485
Data columns (total 3 columns):
 #   Column                   Non-Null Count  Dtype  
---  ------                   --------------  -----  
 0   Fecha                    486 non-null    object 
 1   Cupos en residencias     397 non-null    float64
 2   Usuarios en residencias  397 non-null    float64
dtypes: float64(2), object(1)
memory usage: 39.5 KB

```


---

["DATA18.CSV"](https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data18.csv)


Tiene las siguientes columnas (**2** sin el índice):



```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 486 entries, 0 to 485
Data columns (total 3 columns):
 #   Column                                        Non-Null Count  Dtype  
---  ------                                        --------------  -----  
 0   Fecha                                         486 non-null    object 
 1   PCR informados nuevos                         440 non-null    float64
 2   Media móvil semanal de PCR informados nuevos  433 non-null    float64
dtypes: float64(2), object(1)
memory usage: 39.5 KB

```


---

["DATA19.CSV"](https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data19.csv)


Tiene las siguientes columnas (**2** sin el índice):



```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 486 entries, 0 to 485
Data columns (total 3 columns):
 #   Column                                              Non-Null Count  Dtype  
---  ------                                              --------------  -----  
 0   Fecha                                               486 non-null    object 
 1   Antígenos informados nuevos                         26 non-null     float64
 2   Media móvil semanal de antígenos informados nuevos  20 non-null     float64
dtypes: float64(2), object(1)
memory usage: 39.5 KB

```


---

["DATA2.CSV"](https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data2.csv)


Tiene las siguientes columnas (**2** sin el índice):



```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 7 entries, 0 to 6
Data columns (total 3 columns):
 #   Column                                        Non-Null Count  Dtype  
---  ------                                        --------------  -----  
 0   Fecha                                         7 non-null      object 
 1   Casos activos confirmados últimos siete días  7 non-null      float64
 2   Casos activos probables últimos siete días    7 non-null      float64
dtypes: float64(2), object(1)
memory usage: 709.0 bytes

```


---

["DATA20.CSV"](https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data20.csv)


Tiene las siguientes columnas (**4** sin el índice):



```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 486 entries, 0 to 485
Data columns (total 5 columns):
 #   Column                        Non-Null Count  Dtype  
---  ------                        --------------  -----  
 0   Fecha                         486 non-null    object 
 1   Casos nuevos con síntomas     485 non-null    float64
 2   Casos nuevos sin síntomas     428 non-null    float64
 3   Casos nuevos por laboratorio  378 non-null    float64
 4   Casos nuevos por antígeno     126 non-null    float64
dtypes: float64(4), object(1)
memory usage: 47.1 KB

```


---

["DATA21.CSV"](https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data21.csv)


Tiene las siguientes columnas (**1** sin el índice):



```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 486 entries, 0 to 485
Data columns (total 2 columns):
 #   Column                             Non-Null Count  Dtype  
---  ------                             --------------  -----  
 0   Fecha                              486 non-null    object 
 1   Casos con sospecha de reinfección  126 non-null    float64
dtypes: float64(1), object(1)
memory usage: 35.7 KB

```


---

["DATA22.CSV"](https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data22.csv)


Tiene las siguientes columnas (**1** sin el índice):



```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 486 entries, 0 to 485
Data columns (total 2 columns):
 #   Column                                                        Non-Null Count  Dtype  
---  ------                                                        --------------  -----  
 0   Fecha                                                         486 non-null    object 
 1   Tasa de casos nuevos de casos nuevos por cien mil habitantes  479 non-null    float64
dtypes: float64(1), object(1)
memory usage: 35.7 KB

```


---

["DATA23.CSV"](https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data23.csv)


Tiene las siguientes columnas (**1** sin el índice):



```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 486 entries, 0 to 485
Data columns (total 2 columns):
 #   Column                                         Non-Null Count  Dtype  
---  ------                                         --------------  -----  
 0   Fecha                                          486 non-null    object 
 1   Mortalidad específica por cien mil habitantes  466 non-null    float64
dtypes: float64(1), object(1)
memory usage: 35.7 KB

```


---

["DATA24.CSV"](https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data24.csv)


Tiene las siguientes columnas (**7** sin el índice):



```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 486 entries, 0 to 485
Data columns (total 8 columns):
 #   Column                                         Non-Null Count  Dtype  
---  ------                                         --------------  -----  
 0   Fecha                                          486 non-null    object 
 1   Mortalidad especifica comunal Alto Hospicio *  292 non-null    float64
 2   Mortalidad especifica comunal Camiña *         292 non-null    float64
 3   Mortalidad especifica comunal Colchane *       292 non-null    float64
 4   Mortalidad especifica comunal Huara *          292 non-null    float64
 5   Mortalidad especifica comunal Iquique *        292 non-null    float64
 6   Mortalidad especifica comunal Pica *           292 non-null    float64
 7   Mortalidad especifica comunal Pozo Almonte *   292 non-null    float64
dtypes: float64(7), object(1)
memory usage: 58.5 KB

```


---

["DATA25.CSV"](https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data25.csv)


Tiene las siguientes columnas (**3** sin el índice):



```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 486 entries, 0 to 485
Data columns (total 4 columns):
 #   Column                            Non-Null Count  Dtype  
---  ------                            --------------  -----  
 0   Fecha                             486 non-null    object 
 1   Vacunados acumulados 1° dosis     188 non-null    float64
 2   Vacunados acumulados 2° dosis     188 non-null    float64
 3   Vacunados acumulados unica dosis  188 non-null    float64
dtypes: float64(3), object(1)
memory usage: 43.3 KB

```


---

["DATA3.CSV"](https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data3.csv)


Tiene las siguientes columnas (**3** sin el índice):



```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 486 entries, 0 to 485
Data columns (total 4 columns):
 #   Column                         Non-Null Count  Dtype  
---  ------                         --------------  -----  
 0   Fecha                          486 non-null    object 
 1   Casos nuevos históricos        485 non-null    float64
 2   Recuperados nuevos históricos  449 non-null    float64
 3   Fallecidos nuevos históricos   465 non-null    float64
dtypes: float64(3), object(1)
memory usage: 43.3 KB

```


---

["DATA4.CSV"](https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data4.csv)


Tiene las siguientes columnas (**2** sin el índice):



```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 376 entries, 0 to 375
Data columns (total 3 columns):
 #   Column                     Non-Null Count  Dtype  
---  ------                     --------------  -----  
 0   Fecha                      376 non-null    object 
 1   Casos activos confirmados  375 non-null    float64
 2   Casos activos probables    375 non-null    float64
dtypes: float64(2), object(1)
memory usage: 30.6 KB

```


---

["DATA5.CSV"](https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data5.csv)


Tiene las siguientes columnas (**4** sin el índice):



```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 486 entries, 0 to 485
Data columns (total 5 columns):
 #   Column                        Non-Null Count  Dtype  
---  ------                        --------------  -----  
 0   Fecha                         486 non-null    object 
 1   Casos confirmados acumulados  485 non-null    float64
 2   Casos recuperados acumulados  450 non-null    float64
 3   Casos activos confirmados     465 non-null    float64
 4   Casos fallecidos acumulados   466 non-null    float64
dtypes: float64(4), object(1)
memory usage: 47.1 KB

```


---

["DATA6.CSV"](https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data6.csv)


Tiene las siguientes columnas (**3** sin el índice):



```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 486 entries, 0 to 485
Data columns (total 4 columns):
 #   Column                                     Non-Null Count  Dtype  
---  ------                                     --------------  -----  
 0   Fecha                                      486 non-null    object 
 1   Media móvil semanal de casos nuevos        479 non-null    float64
 2   Media móvil semanal de recuperados nuevos  443 non-null    float64
 3   Media móvil semanal de fallecidos nuevos   459 non-null    float64
dtypes: float64(3), object(1)
memory usage: 43.3 KB

```


---

["DATA7.CSV"](https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data7.csv)


Tiene las siguientes columnas (**2** sin el índice):



```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 486 entries, 0 to 485
Data columns (total 3 columns):
 #   Column                     Non-Null Count  Dtype  
---  ------                     --------------  -----  
 0   Fecha                      486 non-null    object 
 1   Positividad diaria         440 non-null    float64
 2   Positividad media movil *  422 non-null    float64
dtypes: float64(2), object(1)
memory usage: 39.5 KB

```


---

["DATA8.CSV"](https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data8.csv)


Tiene las siguientes columnas (**3** sin el índice):



```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 486 entries, 0 to 485
Data columns (total 4 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   Fecha         486 non-null    object 
 1   Re regional   476 non-null    float64
 2   Re Iquique    469 non-null    float64
 3   Re Tamarugal  469 non-null    float64
dtypes: float64(3), object(1)
memory usage: 43.3 KB

```


---

["DATA9.CSV"](https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data9.csv)


Tiene las siguientes columnas (**2** sin el índice):



```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 486 entries, 0 to 485
Data columns (total 3 columns):
 #   Column                 Non-Null Count  Dtype  
---  ------                 --------------  -----  
 0   Fecha                  486 non-null    object 
 1   Crecimiento diario *   464 non-null    float64
 2   Crecimiento semanal *  465 non-null    float64
dtypes: float64(2), object(1)
memory usage: 39.5 KB

```


---

["NUMERALAB.CSV"](https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/numeralab.csv)


Tiene las siguientes columnas (**140** sin el índice):



```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 486 entries, 0 to 485
Data columns (total 141 columns):
 #    Column                                         Non-Null Count  Dtype  
---   ------                                         --------------  -----  
 0    Fecha                                          486 non-null    object 
 1    Casos confirmados acumulados                   485 non-null    float64
 2    Casos recuperados acumulados                   450 non-null    float64
 3    Casos fallecidos acumulados                    466 non-null    float64
 4    Casos activos confirmados                      465 non-null    float64
 5    Casos activos probables                        375 non-null    float64
 6    Casos nuevos                                   485 non-null    float64
 7    Casos nuevos con sintomas                      485 non-null    float64
 8    Casos nuevos sin sintomas                      428 non-null    float64
 9    Casos nuevos por laboratorio                   378 non-null    float64
 10   Casos nuevos por antigeno                      126 non-null    float64
 11   Casos con sospecha de reinfeccion              126 non-null    float64
 12   Casos recuperados nuevos                       449 non-null    float64
 13   Casos fallecidos nuevos                        465 non-null    float64
 14   Antigenos informados nuevos                    26 non-null     float64
 15   Antigenos informados acumulados                26 non-null     float64
 16   PCR informados nuevos                          440 non-null    float64
 17   PCR informados acumulados                      440 non-null    float64
 18   Cupos en residencias                           397 non-null    float64
 19   Usuarios en residencias                        397 non-null    float64
 20   Numero de residencias                          397 non-null    float64
 21   UCI habilitadas                                442 non-null    float64
 22   UCI ocupadas por confirmados                   456 non-null    float64
 23   UCI ocupadas por no confirmados                442 non-null    float64
 24   UCI ocupacion media movil real                 436 non-null    float64
 25   Re regional                                    476 non-null    float64
 26   Re Iquique                                     469 non-null    float64
 27   Re Tamarugal                                   469 non-null    float64
 28   Positividad diaria                             440 non-null    float64
 29   Vacunados acumulados 1° dosis                  188 non-null    float64
 30   Vacunados acumulados 2° dosis                  188 non-null    float64
 31   Vacunados acumulados unica dosis               188 non-null    float64
 32   Casos acumulados en Alto Hospicio              132 non-null    float64
 33   Casos acumulados en Camiña                     132 non-null    float64
 34   Casos acumulados en Colchane                   132 non-null    float64
 35   Casos acumulados en Huara                      132 non-null    float64
 36   Casos acumulados en Iquique                    132 non-null    float64
 37   Casos acumulados en Pica                       132 non-null    float64
 38   Casos acumulados en Pozo Almonte               132 non-null    float64
 39   Casos acumulados en Comuna desconocida         106 non-null    float64
 40   Casos activos en Alto Hospicio                 126 non-null    float64
 41   Casos activos en Camiña                        126 non-null    float64
 42   Casos activos en Colchane                      126 non-null    float64
 43   Casos activos en Huara                         126 non-null    float64
 44   Casos activos en Iquique                       126 non-null    float64
 45   Casos activos en Pica                          126 non-null    float64
 46   Casos activos en Pozo Almonte                  126 non-null    float64
 47   Casos activos en Comuna desconocida            106 non-null    float64
 48   Paso a Paso Alto Hospicio                      339 non-null    float64
 49   Paso a Paso Camiña                             339 non-null    float64
 50   Paso a Paso Colchane                           339 non-null    float64
 51   Paso a Paso Huara                              339 non-null    float64
 52   Paso a Paso Iquique                            339 non-null    float64
 53   Paso a Paso Pica                               339 non-null    float64
 54   Paso a Paso Pozo Almonte                       339 non-null    float64
 55   Paso a Paso (dias) Alto Hospicio               339 non-null    float64
 56   Paso a Paso (dias) Camiña                      339 non-null    float64
 57   Paso a Paso (dias) Colchane                    339 non-null    float64
 58   Paso a Paso (dias) Huara                       339 non-null    float64
 59   Paso a Paso (dias) Iquique                     339 non-null    float64
 60   Paso a Paso (dias) Pica                        339 non-null    float64
 61   Paso a Paso (dias) Pozo Almonte                339 non-null    float64
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
 94   Cobertura de testeo Pozo Almonte               302 non-null    float64
 95   Oportunidad en notificacion Alto Hospicio      302 non-null    float64
 96   Oportunidad en notificacion Camiña             302 non-null    float64
 97   Oportunidad en notificacion Colchane           288 non-null    float64
 98   Oportunidad en notificacion Huara              302 non-null    float64
 99   Oportunidad en notificacion Iquique            302 non-null    float64
 100  Oportunidad en notificacion Pica               302 non-null    float64
 101  Oportunidad en notificacion Pozo Almonte       302 non-null    float64
 102  Fallecidos Alto Hospicio                       379 non-null    float64
 103  Fallecidos Camiña                              379 non-null    float64
 104  Fallecidos Colchane                            379 non-null    float64
 105  Fallecidos Huara                               379 non-null    float64
 106  Fallecidos Iquique                             379 non-null    float64
 107  Fallecidos Pica                                379 non-null    float64
 108  Fallecidos Pozo Almonte                        379 non-null    float64
 109  Fallecidos Comuna desconocida                  372 non-null    float64
 110  Fallecidos total comunal                       379 non-null    float64
 111  Fallecidos confirmados DEIS Alto Hospicio      292 non-null    float64
 112  Fallecidos confirmados DEIS Camiña             292 non-null    float64
 113  Fallecidos confirmados DEIS Colchane           292 non-null    float64
 114  Fallecidos confirmados DEIS Huara              292 non-null    float64
 115  Fallecidos confirmados DEIS Iquique            292 non-null    float64
 116  Fallecidos confirmados DEIS Pica               292 non-null    float64
 117  Fallecidos confirmados DEIS Pozo Almonte       292 non-null    float64
 118  Fallecidos probables DEIS Alto Hospicio        292 non-null    float64
 119  Fallecidos probables DEIS Camiña               292 non-null    float64
 120  Fallecidos probables DEIS Colchane             292 non-null    float64
 121  Fallecidos probables DEIS Huara                292 non-null    float64
 122  Fallecidos probables DEIS Iquique              292 non-null    float64
 123  Fallecidos probables DEIS Pica                 292 non-null    float64
 124  Fallecidos probables DEIS Pozo Almonte         292 non-null    float64
 125  Positividad media movil *                      422 non-null    float64
 126  Mortalidad especifica *                        466 non-null    float64
 127  Crecimiento semanal *                          465 non-null    float64
 128  Crecimiento diario *                           464 non-null    float64
 129  UCI ocupacion media movil aprox *              437 non-null    float64
 130  UCI error abs *                                436 non-null    float64
 131  Tasa casos nuevos *                            479 non-null    float64
 132  Positividad antigeno *                         26 non-null     float64
 133  Positividad antigeno media movil *             20 non-null     float64
 134  Mortalidad especifica comunal Alto Hospicio *  292 non-null    float64
 135  Mortalidad especifica comunal Camiña *         292 non-null    float64
 136  Mortalidad especifica comunal Colchane *       292 non-null    float64
 137  Mortalidad especifica comunal Huara *          292 non-null    float64
 138  Mortalidad especifica comunal Iquique *        292 non-null    float64
 139  Mortalidad especifica comunal Pica *           292 non-null    float64
 140  Mortalidad especifica comunal Pozo Almonte *   292 non-null    float64
dtypes: float64(140), object(1)
memory usage: 563.5 KB

```


---

