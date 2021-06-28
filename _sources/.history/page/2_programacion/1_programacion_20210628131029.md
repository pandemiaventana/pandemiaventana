# Funcionamiento

El libro es dinámico. Es decir, se actualiza de forma constante.

## ¿Cómo lo hace?

A través de Notebooks de Jupyter, un poco de Markdown y GitHub Actions:

- El script realizado en Jupyter Notebook - *con Python* - genera los archivos de datos, infografías y sitios.

- Jupyter Books se encarga de generar la página web a partir de los Notebooks de Jupyter y Markdown.

- GitHub Actions ejecuta, iteradamente, los procesos anteriores.

## Ejecución de actualizaciones

El despliegue del libro en [gh-pages](https://github.com/pandemiaventana/pandemiaventana/tree/gh-pages) se realiza con GitHub Actions cada vez que:

- Desencadeno un cambio en el repositorio. Puntualmente, en [main](https://github.com/pandemiaventana/pandemiaventana).

- Se cumple una hora desde las 10:30 hrs. hasta las 19:30 hrs. (horario de Santiago de Chile). *El repositorio duerme desde las 19:31 hrs. hasta las 11:29 hrs. del próximo día*.

La ejecución se realiza a través del action [actualiza_libro](https://github.com/pandemiaventana/pandemiaventana/actions/workflows/book.yml).

## Notas

- El repositorio se actualiza constantemente según disponibilidad de datos en el [repositorio del Ministerio de Ciencia, Tecnología, Conocimiento e Innovación](https://github.com/MinCiencia/Datos-COVID19). Por lo general, este tipo de actualizaciones están bajo el commit "🤖 *Actualización de repositorio*".

- La entrada de archivos se encuentra en "[in](https://github.com/pandemiaventana/pandemiaventana/tree/main/in)" y la salida en "[out](https://github.com/pandemiaventana/pandemiaventana/tree/main/out)".

- La subida a Instagram aún no se encuentra automatizada por riesgo de ban.