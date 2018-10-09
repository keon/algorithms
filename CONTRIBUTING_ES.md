# Contribuyendo

Nos encantan los pull requests de todos. Al contribuir a este repositorio, usted acepta cumplir con el [Código de Conducta](CODE_OF_CONDUCT.md).

## Comenzando

* Primero haga un [fork][fork] del repositorio y luego clónelo usando:

    git clone git@github.com:your-username/algorithms.git  

* Después de eso, crea una git branch para tus cambios. Por ejemplo:  
  * add_XXX Si agregara nuevos algoritmos o estructuras de datos.  
  * fix_XXX Si arreglará un error en un determinado algoritmo o estructura de datos.  
  * test_XXX Si escribiste una o más pruebas.  
  * doc_XXX Si ha editado o añadido a la documentación.

Usted puede contribuir:
- Implementando nuevos algoritmos en el repositorio. Asegúrese de ponerlo en la sección correcta (ej. [array](array), [dp](dp), etc). Cree una nueva sección para él si no cae en ninguna. Asegúrese de que su implementación funciona.  
- Optimizando o mejorando los algoritmos existentes.
- Añadiendo una solución diferente para el problema.
- Encontrando y corrigiendo errores.
- Añadiendo ejemplos para explicar mejor los algoritmos.
- Añadiendo casos de prueba.
- Mejorando la documentación.

## Pull Requests
Haga push a su fork y [envie un pull request][pr].

Revisaremos y sugeriremos algunos cambios, mejoras o alternativas. Algunas cosas que aumentarán la posibilidad de que su pull request sea aceptado:


* Todos los algoritmos deben estar escritos en **Python 3**.
(Hay algunos algoritmos todavía con la sintaxis de _Python 2_. Puede comenzar con la conversión de [aquellos][issue120] a _Python 3_.)
* Escribir código limpio y comprensible.
* Comente correctamente el código y explique brevemente qué está haciendo el algoritmo en los [docstrings][docstr].
* También puede explicar la salida usando un ejemplo mínimo.
* Trate de incluir también un par de casos de prueba para el algoritmo.
* Escriba un [buen mensaje en el commit][commit].


## Issues
Envíe un [nuevo issue][newissue] si hay un algoritmo por agregar, o si se encontró un error en un algoritmo existente.  Antes de enviar un nuevo issue, revise lo [issues existentes][issues] para evitar crear duplicados. También, considere resolver problemas actuales o contribuir a la discusión sobre un tema.

## Colaboradores
Puedes pedir ayuda o aclaraciones a los colaboradores.
[Keon Kim](https://github.com/keon)

[Rahul Goswami](https://github.com/goswami-rahul)

[Ankit Agarwal](https://github.com/ankit167)

[Hai Hoang Dang](https://github.com/danghai)

[Saad](https://github.com/SaadBenn)

[fork]: https://help.github.com/articles/fork-a-repo/
[docstr]: https://www.python.org/dev/peps/pep-0257/#multi-line-docstrings
[commit]: http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html
[pr]: https://github.com/keon/algorithms/compare/
[newissue]: https://github.com/keon/algorithms/issues/new
[issue120]: https://github.com/keon/algorithms/issues/120
[issues]: https://github.com/keon/algorithms/issues/
