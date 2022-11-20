import pandas as pd
import os
from sklearn.utils import shuffle

train_data = pd.read_csv("./train.csv", sep=',')
train_data.columns = ['content','type']
train_data_0 = train_data[train_data['type'] == 0].sample(frac=1).reset_index(drop=True)
train_data_0 = train_data_0.iloc[:train_data_0.shape[0] // 40]

train_data_1 = train_data[train_data['type'] == 1].sample(frac=1).reset_index(drop=True)
train_data_1 = train_data_1.iloc[:train_data_1.shape[0] // 40]

train_data = pd.concat([train_data_0, train_data_1])
train_data = train_data.sample(frac=1).reset_index(drop=True)

with open("../guwen_small/data/train.txt", 'w', encoding='utf-8') as f:
    for index, row in train_data.iterrows():
        f.write((str(row[0]) + '\t' + str(row[1]) + '\n'))

test_data = pd.read_csv("./test.csv", sep=',')
test_data = shuffle(test_data)

with open("../guwen_small/data/test.txt", 'w', encoding='utf-8') as f:
    for index, row in test_data.iterrows():
        f.write((str(row[0]) + '\t' + str(row[1]) + '\n'))


valid_data = pd.read_csv("./dev.csv", sep=',')
valid_data.columns = ['content','type']
valid_data = shuffle(valid_data)
valid_data_0 = valid_data[valid_data['type'] == 0].sample(frac=1).reset_index(drop=True)
valid_data_0 = valid_data_0.iloc[:valid_data_0.shape[0] // 20]

valid_data_1 = valid_data[valid_data['type'] == 1].sample(frac=1).reset_index(drop=True)
valid_data_1 = valid_data_1.iloc[:valid_data_1.shape[0] // 20]

valid_data = pd.concat([valid_data_0, valid_data_1])
valid_data = valid_data.sample(frac=1).reset_index(drop=True)

with open("../guwen_small/data/dev.txt", 'w', encoding='utf-8') as f:
    for index, row in valid_data.iterrows():
        f.write((str(row[0]) + '\t' + str(row[1]) + '\n'))
