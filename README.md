# getAirfoil.py
[UIUCの翼型データベース](https://m-selig.ae.illinois.edu/ads/coord_database.html#R)からすべての翼型をダウンロードします。  
ダウンロード先は./dat_files以下でディレクトリがない場合は自動で生成されます。

Download all airfoils from the UIUC airfoil database.  
Download to . /dat_files and if the directory does not exist, it will be generated automatically.

~~~
#run and download
> python getAirfoil.py
~~~

# viewDatAirfoil.py(.bat)
getArifoil.pyで入手した.datファイルの簡易的なビューワーです。  
プログラム本体はviewDatAirfoil.pyですがviewDatAirfoil.batにdatファイルをドラッグアンドドロップすることで翼型が表示されます。

This is a simple viewer for .dat files obtained by getArifoil.py.  
The main program is viewDatAirfoil.py, but by dragging and dropping the dat file into viewDatAirfoil.bat, the airfoil is displayed.



***

LICENSE IS MIT
