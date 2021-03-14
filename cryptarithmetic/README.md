A couple of points to note here.\
First off, since I use a **generator function** for brute forcing all possible number combinations, **only the 1st possible
solution is returned**. To change this and list all possible solutions, the following change can be made in the ```solve``` function:
```python
def solve(formula):
    for elem in fill_in(formula):
        if valid(elem):
            print(elem)
```
This simple change yields the desired result.\
Next, it is possible to see the *execution statistics* of a program in great detail using the ```cProfile``` module. Note that I have used the function 
```time.process_time()``` (compatible with Python 3) instead of ```time.clock()``` which is a feature of Python 2. To check the execution statistics, we run
the program from the command line with the following prompt\:
``` python3 -m cProfile xyz.py```\
```xyz``` being the file name. This should result in a neat table like so\
![Screenshot](https://github.com/ckapoor7/misc-python/blob/main/cryptarithmetic/Screen%20Shot%202021-03-14%20at%204.33.36%20PM.png)
