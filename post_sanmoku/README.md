
## MiniMax法
- minimax.py<br>
  MiniMax法で三目並べを実行する対戦エージェント。<br>

## Q学習
- training.py<br>
  学習スクリプト。config.iniでパラメータを設定し学習を実行します。<br>
  学習済みの重みは"weight_\[学習回数\].csv"という名前でweightsフォルダに格納されます。<br>
- q_learning.py<br>
  学習済みの重みを使用してQ学習で三目並べを実行する対戦エージェント。<br>
  config.iniで使用する学習済みの重みの重みを指定して使用します。<br>

### 更新履歴 <br>
- 20240816: ソースコード一式を追加<br>
  会社の勉強会で作成した対戦エージェントのソースコード。<br>
  GUIは人対人のみ可能。<br>