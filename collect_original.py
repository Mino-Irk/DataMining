import urllib.request
import urllib
import os
import zipfile

print('取得したいデータの分類を入力してください(910~919)')
clas = str(input())
print('取得したいデータ数を入力してください') #フラグ数になる
num = int(input())
flag = 0

#開くファイルのパス名は自由で
f = open('./sample_data/aozora_word_list_utf8.csv', 'r')

for file in f:
    line = file.split(',') 
    class_number = line[8] #分類番号
    if class_number[-3:] == clas:
        if flag < num:
            #------取得データの表示
            print('------ok------------')
            print(clas)
            print(line[0])
            print(line[45])
        
            #------カレントディレクトリの移動
            dire = str('./original_data/' + class_number[-3:])
            os.makedirs(dire, exist_ok=True)
            os.chdir(dire)

            #------データの取得(カレントディレクトリに落としてくる)
            url = line[45] 

            zips = url.split('/')
            zip_name = str(zips[-1])  #zipファイルの名前
            print(zip_name)

            any_url_obj = urllib.request.urlopen(url)
            local = open(os.path.basename(url), 'wb')
            local.write(any_url_obj.read())

            any_url_obj.close()
            local.close()

            #------zipファイルの解凍
            path = '.'
            inputFile = zipfile.ZipFile(zip_name)
            inputFile.extractall(path)

            #------カレントディレクトリを元に戻す
            os.chdir('../..')

            flag = flag + 1
        else:
            break
