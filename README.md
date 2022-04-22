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

<br><br><a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/numeralab.csv">"NUMERALAB.CSV"</a><br><br>Tiene las siguientes columnas (**156** sin el índice):<br><br>- Fecha con **781** datos válidos.<br><br>- Casos confirmados acumulados con **781** datos válidos.<br><br>- Casos recuperados acumulados con **746** datos válidos.<br><br>- Casos fallecidos acumulados con **762** datos válidos.<br><br>- Casos activos confirmados con **761** datos válidos.<br><br>- Casos activos probables con **671** datos válidos.<br><br>- Casos nuevos con **781** datos válidos.<br><br>- Casos nuevos con sintomas con **781** datos válidos.<br><br>- Casos nuevos sin sintomas con **724** datos válidos.<br><br>- Casos nuevos por laboratorio con **674** datos válidos.<br><br>- Casos nuevos por antigeno con **422** datos válidos.<br><br>- Casos con sospecha de reinfeccion con **422** datos válidos.<br><br>- Casos recuperados nuevos con **745** datos válidos.<br><br>- Casos fallecidos nuevos con **761** datos válidos.<br><br>- Antigenos informados nuevos con **322** datos válidos.<br><br>- Antigenos informados acumulados con **322** datos válidos.<br><br>- PCR informados nuevos con **736** datos válidos.<br><br>- PCR informados acumulados con **736** datos válidos.<br><br>- Cupos en residencias con **693** datos válidos.<br><br>- Usuarios en residencias con **693** datos válidos.<br><br>- Numero de residencias con **693** datos válidos.<br><br>- UCI habilitadas con **736** datos válidos.<br><br>- UCI ocupadas por confirmados con **752** datos válidos.<br><br>- UCI ocupadas por no confirmados con **736** datos válidos.<br><br>- UCI ocupacion media movil real con **730** datos válidos.<br><br>- Re regional con **769** datos válidos.<br><br>- Re Iquique con **769** datos válidos.<br><br>- Re Tamarugal con **769** datos válidos.<br><br>- Positividad diaria con **736** datos válidos.<br><br>- Vacunados acumulados 1° dosis con **484** datos válidos.<br><br>- Vacunados acumulados 2° dosis con **484** datos válidos.<br><br>- Vacunados acumulados unica dosis con **484** datos válidos.<br><br>- Vacunados acumulados dosis de refuerzo con **484** datos válidos.<br><br>- Vacunados acumulados 4° dosis con **484** datos válidos.<br><br>- Casos acumulados en Alto Hospicio con **217** datos válidos.<br><br>- Casos acumulados en Camiña con **217** datos válidos.<br><br>- Casos acumulados en Colchane con **217** datos válidos.<br><br>- Casos acumulados en Huara con **217** datos válidos.<br><br>- Casos acumulados en Iquique con **217** datos válidos.<br><br>- Casos acumulados en Pica con **217** datos válidos.<br><br>- Casos acumulados en Pozo Almonte con **217** datos válidos.<br><br>- Casos acumulados en Comuna desconocida con **191** datos válidos.<br><br>- Casos activos en Alto Hospicio con **211** datos válidos.<br><br>- Casos activos en Camiña con **211** datos válidos.<br><br>- Casos activos en Colchane con **211** datos válidos.<br><br>- Casos activos en Huara con **211** datos válidos.<br><br>- Casos activos en Iquique con **211** datos válidos.<br><br>- Casos activos en Pica con **211** datos válidos.<br><br>- Casos activos en Pozo Almonte con **211** datos válidos.<br><br>- Casos activos en Comuna desconocida con **191** datos válidos.<br><br>- Paso a Paso Alto Hospicio con **625** datos válidos.<br><br>- Paso a Paso Camiña con **625** datos válidos.<br><br>- Paso a Paso Colchane con **625** datos válidos.<br><br>- Paso a Paso Huara con **625** datos válidos.<br><br>- Paso a Paso Iquique con **625** datos válidos.<br><br>- Paso a Paso Pica con **625** datos válidos.<br><br>- Paso a Paso Pozo Almonte con **625** datos válidos.<br><br>- Paso a Paso (dias) Alto Hospicio con **633** datos válidos.<br><br>- Paso a Paso (dias) Camiña con **633** datos válidos.<br><br>- Paso a Paso (dias) Colchane con **633** datos válidos.<br><br>- Paso a Paso (dias) Huara con **633** datos válidos.<br><br>- Paso a Paso (dias) Iquique con **633** datos válidos.<br><br>- Paso a Paso (dias) Pica con **633** datos válidos.<br><br>- Paso a Paso (dias) Pozo Almonte con **633** datos válidos.<br><br>- Movilidad Iquique con **731** datos válidos.<br><br>- Movilidad Pica con **731** datos válidos.<br><br>- Movilidad Alto Hospicio con **731** datos válidos.<br><br>- Movilidad Pozo almonte con **731** datos válidos.<br><br>- Movilidad Huara con **731** datos válidos.<br><br>- Notificacion PCR Alto Hospicio con **604** datos válidos.<br><br>- Notificacion PCR Camiña con **604** datos válidos.<br><br>- Notificacion PCR Colchane con **604** datos válidos.<br><br>- Notificacion PCR Huara con **597** datos válidos.<br><br>- Notificacion PCR Iquique con **604** datos válidos.<br><br>- Notificacion PCR Pica con **604** datos válidos.<br><br>- Notificacion PCR Pozo Almonte con **604** datos válidos.<br><br>- BAC Alto Hospicio con **604** datos válidos.<br><br>- BAC Camiña con **604** datos válidos.<br><br>- BAC Colchane con **604** datos válidos.<br><br>- BAC Huara con **597** datos válidos.<br><br>- BAC Iquique con **604** datos válidos.<br><br>- BAC Pica con **604** datos válidos.<br><br>- BAC Pozo Almonte con **604** datos válidos.<br><br>- Positividad Alto Hospicio con **604** datos válidos.<br><br>- Positividad Camiña con **604** datos válidos.<br><br>- Positividad Colchane con **604** datos válidos.<br><br>- Positividad Huara con **597** datos válidos.<br><br>- Positividad Iquique con **604** datos válidos.<br><br>- Positividad Pica con **604** datos válidos.<br><br>- Positividad Pozo Almonte con **604** datos válidos.<br><br>- Cobertura de testeo Alto Hospicio con **604** datos válidos.<br><br>- Cobertura de testeo Camiña con **604** datos válidos.<br><br>- Cobertura de testeo Colchane con **604** datos válidos.<br><br>- Cobertura de testeo Huara con **597** datos válidos.<br><br>- Cobertura de testeo Iquique con **604** datos válidos.<br><br>- Cobertura de testeo Pica con **604** datos válidos.<br><br>- Cobertura de testeo Pozo Almonte con **604** datos válidos.<br><br>- Oportunidad en notificacion Alto Hospicio con **604** datos válidos.<br><br>- Oportunidad en notificacion Camiña con **604** datos válidos.<br><br>- Oportunidad en notificacion Colchane con **604** datos válidos.<br><br>- Oportunidad en notificacion Huara con **597** datos válidos.<br><br>- Oportunidad en notificacion Iquique con **604** datos válidos.<br><br>- Oportunidad en notificacion Pica con **604** datos válidos.<br><br>- Oportunidad en notificacion Pozo Almonte con **604** datos válidos.<br><br>- Fallecidos Alto Hospicio con **676** datos válidos.<br><br>- Fallecidos Camiña con **676** datos válidos.<br><br>- Fallecidos Colchane con **676** datos válidos.<br><br>- Fallecidos Huara con **676** datos válidos.<br><br>- Fallecidos Iquique con **676** datos válidos.<br><br>- Fallecidos Pica con **676** datos válidos.<br><br>- Fallecidos Pozo Almonte con **676** datos válidos.<br><br>- Fallecidos Comuna desconocida con **669** datos válidos.<br><br>- Fallecidos total comunal con **676** datos válidos.<br><br>- Fallecidos confirmados DEIS Alto Hospicio con **589** datos válidos.<br><br>- Fallecidos confirmados DEIS Camiña con **589** datos válidos.<br><br>- Fallecidos confirmados DEIS Colchane con **589** datos válidos.<br><br>- Fallecidos confirmados DEIS Huara con **589** datos válidos.<br><br>- Fallecidos confirmados DEIS Iquique con **589** datos válidos.<br><br>- Fallecidos confirmados DEIS Pica con **589** datos válidos.<br><br>- Fallecidos confirmados DEIS Pozo Almonte con **589** datos válidos.<br><br>- Fallecidos probables DEIS Alto Hospicio con **589** datos válidos.<br><br>- Fallecidos probables DEIS Camiña con **589** datos válidos.<br><br>- Fallecidos probables DEIS Colchane con **589** datos válidos.<br><br>- Fallecidos probables DEIS Huara con **589** datos válidos.<br><br>- Fallecidos probables DEIS Iquique con **589** datos válidos.<br><br>- Fallecidos probables DEIS Pica con **589** datos válidos.<br><br>- Fallecidos probables DEIS Pozo Almonte con **589** datos válidos.<br><br>- Incidencia regional estimada con **745** datos válidos.<br><br>- Incidencia Iquique estimada con **745** datos válidos.<br><br>- Incidencia Tamarugal estimada con **745** datos válidos.<br><br>- Tasa de casos nuevos Iquique estimada con **739** datos válidos.<br><br>- Tasa de casos nuevos Tamarugal estimada con **739** datos válidos.<br><br>- Incidencia acumulada Alto Hospicio con **217** datos válidos.<br><br>- Incidencia acumulada Camina con **217** datos válidos.<br><br>- Incidencia acumulada Colchane con **217** datos válidos.<br><br>- Incidencia acumulada Huara con **217** datos válidos.<br><br>- Incidencia acumulada Iquique con **217** datos válidos.<br><br>- Incidencia acumulada Pica con **217** datos válidos.<br><br>- Incidencia acumulada Pozo Almonte con **217** datos válidos.<br><br>- Incidencia acumulada regional con **217** datos válidos.<br><br>- Positividad media movil * con **718** datos válidos.<br><br>- Mortalidad especifica * con **762** datos válidos.<br><br>- Crecimiento semanal * con **761** datos válidos.<br><br>- Crecimiento diario * con **760** datos válidos.<br><br>- UCI ocupacion media movil aprox * con **733** datos válidos.<br><br>- UCI error abs * con **730** datos válidos.<br><br>- Tasa casos nuevos * con **775** datos válidos.<br><br>- Positividad antigeno * con **322** datos válidos.<br><br>- Positividad antigeno media movil * con **316** datos válidos.<br><br>- Mortalidad especifica comunal Alto Hospicio * con **589** datos válidos.<br><br>- Mortalidad especifica comunal Camiña * con **589** datos válidos.<br><br>- Mortalidad especifica comunal Colchane * con **589** datos válidos.<br><br>- Mortalidad especifica comunal Huara * con **589** datos válidos.<br><br>- Mortalidad especifica comunal Iquique * con **589** datos válidos.<br><br>- Mortalidad especifica comunal Pica * con **589** datos válidos.<br><br>- Mortalidad especifica comunal Pozo Almonte * con **589** datos válidos.<br><br>- Tasa de activos (incidencia) * con **761** datos válidos.<br><br><hr><br><br><a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data1.csv">"DATA1.CSV"</a><br><br>Tiene las siguientes columnas (**3** sin el índice):<br><br>- Fecha con **781** datos válidos.<br><br>- Casos nuevos históricos con **781** datos válidos.<br><br>- Recuperados nuevos históricos con **745** datos válidos.<br><br>- Fallecidos nuevos históricos con **761** datos válidos.<br><br><hr><br><br><a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data2.csv">"DATA2.CSV"</a><br><br>Tiene las siguientes columnas (**2** sin el índice):<br><br>- Fecha con **671** datos válidos.<br><br>- Casos activos confirmados con **671** datos válidos.<br><br>- Casos activos probables con **671** datos válidos.<br><br><hr><br><br><a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data3.csv">"DATA3.CSV"</a><br><br>Tiene las siguientes columnas (**4** sin el índice):<br><br>- Fecha con **781** datos válidos.<br><br>- Casos confirmados acumulados con **781** datos válidos.<br><br>- Casos recuperados acumulados con **746** datos válidos.<br><br>- Casos activos confirmados con **761** datos válidos.<br><br>- Casos fallecidos acumulados con **762** datos válidos.<br><br><hr><br><br><a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data4.csv">"DATA4.CSV"</a><br><br>Tiene las siguientes columnas (**3** sin el índice):<br><br>- Fecha con **781** datos válidos.<br><br>- Media móvil semanal de casos nuevos con **775** datos válidos.<br><br>- Media móvil semanal de recuperados nuevos con **739** datos válidos.<br><br>- Media móvil semanal de fallecidos nuevos con **755** datos válidos.<br><br><hr><br><br><a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data5.csv">"DATA5.CSV"</a><br><br>Tiene las siguientes columnas (**2** sin el índice):<br><br>- Fecha con **781** datos válidos.<br><br>- Positividad diaria con **736** datos válidos.<br><br>- Positividad media movil * con **718** datos válidos.<br><br><hr><br><br><a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data6.csv">"DATA6.CSV"</a><br><br>Tiene las siguientes columnas (**3** sin el índice):<br><br>- Fecha con **781** datos válidos.<br><br>- Re regional con **769** datos válidos.<br><br>- Re Iquique con **769** datos válidos.<br><br>- Re Tamarugal con **769** datos válidos.<br><br><hr><br><br><a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data7.csv">"DATA7.CSV"</a><br><br>Tiene las siguientes columnas (**8** sin el índice):<br><br>- Fecha con **781** datos válidos.<br><br>- Incidencia acumulada Alto Hospicio con **217** datos válidos.<br><br>- Incidencia acumulada Camina con **217** datos válidos.<br><br>- Incidencia acumulada Colchane con **217** datos válidos.<br><br>- Incidencia acumulada Huara con **217** datos válidos.<br><br>- Incidencia acumulada Iquique con **217** datos válidos.<br><br>- Incidencia acumulada Pica con **217** datos válidos.<br><br>- Incidencia acumulada Pozo Almonte con **217** datos válidos.<br><br>- Incidencia acumulada regional con **217** datos válidos.<br><br><hr><br><br><a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data8.csv">"DATA8.CSV"</a><br><br>Tiene las siguientes columnas (**3** sin el índice):<br><br>- Fecha con **781** datos válidos.<br><br>- Incidencia regional estimada con **745** datos válidos.<br><br>- Incidencia Iquique estimada con **745** datos válidos.<br><br>- Incidencia Tamarugal estimada con **745** datos válidos.<br><br><hr><br><br><a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data9.csv">"DATA9.CSV"</a><br><br>Tiene las siguientes columnas (**2** sin el índice):<br><br>- Fecha con **781** datos válidos.<br><br>- Tasa de casos nuevos Iquique estimada con **739** datos válidos.<br><br>- Tasa de casos nuevos Tamarugal estimada con **739** datos válidos.<br><br><hr><br><br><a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data10.csv">"DATA10.CSV"</a><br><br>Tiene las siguientes columnas (**2** sin el índice):<br><br>- Fecha con **781** datos válidos.<br><br>- Crecimiento diario * con **760** datos válidos.<br><br>- Crecimiento semanal * con **761** datos válidos.<br><br><hr><br><br><a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data11.csv">"DATA11.CSV"</a><br><br>Tiene las siguientes columnas (**8** sin el índice):<br><br>- Fecha con **781** datos válidos.<br><br>- Casos acumulados en Alto Hospicio con **217** datos válidos.<br><br>- Casos acumulados en Camiña con **217** datos válidos.<br><br>- Casos acumulados en Colchane con **217** datos válidos.<br><br>- Casos acumulados en Huara con **217** datos válidos.<br><br>- Casos acumulados en Iquique con **217** datos válidos.<br><br>- Casos acumulados en Pica con **217** datos válidos.<br><br>- Casos acumulados en Pozo Almonte con **217** datos válidos.<br><br>- Casos acumulados en Comuna desconocida con **191** datos válidos.<br><br><hr><br><br><a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data12.csv">"DATA12.CSV"</a><br><br>Tiene las siguientes columnas (**7** sin el índice):<br><br>- Fecha con **781** datos válidos.<br><br>- Positividad Alto Hospicio con **604** datos válidos.<br><br>- Positividad Camiña con **604** datos válidos.<br><br>- Positividad Colchane con **604** datos válidos.<br><br>- Positividad Huara con **597** datos válidos.<br><br>- Positividad Iquique con **604** datos válidos.<br><br>- Positividad Pica con **604** datos válidos.<br><br>- Positividad Pozo Almonte con **604** datos válidos.<br><br><hr><br><br><a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data13.csv">"DATA13.CSV"</a><br><br>Tiene las siguientes columnas (**9** sin el índice):<br><br>- Fecha con **781** datos válidos.<br><br>- Casos activos en Alto Hospicio con **211** datos válidos.<br><br>- Casos activos en Camiña con **211** datos válidos.<br><br>- Casos activos en Colchane con **211** datos válidos.<br><br>- Casos activos en Huara con **211** datos válidos.<br><br>- Casos activos en Iquique con **211** datos válidos.<br><br>- Casos activos en Pica con **211** datos válidos.<br><br>- Casos activos en Pozo Almonte con **211** datos válidos.<br><br>- Casos activos en Comuna desconocida con **191** datos válidos.<br><br>- Tasa de activos (incidencia) * con **761** datos válidos.<br><br><hr><br><br><a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data14.csv">"DATA14.CSV"</a><br><br>Tiene las siguientes columnas (**9** sin el índice):<br><br>- Fecha con **781** datos válidos.<br><br>- Fallecidos Alto Hospicio con **676** datos válidos.<br><br>- Fallecidos Camiña con **676** datos válidos.<br><br>- Fallecidos Colchane con **676** datos válidos.<br><br>- Fallecidos Huara con **676** datos válidos.<br><br>- Fallecidos Iquique con **676** datos válidos.<br><br>- Fallecidos Pica con **676** datos válidos.<br><br>- Fallecidos Pozo Almonte con **676** datos válidos.<br><br>- Fallecidos Comuna desconocida con **669** datos válidos.<br><br>- Fallecidos total comunal con **676** datos válidos.<br><br><hr><br><br><a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data15.csv">"DATA15.CSV"</a><br><br>Tiene las siguientes columnas (**7** sin el índice):<br><br>- Fecha con **781** datos válidos.<br><br>- Fallecidos confirmados DEIS Alto Hospicio con **589** datos válidos.<br><br>- Fallecidos confirmados DEIS Camiña con **589** datos válidos.<br><br>- Fallecidos confirmados DEIS Colchane con **589** datos válidos.<br><br>- Fallecidos confirmados DEIS Huara con **589** datos válidos.<br><br>- Fallecidos confirmados DEIS Iquique con **589** datos válidos.<br><br>- Fallecidos confirmados DEIS Pica con **589** datos válidos.<br><br>- Fallecidos confirmados DEIS Pozo Almonte con **589** datos válidos.<br><br><hr><br><br><a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data16.csv">"DATA16.CSV"</a><br><br>Tiene las siguientes columnas (**7** sin el índice):<br><br>- Fecha con **781** datos válidos.<br><br>- Fallecidos probables DEIS Alto Hospicio con **589** datos válidos.<br><br>- Fallecidos probables DEIS Camiña con **589** datos válidos.<br><br>- Fallecidos probables DEIS Colchane con **589** datos válidos.<br><br>- Fallecidos probables DEIS Huara con **589** datos válidos.<br><br>- Fallecidos probables DEIS Iquique con **589** datos válidos.<br><br>- Fallecidos probables DEIS Pica con **589** datos válidos.<br><br>- Fallecidos probables DEIS Pozo Almonte con **589** datos válidos.<br><br><hr><br><br><a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data17.csv">"DATA17.CSV"</a><br><br>Tiene las siguientes columnas (**2** sin el índice):<br><br>- Fecha con **781** datos válidos.<br><br>- Media móvil real de ocupación UCI con **730** datos válidos.<br><br>- Media móvil hipotética de ocupación UCI con **733** datos válidos.<br><br><hr><br><br><a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data18.csv">"DATA18.CSV"</a><br><br>Tiene las siguientes columnas (**2** sin el índice):<br><br>- Fecha con **781** datos válidos.<br><br>- Cupos en residencias con **693** datos válidos.<br><br>- Usuarios en residencias con **693** datos válidos.<br><br><hr><br><br><a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data19.csv">"DATA19.CSV"</a><br><br>Tiene las siguientes columnas (**2** sin el índice):<br><br>- Fecha con **781** datos válidos.<br><br>- PCR informados nuevos con **736** datos válidos.<br><br>- Media móvil semanal de PCR informados nuevos con **729** datos válidos.<br><br><hr><br><br><a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data20.csv">"DATA20.CSV"</a><br><br>Tiene las siguientes columnas (**2** sin el índice):<br><br>- Fecha con **781** datos válidos.<br><br>- Antígenos informados nuevos con **322** datos válidos.<br><br>- Media móvil semanal de antígenos informados nuevos con **316** datos válidos.<br><br><hr><br><br><a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data21.csv">"DATA21.CSV"</a><br><br>Tiene las siguientes columnas (**4** sin el índice):<br><br>- Fecha con **781** datos válidos.<br><br>- Casos nuevos con síntomas con **781** datos válidos.<br><br>- Casos nuevos sin síntomas con **724** datos válidos.<br><br>- Casos nuevos por laboratorio con **674** datos válidos.<br><br>- Casos nuevos por antígeno con **422** datos válidos.<br><br><hr><br><br><a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data22.csv">"DATA22.CSV"</a><br><br>Tiene las siguientes columnas (**1** sin el índice):<br><br>- Fecha con **781** datos válidos.<br><br>- Casos con sospecha de reinfección con **422** datos válidos.<br><br><hr><br><br><a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data23.csv">"DATA23.CSV"</a><br><br>Tiene las siguientes columnas (**1** sin el índice):<br><br>- Fecha con **781** datos válidos.<br><br>- Tasa de casos nuevos de casos nuevos por cien mil habitantes con **775** datos válidos.<br><br><hr><br><br><a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data24.csv">"DATA24.CSV"</a><br><br>Tiene las siguientes columnas (**1** sin el índice):<br><br>- Fecha con **781** datos válidos.<br><br>- Tasa de activos (incidencia) con **761** datos válidos.<br><br><hr><br><br><a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data25.csv">"DATA25.CSV"</a><br><br>Tiene las siguientes columnas (**1** sin el índice):<br><br>- Fecha con **781** datos válidos.<br><br>- Mortalidad específica por cien mil habitantes con **762** datos válidos.<br><br><hr><br><br><a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data26.csv">"DATA26.CSV"</a><br><br>Tiene las siguientes columnas (**7** sin el índice):<br><br>- Fecha con **781** datos válidos.<br><br>- Mortalidad especifica comunal Alto Hospicio * con **589** datos válidos.<br><br>- Mortalidad especifica comunal Camiña * con **589** datos válidos.<br><br>- Mortalidad especifica comunal Colchane * con **589** datos válidos.<br><br>- Mortalidad especifica comunal Huara * con **589** datos válidos.<br><br>- Mortalidad especifica comunal Iquique * con **589** datos válidos.<br><br>- Mortalidad especifica comunal Pica * con **589** datos válidos.<br><br>- Mortalidad especifica comunal Pozo Almonte * con **589** datos válidos.<br><br><hr><br><br><a style="font-size:18px" href="https://raw.githubusercontent.com/pandemiaventana/pandemiaventana/main/out/site/csv/data27.csv">"DATA27.CSV"</a><br><br>Tiene las siguientes columnas (**5** sin el índice):<br><br>- Fecha con **781** datos válidos.<br><br>- Vacunados acumulados 1° dosis con **484** datos válidos.<br><br>- Vacunados acumulados 2° dosis con **484** datos válidos.<br><br>- Vacunados acumulados unica dosis con **484** datos válidos.<br><br>- Vacunados acumulados dosis de refuerzo con **484** datos válidos.<br><br>- Vacunados acumulados 4° dosis con **484** datos válidos.<br><br><hr>