import re
import os
import csv
from opencc import OpenCC

cc = OpenCC('t2s')


train_file = open("csv_data/train.csv", "w", newline='', encoding='utf-8')
dev_file = open("csv_data/dev.csv", "w", newline='', encoding='utf-8')
test_file = open("csv_data/test.csv", "w", newline='', encoding='utf-8')

train_writer = csv.writer(train_file)
dev_writer = csv.writer(dev_file)
test_writer = csv.writer(test_file)

train_list=[]
test_list=[]
dev_list=[]

san_wen_file = "./shibu_clean.txt"
with open(san_wen_file, 'r', encoding='utf-8') as f:
    for i in range(100000):
        line = f.readline().strip()
        line = re.sub(r'[《》（）〈〉〔〕“”\u3000﹑‘’【】0-9]+','', line)
        line = cc.convert(line)
        if i % 10 == 8:
            dev_list.append([line, 0])
        elif i % 10 == 9:
            test_list.append([line, 0])
        else:
            train_list.append([line, 0])

yun_wen_file_directory = "./Poetry"
yun_wen_files = os.listdir(yun_wen_file_directory)
print(yun_wen_files)

sum = 0
for file in yun_wen_files:
    with open(yun_wen_file_directory + '/' + file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        i = -1
        for csv_line in reader:
            if i == -1:
                i+=1
                continue
            line = csv_line[-1]
            line = cc.convert(line)
            if i % 76== 8:
                dev_list.append([line, 1])
            elif i % 76 == 9:
                test_list.append([line, 1])
            elif i % 76 < 8:
                train_list.append([line, 1])
            i+=1
        sum += i
print("data length in poetry", sum / 76 * 10)

train_writer.writerows(train_list)
dev_writer.writerows(dev_list)
test_writer.writerows(test_list)


