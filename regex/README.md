One useful function in the Python module is ```dis```. This is a **bytecode analysis API**, which essentialy *disssembles* Python bytecode into a more readable format.\
A demonstration of the same is below:
```python
dis.dis(lambda x,y : sqrt(x ** 2 + y ** 2))
```
The purpose of the above code is pretty much self explanatory. The output that we get from this produces a somewhat interesting result:\
![Screenshot](https://github.com/ckapoor7/misc-python/blob/main/regex/Screen%20Shot%202021-04-07%20at%209.09.13%20PM.png) 