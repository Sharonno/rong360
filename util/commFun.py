# -*- coding: utf-8 -*-
__author__ = 'Shang'

import math

def UserSimilarity(train):
    """
    return similarity matrix
    """
    # 建立物品－用户的倒排表, 对每个物品都保存对该物品产生过行为的用户列表
    item_user = {}
    for u, items in train.items():
        for i in item.keys():
            if i not in item_user:
                item_user[i] = set()
            item_user[i].add(u)

     # 计算用户之间有交集的物品
     C = dict()
     N = dict()
     for i, users in item_user.items():
         for u in users:
             N[u] += 1
             for v in users:
                 if u == v:
                     continue;
                 C[u][v] += 1 / math.log(1 + len(users))

    # 计算相似性矩阵
    # TODO: add u_v pair weight !!!
    W = dict()
    for u, related_users in C.items():
        for v, cuv in related_users.items():
            W[u][v] = cuv / math.sqrt(N[u]*N[v])

    return W



