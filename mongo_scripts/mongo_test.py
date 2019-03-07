# coding: utf-8

'''
    For mongodb search
    @author:xuriliuhen
'''

import os
import json
from pymongo import MongoClient



# 4.mongo_test
if __name__ == '__main__':
    
    ####测试环境
    '''
    client = MongoClient(host='****', port=****)
    db = client["****"]
    db.authenticate("user_name", r"password")
    '''
    ###生产环境
    client = MongoClient(host='****',port=****)
    db = client["****"]
    db.authenticate("user_name", r"password")
    

    #创建数据表(表相当于集合)
    
    table = db['****']
    #table = db['video_ai_error']

    ## 查
    print('***********************************************')
    #结合video_key和model查询指定模型的结果，也可组合其他条件查询
    #查询参考链接 https://www.cnblogs.com/xingmeng/p/5133782.html
    queryArgs = {'video_key':'d8cbfff7ac36fd46cd1ef03e6b9f600d286e4044', 'model': 'video_tag'}
    search_res = table.find(queryArgs)
    for record in search_res:
        print(record)
    

    



    
    
    
    

