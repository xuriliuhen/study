# coding: utf-8

'''
    For mongodb search
    @author:lzx
'''

import os
import json
from pymongo import MongoClient



# 4.mongo_test
if __name__ == '__main__':
    
    ####测试环境
    '''
    client = MongoClient(host='10.4.12.12', port=27018)
    db = client["admin"]
    db.authenticate("fulishe", r"$uQKq5Nr2M&8")
    '''
    ###生产环境
    client = MongoClient(host='mongos-shequ04',port=6002)
    db = client["media_ai"]
    db.authenticate("media_user", r"G5!tbw%gXe4t")
    

    #创建数据表(表相当于集合)
    
    table = db['video_ai_result']
    #table = db['video_ai_error']

    ## 查
    print('***********************************************')
    #结合video_key和model查询指定模型的结果，也可组合其他条件查询
    #查询参考链接 https://www.cnblogs.com/xingmeng/p/5133782.html
    queryArgs = {'video_key':'d8cbfff7ac36fd46cd1ef03e6b9f600d286e4044', 'model': 'video_tag'}
    search_res = table.find(queryArgs)
    for record in search_res:
        print(record)
    

    



    
    
    
    

