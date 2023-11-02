#!/usr/bin/env/ python3

import os,re,time,sys

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

rootdir = "/home/riko/S1PlainTextArchive2023/"
rootcat = ["外野","手游专楼","游戏区","漫区","虚拟主播区专楼"]

for cate in rootcat:
    # cate = "手游专楼"
    cate_dict = {}
    files = get_dir_files(rootdir+cate)
    for i in files:
        th_id = re.split('/|-',i)[5]
        if th_id not in cate_dict.keys():
            cate_dict[th_id] = []
        cate_dict[th_id].append(i)
    dup_dict = {}
    for j in cate_dict.keys():
        if(len(cate_dict[j]) >1):
            dup_dict[j] = cate_dict[j]
    for k in dup_dict.keys():
        merge_dict = {}
        for l in dup_dict[k]:
            merge_dict[os.path.getmtime(l)] = l
            print(l)
        print('>>>')
        merge_list = sorted(list(merge_dict.keys()))
        while 1:
            if len(merge_list) >= 2:
                thread_merge(merge_dict[merge_list[1]],merge_dict[merge_list[0]])
                merge_list.pop(0)
            else:
                break
        print(merge_dict[merge_list[0]])
        print('---')

