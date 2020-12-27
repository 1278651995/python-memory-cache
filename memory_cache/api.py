# coding=gbk
from abc import ABCMeta, abstractmethod

from memory_cache.algorithms import LRU
from memory_cache.storage import SimpleStorage

"""
操作的API
"""


class BaseCacheAPI(metaclass=ABCMeta):
    def __init__(self, storage=None, algorithms=None, max_size=1024):
        """
        :param storage: 存储类，[storage.BaseStorage]
        :param max_size: 默认存储最大内存为1024字节的数据
        """
        self._storage = storage if storage is not None else SimpleStorage()
        self._alg = algorithms if algorithms is not None else LRU(self._storage)
        self.max_size = max_size

    @abstractmethod
    def set(self, key, value, expire=-1):
        """
        存储key-value数据
        :param key: 存储的key
        :param value: 存储的key对应的值
        :param expire: 存储超时时间，默认是不会过期
        """
        if len(value) > self.max_size:
            assert ValueError('超出内存限制')
        return self._alg.set(key, value, expire)

    @abstractmethod
    def get(self, key):
        """
        根据key取值
        :param key: 存储的键
        :return: value: 获取的值
        """
        return self._alg.get(key)

    @abstractmethod
    def delete(self, key):
        """
        删除存储的键值对
        :param key: 键
        :return: items: 存储的键的值
        """
        return self._alg.delete(key)


class SimpleCacheAPI(BaseCacheAPI):
    def __init__(self, storage=None, algorithms=None, max_size=1024):
        super().__init__(storage, algorithms, max_size)

    def set(self, key, value, expire=-1):
        return super().set(key, value, expire)

    def get(self, key):
        return super().get(key)

    def delete(self, key):
        return super().delete(key)
