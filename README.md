# まるつけくん
まるつけくんは簡単な2つの数の四則演算を画像認識、計算してくれるプログラムです。  
## <実行方法>  
marutsukekunディレクトリ内で以下のように実行
$ python3 maru.py problem/実行したい問題番号.png  

足し算→ta2〜ta7,ta10〜ta18,ta100  
引き算→hi1〜hi5  
掛け算→ka1〜ka7  
割り算→wa1〜wa6  

実行結果は
$ こたえは5×6=30だよ
のように返ってくる。

## <ディレクトリ構成>
- match_data              - 四則演算の記号データ  
- pdf                     - 問題の元データ  
- problem                 - 使用する問題ファイル群  
- README                  - 当初のアプリ案  
- maru.py                 - まるつけくん本体プログラム
- result.py               - 数字の特定を行うプログラム
- temp_match.py           - 記号をマッチングするプログラム
- generalresponses.data   - 学習データ
- generalsamples.data     - 学習データ2
- pitrain.png             - 学習用数字画像
