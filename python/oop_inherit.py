#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
    单继承
    多继承
'''
class BaseHello(object):
    def hello(self, name='hello world'):
        print('This is the  BaseHello, %s.' % name)
#单继承
class FontHello(BaseHello):
    def font(self):
        print ("FontHello.font()") 
    pass
#单继承
class SizeHello(BaseHello):
    def size(self):
        print ("SizeHello.size()")
    pass
    
#单继承
class ColorHello(BaseHello):
    def hello(self, name='color hello world'):
        print ('ColorHello.hello() called.')
    def color(self):
        print ("ColorHello.color()")
    pass
    
#多继承
class RichHello(FontHello,SizeHello,ColorHello):
    pass

if __name__ == '__main__':
    #实例化标准类，创建base对象
    base = BaseHello()
    base.hello()
    print("isinstance(base,BaseHello: ",isinstance(base,BaseHello)) 

    font = FontHello()
    font.hello()
    font.font()
    print("isinstance(font,BaseHello: ",isinstance(font,BaseHello)) 
    print("isinstance(font,FontHello: ",isinstance(font,FontHello)) 
    
    size = SizeHello()
    size.hello()
    size.size()
    
    color = ColorHello()
    color.hello()
    color.color()

    print("multiple inherite :")    
    rich = RichHello()
    rich.hello() #注意是继承了子类的Color.hello方法
    rich.font()
    rich.size()
    rich.color()

    print("RichHello isinstance(rich,BaseHello: ",isinstance(rich,BaseHello)) 
    print("RichHello isinstance(rich,FontHello: ",isinstance(rich,FontHello)) 
    print("RichHello isinstance(rich,SizeHello: ",isinstance(rich,SizeHello)) 
    print("RichHello isinstance(rich,ColorHello: ",isinstance(rich,ColorHello)) 

    
