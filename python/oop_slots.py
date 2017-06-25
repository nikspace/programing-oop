#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from types import MethodType

'''
动态语言特性,不同于经验语言c++或者java，可以在运行时给对象/实例 ,或者类绑定任何属性和方法，注意如果是给对象绑定方法，对于其他对象是无效的；如果是给类绑定方法或者属性，会作用于所有对象/实例。

动态语言属于duck type：意思是弱类型语言，只要看起来像鸭子，走起路来像鸭子，就可以说它是鸭子。

__slots__ = ('name','size'): 限制可以动态绑定的属性范围，name,size之外的属性绑定时，会报错;只作用于当前类，对于子类无作用
'''

#外部方法
def set_color(self,color):
    self.color = color

class NormalHello(object):
    __slots__ = ('name','size','color')   
    pass

if __name__ == '__main__':
    #实例化标准类，创建nh对象
    nh = NormalHello()
    nh.name = "Slots"    
    nh.size = 110   
    try:
        nh.font = "Normal" 
    except:
        print("__slots__ 内无font定义，不能动态绑定属性")
    finally:
        print("finally")
    print(nh.name,nh.size)    


    #MethodType 给对象绑定自己特有方法，只作用于当前对象，其他对象无影响
    #nh.set_color = MethodType(set_color,nh) #python3 调用方式
    nh.set_color = MethodType(set_color,nh,NormalHello)
    nh.set_color("ffffff")
    print ("nh.set_color: ", nh.color)
    
    #给类绑定方法
    #NormalHello.set_color = set_color #python3 调用方式
    NormalHello.set_color = MethodType(set_color,None,NormalHello)
    nh2 = NormalHello()
    nh2.set_color("111111")
    print ("类绑定方法后: ", nh2.color)
