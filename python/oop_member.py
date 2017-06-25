#!/usr/bin/env python
# -*- coding: utf-8 -*- 

'''
标准类定义
成员访问权限控制
'''
class ProtectedHello(object):
    '''
        构造函数
        __font 字体 
        __size 大小
        __开头成员变量为私有变量，外部无法访问，类似c++ protected:定义的变量
        如果需要访问，需要设置成员函数来访问
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

    nh.set_font("Normal");
    print (nh)
    #print self.__font
    print(nh.get_font())

    #print 私有成员变量,不是不能访问，而是被解析器改成了另外一个方式，但是强烈不建议直接访问，不同解析器解析成的变量名格式不一样
    #print(nh._ProtectHello__font)

    #像属性一样访问成员函数，@property的作用
    print ("@property:  ", nh.size)  #nh.get_size() 
    nh.size = 130    #nh.set_size(130)
    print ("@size.setter:  ", nh.size)  #nh.get_size() 
    
