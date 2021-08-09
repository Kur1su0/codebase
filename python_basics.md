## Array ops
- initialize 2d-array
```
op = [[0] * col for _ in range(row)]
```
## OrderedDict
```
from collections import OrderedDict
od = OrderedDict()
```
- iteration
```
for key,v in od.items():
    print(key,v)
```
-Move to end(key, last=True)  \[ret:None\]
```
od.move_to_end('key')
```
-popitem(last=True)  \[ret: popped item\]



## More on the way
