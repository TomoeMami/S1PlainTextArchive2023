#!/usr/bin/env/ python3

import os,shutil,re,time,sys

def thread_dict(thdir,thdict):
    with open(thdir,'r',encoding='UTF-8') as f:
        lines = f.readlines()
        a = ''
        for line in lines:
            a += line
        b = a.split("*****")
    for i in b[1::]:
        if(re.findall(r'#####\s(\d+)#',i)[0]):
            thdict[re.findall(r'\n#####\s(\d+)#',i)[0]] = i

def thread_merge(oridir,desdir):
    ori = {}
    des = {}
    thread_dict(oridir,ori)
    if os.path.exists(desdir):
        thread_dict(desdir,des)
    result = ''
    for i in sorted(list(set(ori.keys())-set(des.keys()))):
        result = result +  ("*****") + ori[i]
    with open (desdir,'a',encoding='UTF-8')as f:
        f.write(result)
    os.remove(oridir)

def get_dir_files(dir_path):
    file_list = os.listdir(dir_path)
    result = []
    for i in file_list:
        result.append(os.path.join(dir_path, i))
    return result
