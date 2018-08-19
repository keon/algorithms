# Contribuer

Nous aimons les contributions (sous la forme de pull requests). En contribuant à ce repertoire, vous acceptez de suivre les 
règles du [Code de conduite](CODE_OF_CONDUCT_FR.md).

## Mise en route

* Dans un premier temps [forkez][fork] le repertoire puis clonez le grâce à la commande:

    git clone git@github.com:votre-pseudo-github/algorithms.git  

* Ensuite, créez une nouvelle branche dans laquelle vous effectuerez vos changements. For example:  
  * add_XXX si vous allez ajouter de nouveaux algorithmes ou de nouvelles structures de données.  
  * fix_XXX si vous allez corriger un bogue sur un certain algorithme ou structure de données.  
  * test_XXX si vous avez écrit un ou des tests.  
  * doc_XXX si vous avez ajouté ou édité de la documentation.

Vous pouvez contribuer en : 
- implémenter un nouvel algorithme dans ce repertoire. Faites bien attention à 
le mettre dans la bonne section (i.e. [array](array), [dp](dp), etc). Vous pouvez créer une nouvelle
section si besoin. Assurez-vous que votre implémentation fonctionne,
- optimisant et en améliorant les algorithmes déjà présents,
- ajoutant de nouvelles solutions aux problèmes,
- trouvant et corrigeant des bogues,
- ajoutant des exemples afin de mieux expliquer le fonctionnement des algorithmes,
- ajoutant des tests,
- améliorant la documentation.

## Pull Requests
Poussez votre fork sur git et [soumettez une nouvelle pull request][pr].
Nous examinerons et pourrons suggérer des changements, des améliorations ou des solutions de rechange.
Pour faciliter l'acceptation, vous pouvez vérifier que :

* tous les algorithmes doivent être écrits en **Python 3**,
(il reste encore quelques algorithmes écrits en  _Python 2_. Vous pouvez commencer par convertir ces 
[derniers][issue120] vers du _Python 3_),
* écrire un code propre et compréhensible,
* commenter correctement le code et expliquer brièvement ce que l'algorithme fait dans la [documentation][docstr],
* vous pouvez également expliquer le résultat à l'aide d'un exemple simple.
* essayer d'écrire quelques tests pour les algorithmes,
* écrire un [message de soumission (commit) clair][commit].


## Problèmes
Soumettez une [nouveau issue][newissue] s'il y a un algorithme à ajouter, ou si un bogue a été trouvé dans un algorithme existant. Avant d'en soumettre une nouvelle, veuillez passer en revue les [issues existantes][issues] afin d'éviter de créer des doublons. Envisagez également de résoudre des issues actuellement ouvertes ou de contribuer à la discussion sur une issue.

## Collaborateurs
Vous pouvez demander de l'aide ou des éclaircissements aux collaborateurs.  
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
