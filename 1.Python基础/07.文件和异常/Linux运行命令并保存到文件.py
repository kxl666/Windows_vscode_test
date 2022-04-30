#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import time

# os.popen("command").read()
# 获取命令内容

proc_fp = sum(
    map(
        int,
        os.popen(
            "ps -ef | grep face_platform |grep -v grep| awk '{print $2}'|xargs -I {} cat /proc/{}/status|grep -i thread| awk '{print $2}'"
        ).read().split('\n')[:-1]))  # [:-1] 切片取到最后一个元素之前

proc_all = os.popen("pstree -p|wc -l").read()[:-1]

proc_other = int(proc_all) - proc_fp

proc_gunicron = sum(
    map(
        int,
        os.popen(
            "ps -ef | grep gunicorn |grep -v grep| awk '{print $2}'|xargs -I {} cat /proc/{}/status|grep -i thread|awk '{print $2}'"
        ).read().split('\n')[:-1]))

now = time.strftime('%Y%m%d_%H:%M:%S', time.localtime())

result = '{}  fp线程数:{}  其他线程数:{}  总线程数:{}  gunicorn线程数:{}\n'.format(
    now, proc_fp, proc_other, proc_all, proc_gunicron)

with open('./report', 'a') as f:
    f.write(result)
