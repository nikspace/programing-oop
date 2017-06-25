#!/usr/bin/env python
# -*- coding: utf-8 -*- 

'''
标准类定义
'''
class NormalHello(object):
    def hello(self, name='hello world'):
        print('This is the  NormalHello, %s.' % name)

if __name__ == '__main__':
    #实例化标准类，创建nh对象
    nh = NormalHello()
    nh.hello()
    # 因为NormalHello是一个类，所以type(NormalHello) 输出type
    print (type(NormalHello))
    # 因为nh是对象，对象的type是类NormalHello
    print (type(nh))
    print('\n-------------------\n')
