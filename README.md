# weko_index
WEKO_INDEX

**WEKO_INDEX** は、[情報処理学会電子図書館　情報学広場](https://ipsj.ixsq.nii.ac.jp/ej/) でダウンロードしたシンポジウム予稿論文のWebインデックスファイルを生成するプログラムです。

## つかいかた

### (1) 情報学広場から、WEKOエクスポート形式で、ZIPファイルをダウンロードします。

### (2) WEKO_INDEX をクローンしたフォルダに、ZIPファイルを置きます。

<img src="https://github.com/miuramo/weko_index/blob/master/wekoindex_usage01.png" width="40%">

### (3) make

### (4) index.html を生成し、PDFファイルも同一フォルダに展開します。

zip ファイルが不要でしたら、削除してください。


## 必要なもの

- Python3
- unzip
