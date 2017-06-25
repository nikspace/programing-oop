#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#-- 标准类定义
class ProtectedHello(object):
    '''
        type(Object/object): 输出对象类型
        isinstance(object,Class): object是否是Class类型实例
        dir(object) :输出对象的所有方法和属性
        hasattr(object,method_str) :对象是否存在method_str属性
        getattr(object,method_str): 获取object.method_str属性

    '''
    def __init__(self,font,size):
        self.__font = font
        self.__size = size
    # 打印对象信息，返回字符串
    def __str__(self):
        return ("font=%s,size=%d,hello world" % (self.__font,self.__size))

    #缩写
    #__repr__ = __str__

    # 为调试服务的
    def __repr__(self):
        return ("font=%s,size=%d,hello world" % (self.__font,self.__size))
    #成员函数getter
    def get_font(self):
        return self.__font

    #成员函数setter
    def set_font(self,font):
        self.__font = font
    
    #成员函数getter
    #应用@property 装饰器，讲成员函数装饰成属性
    @property
    def size(self):
        return self.__size
    
    #应用@property 装饰器，讲成员函数装饰成属性
    @size.setter
    def size(self,size):
        if not isinstance(size, int):
            raise ValueError('size must be an integer!')
        if size < 0 or size > 200:
            raise ValueError('size must between 0 ~ 200!')
        self.__size = size

    def hello(self, name='hello world'):
        print('This is the  ProtectedHello, %s.' % name)

if __name__ == '__main__':
    #实例化标准类，创建nh对象
    nh = ProtectedHello("Bold",110)
    nh.hello()
    print (nh)
    
    print ("hasattr(nh,'size'): " ,hasattr(nh,'size'))
    print ("getattr(nh,'size'): " ,getattr(nh,'size'))
    
    print ("type(nh): " ,type(nh))
    print ("isinstance(nh,ProtectedHello): " ,isinstance(nh,ProtectedHello))
    #输出对象的所有属性和方法
    print ("dir(nh): " ,dir(nh))
