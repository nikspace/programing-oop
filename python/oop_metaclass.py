#!/usr/bin/env python
# -*- coding: utf-8 -*- 

'''
metaclass-元类 所有类的创建者模板类，注意与Object区分开来。 metaclass是Object的创建者模板类，而Object是所有类的父类
metaclass -> class -> object :metaclass 创建类，然后通过类创建对象
metaclass的类名总是以Metaclass结尾
metaclass是类的模板，所以必须从`type`类型派生：
'''
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

'''
当传入关键字参数metaclass时，魔术就生效了，它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建，在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。

__new__()方法接收到的参数依次是：
1. 当前准备创建的类的对象；
2. 类的名字；
3. 类继承的父类集合；
4. 类的方法集合。
'''
class MyList(list):
    __metaclass__ = ListMetaclass #用指定的元类模板来定制类定义

if __name__ == '__main__':

    #元类测试 
    L = MyList()
    L.add(1) # 标准List库是没有add方法的
    print(L)   
    
