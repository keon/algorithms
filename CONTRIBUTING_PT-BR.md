# Contribuindo

Pull requests são bem vindos de todos. Contribuindo para este repositório, você concorda em respeitar o [Código de Conduta](CODE_OF_CONDUCT_PT-BR.md).

## Por onde começar

* Primeiro [fork][fork] o repositório e então clone com o seguinte comando:

    git clone git@github.com:seu-username/algorithms.git  

* Depois disso crie um branch para as suas mudanças. Por exemplo:  
  * add_XXX se você vai adicionar novos algoritmos ou estruturas de dados.  
  * fix_XXX se você vai corrigir um bug em um certo algoritmo ou estrutura de dados.  
  * test_XXX se você vai escrever um teste.  
  * doc_XXX se você adicionou ou editou documentação.

Você pode contribuir:
- implementando novos algoritmos no repositório. Certifique-se de mantê-lo na seção correta (ex. [array](array), [dp](dp), etc). Crie uma nova seção caso sua contribuição não se encaixe em nenhuma seção. Assegure-se de que sua implementação funcione.  
- otimizando ou melhorando os algoritmos existentes.
- adicionando uma solução diferente para um problema.
- encontrando e corrigindo bugs.
- incluindo exemplos para explicar melhor os algoritmos.
- adicionando casos de teste.
- melhorando a documentação.

## Pull Requests
Faça upload para o seu fork e então [submeta um pull request][pr].

Nós vamos revisar e podemos sugerir algumas mudanças, melhorias ou alternativas.
Algumas coisas que vão aumentar a chance do seu pull request ser aceito:

* Todos os algoritmos devem ser escritos em **Python 3**.
(Ainda existem alguns algoritmos em _Python 2_. Você pode começar convertendo
[esses][issue120] para _Python 3_.)
* Escreva código claro e compreensível.
* Comente o código devidamente e explique brevemente o que o algoritmo está fazendo nos [docstrings][docstr].
* Você também pode explicar a saída usando um exemplo mínimo.
* Também tente incluir alguns casos de teste para o algoritmo.
* Escreva uma [boa mensagem de commit][commit].


## Issues
Submeta uma [nova issue][newissue] se existe algum algoritmo para adicionar, ou se um bug foi encontrado em algum algoritmo existente. antes de submeter uma nova issue por favor revise os [issues existentes][issues] para evitar a criação de duplicatas. Também, considere resolver as issues existentes ou participar na discussão de uma issue.

## Colaboradores
Você pode pedir qualquer ajuda ou esclarecimentos dos colaboradores.  
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
