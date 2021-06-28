## Bienvenido 📉

La pandemia por la ventana es un sitio, elaborado con formato de *libro* gracias a Jupyter Books, realizado por Alejandro Dinamarca, que recaba el trabajo en Numeral.lab en la Región de Tarapacá.

Favor, cualquier sugerencia o comentario, hacerlo llegar mediante [Issues de GitHub](https://github.com/pandemiaventana/pandemiaventana/issues/new).

:::{figure-md} markdown-fig
<img src="../../img/page/2_cover.png">

**Ilustración realizada por Bernardo Dinamarca**.
:::

El libro está dividido en distintas secciones, algunas respecto a las experiencias personales y otras con código de programación (hecho con cariño).

## Notas del autor

*Como siempre he recalcado, todo el trabajo realizado en pandemia fue en post de un bien común. Una especie de anhelo de devolver, en parte, una mano, a todo el mundo que me ha rodeado y del cual he aprendido, y espero seguir aprendiendo como un eterno aprendiz.*

*Este pequeño libro está dedicado a mis padres, a mis hermanos, familia y a mi amor. No sería nada sin ellos.*

*Dar las gracias al Dr. Cristóbal Corral y la Universidad Arturo Prat por el apoyo recibido, como también, por acojerme como estudiante y darme la posibilidad de desarrollar una idea que surgió desde el polvo.*

*Si bien este librito parece ser bastante serio, tiene un componente humano. Por lo que, a veces, en el relato, se utilizarán algunas frases coloquiales.*

## Tabla de contenido

La tabla de contenido de Jupyter Books (plataforma con la que se realizó esta página web) se encuentra a la izquierda:

```{tableofcontents}
```

## Funcionamiento

Básicamente, a través de Notebooks de Jupyter y un poco de Markdown. Python, por contraparte, genera los CSV, y Jupyter Books se encarga de generar la página web a partir de los Notebooks y el Markdown.

El despliegue del libro en [gh-pages](https://github.com/pandemiaventana/pandemiaventana/tree/gh-pages) se realiza cada vez que desencadeno un cambio en [main](https://github.com/pandemiaventana/pandemiaventana) a través del action [actualiza_libro](https://github.com/pandemiaventana/pandemiaventana/actions/workflows/book.yml).

## Estado

[![deploy-book](https://github.com/pandemiaventana/pandemiaventana/actions/workflows/book.yml/badge.svg)](https://github.com/pandemiaventana/pandemiaventana/actions/workflows/book.yml)
