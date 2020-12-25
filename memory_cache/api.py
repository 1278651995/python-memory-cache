# coding=gbk
from abc import ABCMeta, abstractmethod

from memory_cache.storage import SimpleStorage

"""
操作的API
"""


class BaseCacheAPI(metaclass=ABCMeta):
    def __init__(self, storage=None, max_size=1024):
        """
        :param storage: 存储类，[storage.BaseStorage]
        :param max_size: 默认存储最大内存为1024字节的数据
        """
        self._storage = storage if storage is not None else SimpleStorage()

    @abstractmethod
    def set(self, key, value, expire=-1):
        """
        存储key-value数据
        :param key: 存储的key
        :param value: 存储的key对应的值
        :param expire: 存储超时时间，默认是不会过期
        """
        self._hash_storage[key] = value

    @abstractmethod
    def get(self, key):
        """
        根据key取值
        :param key: 存储的键
        :return: value: 获取的值
        """
        return self._hash_storage.get(key, None)

    @abstractmethod
    def delete(self, key):
        """
        删除存储的键值对
        :param key: 键
        :return: items: 存储的键的值
        """
        value = self._hash_storage.get(key, None)
        del self._hash_storage[key]
        return value
