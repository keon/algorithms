# 貢献

私たちは、誰からもプルリクエストを歓迎します。このレポジトリに貢献をするためには[Code of Conduct](CODE_OF_CONDUCT.md)を従うことを同意しなければなりません。

## 始める

* まずリポジトリを[フォーク][fork]し,次を使用してクローンします.

    git clone git@github.com:your-username/algorithms.git  

* その後,変更のためのブランチを作成します. 例えば：
  * add_XXX : 新しいアルゴリズムやデータ構造を追加する場合  
  * fix_XXX : 特定のアルゴリズムやデータ構造のbugを修正する場合
  * test_XXX : テストを作成する場合

以下の方法で貢献できます:
- レポジトリの新しいアルゴリズムを開発すること。 正しいセクションに保存してください(例: [array](array), [dp](dp), 等)。 どのセクションにも該当しない場合は、新しいセクションを作成します。 また、コードが正常に作動するかどうか確認してください。
- 既存のアルゴリズムの最適化または改善。
- 問題の他のソリューションを追加。
- バグの検索と修正。
- アルゴリズムをよりよく説明するための例を追加。
- テストケースの追加。

## プルリクエスト
フォークにプッシュして[プルリクエストを送信します][pr]。

私たちは、検討した後、変更、改善、代替案を提案することもできます。
あなたのプルリクエストが受け入れられる可能性が高くなる方法：

* すべてのアルゴリズムは**Python 3**で開発されなければなりません。
(まだPython 2で作成されたアルゴリズムがいくつかあります。これらをPython 3に転換する作業でスタートすることもできます。)
* きれいで理解しやすいコードを作成する。
* コードに適切なコメントを残して[docstrings][docstr]にアルゴリズムが何をしているのか簡単に説明する。
* 小さな例を通じて出力を説明する。
* アルゴリズムのテストケースをいくつか含ませる。
* [good commit message][commit]を書く。


## イシュー
追加するアルゴリズムがあったり、既存のアルゴリズムにバグが発見された場合の[new issue][newissue]を提出してください。 新たなイシューを提出する前に重複を避けるために、[existing issues][issues]を確認してください。 また、現在のイシューを解決したり論議中のイシューに貢献することも考慮してください。

## コラボレータ
コラボレータには,どのようなヘルプや説明も求めることができます.

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
