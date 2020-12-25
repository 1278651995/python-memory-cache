# coding=gbk
from abc import ABCMeta, abstractmethod

"""
存储类
"""


class BaseStorage(metaclass=ABCMeta):
    def __init__(self):
        self._hash_storage = dict()

    @abstractmethod
    def set(self, key, value):
        """
        存储key-value数据
        :param key: 存储的key
        :param value: 存储的key对应的值
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


class SimpleStorage(BaseStorage):
    def set(self, key, value):
        super(SimpleStorage, self).set(key, value)

    def get(self, key):
        return super(SimpleStorage, self).get(key)

    def delete(self, key):
        return super(SimpleStorage, self).delete(key)
