# 기여 활동

모든 pull request는 환영입니다. 이 저장소에 기여 함으로써, 당신은 [code of conduct](CODE_OF_CONDUCT.md)
를 준수하는 것에 동의 한 것입니다.


## 시작하기 

* 우선 이 저장소를 [fork][fork] 하시고, 이를 사용하기 위해서 다음과 같이 clone 주세요:

    git clone git@github.com:your-username/algorithms.git  

* 그리고 새로운 내용을 더할 branch를 만들어주세요. 예를 들어:  
  * add_XXX 만약 당신이 새로운 알고리즘이나 자료 구조를 추가 했을 경우.  
  * fix_XXX 만약 당신이 어떤 알고리즘이나 자료 구조에서 고쳐야할 bug를 발견했을 경우.  
  * test_XXX 만약 당신이 test/s를 작성한 경우.  

당신은 다음과 같이 기여할 수 있습니다:
- 새로운 알고리즘을 구현해주세요. 그리고, 그것을 정확히 분류해주세요(e.g. [array](array), [dp](dp), etc).
만약 당신의 알고리즘이 어떤 섹션에도 포함이 되지 않는다면, 새로운 섹션을 만들어 주세요. 단, 당신의 알고리즘이 제대로 작동하는지
확인해주세요.  
- 알고리즘들을 최적화하거나 향상시켜주세요.
- 문제들에 대해서 다른 해결 법을 추가해주세요.
- 버그들을 찾거나 고쳐주세요.
- 알고리즘들을 더 잘 설명하기 위한 새로운 예시들을 추가해주세요.
- test cases를 추가해주세요.

## Pull Requests
당신의 fork에 push 하고 pull request를 제출하세요 [submit a pull request][pr].

우리는 이를 검토할 것이며, 변화, 개량, 혹은 대안을 제시할 수 도 있습니다.
여기에 당신의 pull request가 허용될 가능성을 높여주는 몇몇 요소들이 있습니다:

* 모든 알고리즘들은 **Python 3**로 작성되어야 합니다.
(몇몇 알고리즘들은 여전히 _python 2_ 로 작성되어져 있습니다. 당신은 이를 Python 3으로 번역함으로써 저희에게 기여 해주실 수도 있습니다.
[those][issue120] to _Python 3_.)
* 깔끔하고 이해할 수 있는 코드를 작성해주세요.
* 코드에 대해 올바르게 주석 처리 해 주시고, 알고리즘이 수행하는 작업에 대해서 [docstrings][docstr]에서 설명해 주세요.
* 당신은 간단한 예시를 제시함으로써 출력 값에 대하여 설명하실 수도 있습니다.
* 또한 가능하다면 알고리즘에 대하여, 두 가지의 test cases를 포함 시켜주세요.
* [good commit message][commit]를 작성해주세요.


## Issues
만약 추가해야 할 알고리즘이 있거나, 현재 저희 프로젝트의 어떤 알고리즘에서 버그가 발견된다면 [new issue][newissue]에 이를 추가해주세요. 새로운 issue를 제안하기 전에 중복된 issue을 발생을 피하기 위해서 [existing issues][issues]를 확인해주세요. 또한, 현재 존재하는 issue를 해결하는 것을 고려해주시거나 issue에 대한 토의에 기여해주세요.

## Collaborators
저희 협업자 들에게 어떤 도움이나 확인이 필요하다면, 위 주소로 물어봐주세요.

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
