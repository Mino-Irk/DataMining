# 青空文庫の文庫の分類ごとのファイル分けを行う．
# 分類するのは日本文学のみ．(910~919まで)
# 分類された文庫の作品一覧は"91*.txt"としてクラスごとに出力される.

first = open('sample_data/aozora_word_list_utf8.csv', 'r')

a = open('classify_novel/910.txt', 'w')
b = open('classify_novel/911.txt', 'w')
c = open('classify_novel/912.txt', 'w')
d = open('classify_novel/913.txt', 'w')
e = open('classify_novel/914.txt', 'w')
f = open('classify_novel/915.txt', 'w')
g = open('classify_novel/916.txt', 'w')
h = open('classify_novel/917.txt', 'w')
i = open('classify_novel/918.txt', 'w')
j = open('classify_novel/919.txt', 'w')

for line in first:
    ele = line.split(',')
    num = ele[8]
    class_num = num[-3:]
    print(class_num)
    if class_num == "910":
        a.writelines(ele[1]+"\n")
    elif class_num == "911":
        b.writelines(ele[1]+"\n")
    elif class_num == "912":
        c.writelines(ele[1]+"\n")
    elif class_num == "913":
        d.writelines(ele[1]+"\n")
    elif class_num == "914":
        e.writelines(ele[1]+"\n")
    elif class_num == "915":
        f.writelines(ele[1]+"\n")
    elif class_num == "916":
        g.writelines(ele[1]+"\n")
    elif class_num == "917":
        h.writelines(ele[1]+"\n")
    elif class_num == "918":
        i.writelines(ele[1]+"\n")
    elif class_num == "919":
        j.writelines(ele[1]+"\n")
    else:
        print("find no nobel")

a.close()
b.close()
c.close()
d.close()
e.close()
f.close()
g.close()
h.close()
i.close()
j.close()

