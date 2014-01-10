bcentroid
=========

Bayesian centroid motif finder with the ability to handle ChIP-seq sequences.

运行方法：
-------
python main.py f=FileName[ argname=argvalue ... ]
参数：
---
    f: 序列文件名，接受txt，fasta等格式。
    n: 模体实例数量，默认值为1.
    t: 迭代次数，默认1000.
    len: 模体实例长度， 默认10.
    p: 初始矩阵文件名, 默认随机生成矩阵。
