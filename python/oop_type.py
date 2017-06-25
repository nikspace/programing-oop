#!/usr/bin/env python
# -*- coding: utf-8 -*- 

'''
定义一个类函数，稍后用type函数关联到指定对象
'''
def type_fn(self, name='hello world'): # 先定义函数
    print('This is the type_fn, %s.' % name)

if __name__ == '__main__':
    '''
    @doc: type()函数也允许我们动态创建

    param1: class的名称；
    param2: 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
    param3: class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
    '''
    TypeHello = type('TypeHello',(object,),dict(hello=type_fn))
    th = TypeHello() 
    th.hello()
    print (type(TypeHello))
    print (type(th))
    print('\n-------------------\n')
    

    
    



