# EC601-Visual-Question-Answering
## Overview
The mission of this project is to reimplement the baseline of VQA from Vahid Kazemi and Ali Elqursh’s paper, Show, Ask, Attend, and Answer: A Strong Baseline For Visual Question Answering, and to compare their method from previously published work on the popular VQA v1 dataset. The team hopes to replace and inject various implementations into these researcher’s models in order to achieve the most efficient Visual Question Answering task. Moreover, this project aims to provide simple analysis of the results for future researchers to build on. 

## Requirements
The following libraries are needed for the base model:

* torch
* torchvision
* h5py
* tqdm

## Steps

To run the base model, you should follow these steps:

* Clone the repository to your local computer
* Download the [mscoco dataset](https://visualqa.org/vqa_v1_download.html), and set their paths in `config.py`
* Pre-process the images and vocabularies. (Before doing this, you can customize the number of layers of resnet. We used resnet152, resnet101, resnet50, resnet34, resnet18 respectively to test the performance of base model).

```shell
python preprocess-images.py
python preprocess-vocab.py
```

* Train the model with:

```shell
python train.py
```

The default number of training epochs is 50 (indexed from 0 to 49). The result (`*.pth` file) will be saved to `logs` directory. You can plot diagram to visualize the result.

## Set Backs

Before successfully running the base model, we encountered several problems:

* At first we ran the model on BU SCC platform without GPU cores, thusing making the training speed so slow. Therefore, we switched to Google Colab to run base model. However, the connection to Colab is unstable and has limited using time, so that we cannot get the time-consuming training job done. Finally, we solved this issue by asking for GPU cores in the BU SCC platform, so we can use cuda to speed up the training process.
* We encountered some permission issues when installing libraries and running the model on SCC platform, because the base model code involves a lot of reading and writing operations. We solved this by operating `chmod` on specified files.
* As some of the code of base model is outdated, we modified these code when reimplementing it.

## Conclusion
