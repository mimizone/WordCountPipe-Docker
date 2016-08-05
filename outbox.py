# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 17:38:08 2016

@author: hpvk7699
"""
import os
import simplejson as json

def get_data(start_path):
    
    for root, dirs, files in os.walk(start_path):
        for f in files:
            path = os.path.join(root, f)
            with open(path) as fp:
                print (path)
                data = json.load(fp)
                return data
    
    
def output(data,outputpath):
    if not os.path.exists(outputpath):
        os.makedirs(outputpath)
    with open(outputpath+'/output_file','w') as fp:
        json.dumps(data ,fp)
        fp.write(json.dumps(data ,fp))
        fp.close()
        print('data export to outbox')
                                                                                                                                    