# coding=utf-8
import jieba


def readFile(filepath):
    string = ""
    with open(filepath, "r", encoding='utf-8', errors='ignore') as f:
        string = f.read()

    punctuation = [",", ".", "_", "-", "s", "\n"]
    for punc in punctuation:
        string = string.replace(punc, " ")
    string = string.lower()

    string = jieba.lcut(string, cut_all=True)
    res = []
    for item in string:
        if item != "":
            res.append(item)

    return res


