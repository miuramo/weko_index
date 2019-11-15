# WEKO_INDEX

**WEKO_INDEX** は、[情報処理学会電子図書館　情報学広場](https://ipsj.ixsq.nii.ac.jp/ej/) でダウンロードしたシンポジウム予稿論文のWebインデックスファイルを生成するプログラムです。

## つかいかた (その1)

### (1) 情報学広場から、WEKOエクスポート形式で、ZIPファイルをダウンロードします。

### (2) WEKO_INDEX をクローンしたフォルダに、ZIPファイルを置きます（複数ファイル可）。

<img src="https://github.com/miuramo/weko_index/blob/master/wekoindex_usage01.png" width="40%">

### (3) $ make

- ZIPファイルに含まれる import.xml の内容をもとに index.html を生成します。
- PDFファイルも、同一フォルダに展開します。
- zip ファイルやスクリプト、ライセンスファイル等の不要なファイルは、あとで削除してください。

## つかいかた (その2：単一ZIP内の import.xml から、インデックス生成)

### (1) ZIPファイル中の、import.xml を、フォルダ内トップに置きます。

### (2) $ make xml2html

## 必要なもの

- Python3
- unzip
- make
