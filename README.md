# python-memory-cache

#### 介绍

python实现内存的缓存器，用于小数据存储。

默认使用LRU作为回收算法。

#### 安装
```shell script
pip install csy-memory-cache
```

#### 结构图

![结构图](/docs/结构图.png)



#### 使用教程

实例化

```python
from memory_cache.api import SimpleCacheAPI

api = SimpleCacheAPI()
# or
from memory_cache.algorithms import LRU
from memory_cache.storage import SimpleStorage

api = SimpleCacheAPI(algorithms=LRU, storage=SimpleStorage, max_size=1024)
```

存储

```python
api.set(key, value)
# or 
api.set(key, value, expire=10)  # 单位秒(s)
```

获取

```python
api.get(key)
```

删除

```python
api.delete(key)
```



#### 扩展

该缓存器中所有组件均可扩展，其中API扩展只需满足```BaseCacheAPI```定义、存储扩展只需满足```BaseStorage```定义， 回收算法只需满足```BaseAlgorithms```定义
