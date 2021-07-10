# La pandemia por la ventana 


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

<br><br><a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/numeralab.csv">"NUMERALAB.CSV"</a><br><br>Tiene las siguientes columnas (**140** sin el índice):<br><br>- Fecha con **495** datos válidos.<br><br>- Casos confirmados acumulados con **495** datos válidos.<br><br>- Casos recuperados acumulados con **460** datos válidos.<br><br>- Casos fallecidos acumulados con **476** datos válidos.<br><br>- Casos activos confirmados con **475** datos válidos.<br><br>- Casos activos probables con **385** datos válidos.<br><br>- Casos nuevos con **495** datos válidos.<br><br>- Casos nuevos con sintomas con **495** datos válidos.<br><br>- Casos nuevos sin sintomas con **438** datos válidos.<br><br>- Casos nuevos por laboratorio con **388** datos válidos.<br><br>- Casos nuevos por antigeno con **136** datos válidos.<br><br>- Casos con sospecha de reinfeccion con **136** datos válidos.<br><br>- Casos recuperados nuevos con **459** datos válidos.<br><br>- Casos fallecidos nuevos con **475** datos válidos.<br><br>- Antigenos informados nuevos con **36** datos válidos.<br><br>- Antigenos informados acumulados con **36** datos válidos.<br><br>- PCR informados nuevos con **450** datos válidos.<br><br>- PCR informados acumulados con **450** datos válidos.<br><br>- Cupos en residencias con **407** datos válidos.<br><br>- Usuarios en residencias con **407** datos válidos.<br><br>- Numero de residencias con **407** datos válidos.<br><br>- UCI habilitadas con **449** datos válidos.<br><br>- UCI ocupadas por confirmados con **466** datos válidos.<br><br>- UCI ocupadas por no confirmados con **449** datos válidos.<br><br>- UCI ocupacion media movil real con **443** datos válidos.<br><br>- Re regional con **483** datos válidos.<br><br>- Re Iquique con **483** datos válidos.<br><br>- Re Tamarugal con **483** datos válidos.<br><br>- Positividad diaria con **450** datos válidos.<br><br>- Vacunados acumulados 1° dosis con **197** datos válidos.<br><br>- Vacunados acumulados 2° dosis con **197** datos válidos.<br><br>- Vacunados acumulados unica dosis con **197** datos válidos.<br><br>- Casos acumulados en Alto Hospicio con **135** datos válidos.<br><br>- Casos acumulados en Camiña con **135** datos válidos.<br><br>- Casos acumulados en Colchane con **135** datos válidos.<br><br>- Casos acumulados en Huara con **135** datos válidos.<br><br>- Casos acumulados en Iquique con **135** datos válidos.<br><br>- Casos acumulados en Pica con **135** datos válidos.<br><br>- Casos acumulados en Pozo Almonte con **135** datos válidos.<br><br>- Casos acumulados en Comuna desconocida con **109** datos válidos.<br><br>- Casos activos en Alto Hospicio con **129** datos válidos.<br><br>- Casos activos en Camiña con **129** datos válidos.<br><br>- Casos activos en Colchane con **129** datos válidos.<br><br>- Casos activos en Huara con **129** datos válidos.<br><br>- Casos activos en Iquique con **129** datos válidos.<br><br>- Casos activos en Pica con **129** datos válidos.<br><br>- Casos activos en Pozo Almonte con **129** datos válidos.<br><br>- Casos activos en Comuna desconocida con **109** datos válidos.<br><br>- Paso a Paso Alto Hospicio con **346** datos válidos.<br><br>- Paso a Paso Camiña con **346** datos válidos.<br><br>- Paso a Paso Colchane con **346** datos válidos.<br><br>- Paso a Paso Huara con **346** datos válidos.<br><br>- Paso a Paso Iquique con **346** datos válidos.<br><br>- Paso a Paso Pica con **346** datos válidos.<br><br>- Paso a Paso Pozo Almonte con **346** datos válidos.<br><br>- Paso a Paso (dias) Alto Hospicio con **346** datos válidos.<br><br>- Paso a Paso (dias) Camiña con **346** datos válidos.<br><br>- Paso a Paso (dias) Colchane con **346** datos válidos.<br><br>- Paso a Paso (dias) Huara con **346** datos válidos.<br><br>- Paso a Paso (dias) Iquique con **346** datos válidos.<br><br>- Paso a Paso (dias) Pica con **346** datos válidos.<br><br>- Paso a Paso (dias) Pozo Almonte con **346** datos válidos.<br><br>- Movilidad Iquique con **463** datos válidos.<br><br>- Movilidad Pica con **463** datos válidos.<br><br>- Movilidad Alto Hospicio con **463** datos válidos.<br><br>- Movilidad Pozo almonte con **463** datos válidos.<br><br>- Movilidad Huara con **463** datos válidos.<br><br>- Notificacion PCR Alto Hospicio con **316** datos válidos.<br><br>- Notificacion PCR Camiña con **316** datos válidos.<br><br>- Notificacion PCR Colchane con **316** datos válidos.<br><br>- Notificacion PCR Huara con **316** datos válidos.<br><br>- Notificacion PCR Iquique con **316** datos válidos.<br><br>- Notificacion PCR Pica con **316** datos válidos.<br><br>- Notificacion PCR Pozo Almonte con **316** datos válidos.<br><br>- BAC Alto Hospicio con **316** datos válidos.<br><br>- BAC Camiña con **316** datos válidos.<br><br>- BAC Colchane con **316** datos válidos.<br><br>- BAC Huara con **316** datos válidos.<br><br>- BAC Iquique con **316** datos válidos.<br><br>- BAC Pica con **316** datos válidos.<br><br>- BAC Pozo Almonte con **316** datos válidos.<br><br>- Positividad Alto Hospicio con **316** datos válidos.<br><br>- Positividad Camiña con **316** datos válidos.<br><br>- Positividad Colchane con **316** datos válidos.<br><br>- Positividad Huara con **316** datos válidos.<br><br>- Positividad Iquique con **316** datos válidos.<br><br>- Positividad Pica con **316** datos válidos.<br><br>- Positividad Pozo Almonte con **316** datos válidos.<br><br>- Cobertura de testeo Alto Hospicio con **316** datos válidos.<br><br>- Cobertura de testeo Camiña con **316** datos válidos.<br><br>- Cobertura de testeo Colchane con **316** datos válidos.<br><br>- Cobertura de testeo Huara con **316** datos válidos.<br><br>- Cobertura de testeo Iquique con **316** datos válidos.<br><br>- Cobertura de testeo Pica con **316** datos válidos.<br><br>- Cobertura de testeo Pozo Almonte con **316** datos válidos.<br><br>- Oportunidad en notificacion Alto Hospicio con **316** datos válidos.<br><br>- Oportunidad en notificacion Camiña con **316** datos válidos.<br><br>- Oportunidad en notificacion Colchane con **309** datos válidos.<br><br>- Oportunidad en notificacion Huara con **316** datos válidos.<br><br>- Oportunidad en notificacion Iquique con **316** datos válidos.<br><br>- Oportunidad en notificacion Pica con **316** datos válidos.<br><br>- Oportunidad en notificacion Pozo Almonte con **316** datos válidos.<br><br>- Fallecidos Alto Hospicio con **389** datos válidos.<br><br>- Fallecidos Camiña con **389** datos válidos.<br><br>- Fallecidos Colchane con **389** datos válidos.<br><br>- Fallecidos Huara con **389** datos válidos.<br><br>- Fallecidos Iquique con **389** datos válidos.<br><br>- Fallecidos Pica con **389** datos válidos.<br><br>- Fallecidos Pozo Almonte con **389** datos válidos.<br><br>- Fallecidos Comuna desconocida con **382** datos válidos.<br><br>- Fallecidos total comunal con **389** datos válidos.<br><br>- Fallecidos confirmados DEIS Alto Hospicio con **302** datos válidos.<br><br>- Fallecidos confirmados DEIS Camiña con **302** datos válidos.<br><br>- Fallecidos confirmados DEIS Colchane con **302** datos válidos.<br><br>- Fallecidos confirmados DEIS Huara con **302** datos válidos.<br><br>- Fallecidos confirmados DEIS Iquique con **302** datos válidos.<br><br>- Fallecidos confirmados DEIS Pica con **302** datos válidos.<br><br>- Fallecidos confirmados DEIS Pozo Almonte con **302** datos válidos.<br><br>- Fallecidos probables DEIS Alto Hospicio con **302** datos válidos.<br><br>- Fallecidos probables DEIS Camiña con **302** datos válidos.<br><br>- Fallecidos probables DEIS Colchane con **302** datos válidos.<br><br>- Fallecidos probables DEIS Huara con **302** datos válidos.<br><br>- Fallecidos probables DEIS Iquique con **302** datos válidos.<br><br>- Fallecidos probables DEIS Pica con **302** datos válidos.<br><br>- Fallecidos probables DEIS Pozo Almonte con **302** datos válidos.<br><br>- Positividad media movil * con **432** datos válidos.<br><br>- Mortalidad especifica * con **476** datos válidos.<br><br>- Crecimiento semanal * con **475** datos válidos.<br><br>- Crecimiento diario * con **474** datos válidos.<br><br>- UCI ocupacion media movil aprox * con **447** datos válidos.<br><br>- UCI error abs * con **443** datos válidos.<br><br>- Tasa casos nuevos * con **489** datos válidos.<br><br>- Positividad antigeno * con **36** datos válidos.<br><br>- Positividad antigeno media movil * con **30** datos válidos.<br><br>- Mortalidad especifica comunal Alto Hospicio * con **302** datos válidos.<br><br>- Mortalidad especifica comunal Camiña * con **302** datos válidos.<br><br>- Mortalidad especifica comunal Colchane * con **302** datos válidos.<br><br>- Mortalidad especifica comunal Huara * con **302** datos válidos.<br><br>- Mortalidad especifica comunal Iquique * con **302** datos válidos.<br><br>- Mortalidad especifica comunal Pica * con **302** datos válidos.<br><br>- Mortalidad especifica comunal Pozo Almonte * con **302** datos válidos.<br><br><hr><br><br><a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data1.csv">"DATA1.CSV"</a><br><br>Tiene las siguientes columnas (**3** sin el índice):<br><br>- Fecha con **7** datos válidos.<br><br>- Casos nuevos últimos siete días con **7** datos válidos.<br><br>- Recuperados nuevos últimos siete días con **7** datos válidos.<br><br>- Fallecidos nuevos últimos siete días con **7** datos válidos.<br><br><hr><br><br><a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data2.csv">"DATA2.CSV"</a><br><br>Tiene las siguientes columnas (**2** sin el índice):<br><br>- Fecha con **7** datos válidos.<br><br>- Casos activos confirmados últimos siete días con **7** datos válidos.<br><br>- Casos activos probables últimos siete días con **7** datos válidos.<br><br><hr><br><br><a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data3.csv">"DATA3.CSV"</a><br><br>Tiene las siguientes columnas (**3** sin el índice):<br><br>- Fecha con **495** datos válidos.<br><br>- Casos nuevos históricos con **495** datos válidos.<br><br>- Recuperados nuevos históricos con **459** datos válidos.<br><br>- Fallecidos nuevos históricos con **475** datos válidos.<br><br><hr><br><br><a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data4.csv">"DATA4.CSV"</a><br><br>Tiene las siguientes columnas (**2** sin el índice):<br><br>- Fecha con **385** datos válidos.<br><br>- Casos activos confirmados con **385** datos válidos.<br><br>- Casos activos probables con **385** datos válidos.<br><br><hr><br><br><a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data5.csv">"DATA5.CSV"</a><br><br>Tiene las siguientes columnas (**4** sin el índice):<br><br>- Fecha con **495** datos válidos.<br><br>- Casos confirmados acumulados con **495** datos válidos.<br><br>- Casos recuperados acumulados con **460** datos válidos.<br><br>- Casos activos confirmados con **475** datos válidos.<br><br>- Casos fallecidos acumulados con **476** datos válidos.<br><br><hr><br><br><a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data6.csv">"DATA6.CSV"</a><br><br>Tiene las siguientes columnas (**3** sin el índice):<br><br>- Fecha con **495** datos válidos.<br><br>- Media móvil semanal de casos nuevos con **489** datos válidos.<br><br>- Media móvil semanal de recuperados nuevos con **453** datos válidos.<br><br>- Media móvil semanal de fallecidos nuevos con **469** datos válidos.<br><br><hr><br><br><a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data7.csv">"DATA7.CSV"</a><br><br>Tiene las siguientes columnas (**2** sin el índice):<br><br>- Fecha con **495** datos válidos.<br><br>- Positividad diaria con **450** datos válidos.<br><br>- Positividad media movil * con **432** datos válidos.<br><br><hr><br><br><a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data8.csv">"DATA8.CSV"</a><br><br>Tiene las siguientes columnas (**3** sin el índice):<br><br>- Fecha con **495** datos válidos.<br><br>- Re regional con **483** datos válidos.<br><br>- Re Iquique con **483** datos válidos.<br><br>- Re Tamarugal con **483** datos válidos.<br><br><hr><br><br><a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data9.csv">"DATA9.CSV"</a><br><br>Tiene las siguientes columnas (**2** sin el índice):<br><br>- Fecha con **495** datos válidos.<br><br>- Crecimiento diario * con **474** datos válidos.<br><br>- Crecimiento semanal * con **475** datos válidos.<br><br><hr><br><br><a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data10.csv">"DATA10.CSV"</a><br><br>Tiene las siguientes columnas (**8** sin el índice):<br><br>- Fecha con **495** datos válidos.<br><br>- Casos acumulados en Alto Hospicio con **135** datos válidos.<br><br>- Casos acumulados en Camiña con **135** datos válidos.<br><br>- Casos acumulados en Colchane con **135** datos válidos.<br><br>- Casos acumulados en Huara con **135** datos válidos.<br><br>- Casos acumulados en Iquique con **135** datos válidos.<br><br>- Casos acumulados en Pica con **135** datos válidos.<br><br>- Casos acumulados en Pozo Almonte con **135** datos válidos.<br><br>- Casos acumulados en Comuna desconocida con **109** datos válidos.<br><br><hr><br><br><a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data11.csv">"DATA11.CSV"</a><br><br>Tiene las siguientes columnas (**7** sin el índice):<br><br>- Fecha con **495** datos válidos.<br><br>- Positividad Alto Hospicio con **316** datos válidos.<br><br>- Positividad Camiña con **316** datos válidos.<br><br>- Positividad Colchane con **316** datos válidos.<br><br>- Positividad Huara con **316** datos válidos.<br><br>- Positividad Iquique con **316** datos válidos.<br><br>- Positividad Pica con **316** datos válidos.<br><br>- Positividad Pozo Almonte con **316** datos válidos.<br><br><hr><br><br><a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data12.csv">"DATA12.CSV"</a><br><br>Tiene las siguientes columnas (**8** sin el índice):<br><br>- Fecha con **495** datos válidos.<br><br>- Casos activos en Alto Hospicio con **129** datos válidos.<br><br>- Casos activos en Camiña con **129** datos válidos.<br><br>- Casos activos en Colchane con **129** datos válidos.<br><br>- Casos activos en Huara con **129** datos válidos.<br><br>- Casos activos en Iquique con **129** datos válidos.<br><br>- Casos activos en Pica con **129** datos válidos.<br><br>- Casos activos en Pozo Almonte con **129** datos válidos.<br><br>- Casos activos en Comuna desconocida con **109** datos válidos.<br><br><hr><br><br><a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data13.csv">"DATA13.CSV"</a><br><br>Tiene las siguientes columnas (**9** sin el índice):<br><br>- Fecha con **495** datos válidos.<br><br>- Fallecidos Alto Hospicio con **389** datos válidos.<br><br>- Fallecidos Camiña con **389** datos válidos.<br><br>- Fallecidos Colchane con **389** datos válidos.<br><br>- Fallecidos Huara con **389** datos válidos.<br><br>- Fallecidos Iquique con **389** datos válidos.<br><br>- Fallecidos Pica con **389** datos válidos.<br><br>- Fallecidos Pozo Almonte con **389** datos válidos.<br><br>- Fallecidos Comuna desconocida con **382** datos válidos.<br><br>- Fallecidos total comunal con **389** datos válidos.<br><br><hr><br><br><a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data14.csv">"DATA14.CSV"</a><br><br>Tiene las siguientes columnas (**7** sin el índice):<br><br>- Fecha con **495** datos válidos.<br><br>- Fallecidos confirmados DEIS Alto Hospicio con **302** datos válidos.<br><br>- Fallecidos confirmados DEIS Camiña con **302** datos válidos.<br><br>- Fallecidos confirmados DEIS Colchane con **302** datos válidos.<br><br>- Fallecidos confirmados DEIS Huara con **302** datos válidos.<br><br>- Fallecidos confirmados DEIS Iquique con **302** datos válidos.<br><br>- Fallecidos confirmados DEIS Pica con **302** datos válidos.<br><br>- Fallecidos confirmados DEIS Pozo Almonte con **302** datos válidos.<br><br><hr><br><br><a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data15.csv">"DATA15.CSV"</a><br><br>Tiene las siguientes columnas (**7** sin el índice):<br><br>- Fecha con **495** datos válidos.<br><br>- Fallecidos probables DEIS Alto Hospicio con **302** datos válidos.<br><br>- Fallecidos probables DEIS Camiña con **302** datos válidos.<br><br>- Fallecidos probables DEIS Colchane con **302** datos válidos.<br><br>- Fallecidos probables DEIS Huara con **302** datos válidos.<br><br>- Fallecidos probables DEIS Iquique con **302** datos válidos.<br><br>- Fallecidos probables DEIS Pica con **302** datos válidos.<br><br>- Fallecidos probables DEIS Pozo Almonte con **302** datos válidos.<br><br><hr><br><br><a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data16.csv">"DATA16.CSV"</a><br><br>Tiene las siguientes columnas (**2** sin el índice):<br><br>- Fecha con **495** datos válidos.<br><br>- Media móvil real de ocupación UCI con **443** datos válidos.<br><br>- Media móvil hipotética de ocupación UCI con **447** datos válidos.<br><br><hr><br><br><a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data17.csv">"DATA17.CSV"</a><br><br>Tiene las siguientes columnas (**2** sin el índice):<br><br>- Fecha con **495** datos válidos.<br><br>- Cupos en residencias con **407** datos válidos.<br><br>- Usuarios en residencias con **407** datos válidos.<br><br><hr><br><br><a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data18.csv">"DATA18.CSV"</a><br><br>Tiene las siguientes columnas (**2** sin el índice):<br><br>- Fecha con **495** datos válidos.<br><br>- PCR informados nuevos con **450** datos válidos.<br><br>- Media móvil semanal de PCR informados nuevos con **443** datos válidos.<br><br><hr><br><br><a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data19.csv">"DATA19.CSV"</a><br><br>Tiene las siguientes columnas (**2** sin el índice):<br><br>- Fecha con **495** datos válidos.<br><br>- Antígenos informados nuevos con **36** datos válidos.<br><br>- Media móvil semanal de antígenos informados nuevos con **30** datos válidos.<br><br><hr><br><br><a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data20.csv">"DATA20.CSV"</a><br><br>Tiene las siguientes columnas (**4** sin el índice):<br><br>- Fecha con **495** datos válidos.<br><br>- Casos nuevos con síntomas con **495** datos válidos.<br><br>- Casos nuevos sin síntomas con **438** datos válidos.<br><br>- Casos nuevos por laboratorio con **388** datos válidos.<br><br>- Casos nuevos por antígeno con **136** datos válidos.<br><br><hr><br><br><a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data21.csv">"DATA21.CSV"</a><br><br>Tiene las siguientes columnas (**1** sin el índice):<br><br>- Fecha con **495** datos válidos.<br><br>- Casos con sospecha de reinfección con **136** datos válidos.<br><br><hr><br><br><a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data22.csv">"DATA22.CSV"</a><br><br>Tiene las siguientes columnas (**1** sin el índice):<br><br>- Fecha con **495** datos válidos.<br><br>- Tasa de casos nuevos de casos nuevos por cien mil habitantes con **489** datos válidos.<br><br><hr><br><br><a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data23.csv">"DATA23.CSV"</a><br><br>Tiene las siguientes columnas (**1** sin el índice):<br><br>- Fecha con **495** datos válidos.<br><br>- Mortalidad específica por cien mil habitantes con **476** datos válidos.<br><br><hr><br><br><a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data24.csv">"DATA24.CSV"</a><br><br>Tiene las siguientes columnas (**7** sin el índice):<br><br>- Fecha con **495** datos válidos.<br><br>- Mortalidad especifica comunal Alto Hospicio * con **302** datos válidos.<br><br>- Mortalidad especifica comunal Camiña * con **302** datos válidos.<br><br>- Mortalidad especifica comunal Colchane * con **302** datos válidos.<br><br>- Mortalidad especifica comunal Huara * con **302** datos válidos.<br><br>- Mortalidad especifica comunal Iquique * con **302** datos válidos.<br><br>- Mortalidad especifica comunal Pica * con **302** datos válidos.<br><br>- Mortalidad especifica comunal Pozo Almonte * con **302** datos válidos.<br><br><hr><br><br><a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data25.csv">"DATA25.CSV"</a><br><br>Tiene las siguientes columnas (**3** sin el índice):<br><br>- Fecha con **495** datos válidos.<br><br>- Vacunados acumulados 1° dosis con **197** datos válidos.<br><br>- Vacunados acumulados 2° dosis con **197** datos válidos.<br><br>- Vacunados acumulados unica dosis con **197** datos válidos.<br><br><hr>