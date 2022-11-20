import os

models = ["RNN", "RCNN", "CNN"]
pretrains = ["bert", "roberta",  "ernie",  "wwm"]
datasets = ["mini", "small", "mid", "large"]
seeds = [1, 11, 13]

for i in range(len(seeds)):
    seed = seeds[i]
    for dataset in datasets:
        for pretrain in pretrains:
            print("seed: {}, dataset: guwen_{}, pretrain: {}, model: {}".format(seed, dataset, pretrain, "MLP"))
            os.system("python run.py --model {} --dataset guwen_{} --seed {} > result/result_{}/result_{}_{}.txt".format(pretrain, dataset, seed, dataset, pretrain, i))
                
    for dataset in datasets:
        for pretrain in pretrains:
            for model in models:
                print("seed: {}, dataset: guwen_{}, pretrain: {}, model: {}".format(seed, dataset, pretrain, model))
                model_name = "{}_{}".format(pretrain, model)
                os.system("python run.py --model {} --dataset guwen_{} --seed {} > result/result_{}/result_{}_{}.txt".format(model_name, dataset, seed, dataset, model_name, i))
                
   