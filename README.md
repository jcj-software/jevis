# Jevis——一个第三方Python库

[![Upload Python Package](https://github.com/lemonorangeapple/jevis/actions/workflows/python-publish.yml/badge.svg)](https://github.com/lemonorangeapple/jevis/actions/workflows/python-publish.yml)

下载方式：
```python
pip install Jevis
```
导入方式：
```python
from Jevis import *
```
功能：
指针（pointer）类
and
switch类

pointer类使用方式：
```python
> from Jevis import *

> p1 = pointer(123)

> p1.get()
123
> p2 = pointer(567)

> p2.set(456)

> p2.get()
456
> p1.swap(p2)

> p1.get()
456
> p2.get()
123
```
switch类使用方式：
```python
from Jevis import *
i = int(input())
s = switch(i)
s.case(1, lambda: print(1))
s.case(2, lambda: print(2))
s.case(3, lambda: print(3))
s.case(4, lambda: print(4))
s.case(5, lambda: print(5))
s.default(lambda: print("default"))
```
运行：
```python
> 1
1
> 2
2
> 3
3
> 4
4
> 5
5
> 6
default
```

下载地址：    
https://pypi.org/project/Jevis/    

源码：    
https://github.com/lemonorangeapple/Jevis    
