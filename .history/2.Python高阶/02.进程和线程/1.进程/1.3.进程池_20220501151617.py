'''
当需要创建的子进程数量不多时，可以直接利用multiprocessing中的Process动态成生多个进程,
但如果是上百甚至上千个目标，手动的去创建进程的工作量巨大，此时就可以用到multiprocessing模块提供的Pool方法。

'''
