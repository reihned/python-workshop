# Python Notes

> Learning and working with python

###The Zen of Python, by Tim Peters

> Beautiful is better than ugly.  
> Explicit is better than implicit.  
> Simple is better than complex.
> Complex is better than complicated.  
> Flat is better than nested.  
> Sparse is better than dense.
> Readability counts.  
> Special cases aren't special enough to break the rules.  
> Although practicality beats purity.  
> Errors should never pass silently.
> Unless explicitly silenced.  
> In the face of ambiguity, refuse the temptation to guess.  
> There should be one-- and preferably only one --obvious way to do it.  
> Although that way may not be obvious at first unless you're Dutch.
> Now is better than never.  
> Although never is often better than *right* now.  
> If the implementation is hard to explain, it's a bad idea.  
> If the implementation is easy to explain, it may be a good idea.  
> Namespaces are one honking great idea -- let's do more of those!  


##Setup
###install
```bash
$ sudo apt-get install python-pip python-dev build-essential
$ sudo pip install --upgrade pip
$ sudo pip install --upgrade virtualenv
```

###quick virtual environment

```bash
$ virtualenv [folder]
$ cd [folder]
$ bin/source
```

also

```
$ pip install ipdb
```

##ipdb
```python
import ipdb; ipdb.set_trace()
```

|cmds |description          |
|-----|---------------------|
| n   | next                |
| c   | continue            |
| l   | show where you are  |
| q   | quit                |

##Styleguide
pep8

##Data Types and Variables
|Type           |Mutability   |Common use case  |
|-              |-            |-                |
|Numbers        |immutable    ||
|String         |immutable    ||
|List *(Array)* |mutable      ||
|Tuple          |immutable    ||
|Dict *(Hash)*  |mutable      ||

####Mutability
> http://en.wikipedia.org/wiki/Immutable_object  
> Copy-on-Write

None (nil)

###Everything is an object
```python
a = 1000
b = 1000
a == b    # true
a is b    # false
```
