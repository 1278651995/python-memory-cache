# coding=gbk

"""
�����㷨
"""
import time
from abc import ABCMeta, abstractmethod
from collections import OrderedDict

from memory_cache.timer import Timer


class BaseAlgorithms(metaclass=ABCMeta):
    def __init__(self, storage, timer=Timer):
        self.capacity = 64
        self.cache = None
        self.timer = timer()
        self._storage = storage

    @abstractmethod
    def get(self, key):
        """
        ��ȡ�洢����ֵ
        :param key: �洢��
        :return: value
        """
        return None

    @abstractmethod
    def set(self, key, value, expire=-1):
        """
        �洢key�������ӳ�ʱʱ��
        :param key: key
        :param value: ֵ
        :param expire: ��ʱʱ�䣬��λ�루s)
        :return: �Ƿ�洢�ɹ�
        """
        return True

    @abstractmethod
    def delete(self, key):
        """
        ɾ��key��ͬʱɾ���洢�еļ�ֵ��
        :param key: key
        :param storage: �洢
        :return: �Ƿ�ɾ���ɹ�
        """
        del self._storage[key]
        return True

    @abstractmethod
    def clear(self):
        """
        ɾ�����еļ�ֵ��
        :return: �洢��
        """
        self._storage = type(self._storage)()
        return True

    @abstractmethod
    def clear_timeout(self):
        """
        ������ʱ�ļ�
        :return: �Ƿ�������
        """
        return True


class LRU(BaseAlgorithms):
    """
    ʹ��LRU�㷨���д洢
    """
    def __init__(self, storage):
        super(LRU, self).__init__(storage)
        self.cache = OrderedDict()
        self.timer.do(self.clear_timeout)

    def get(self, key):
        if key in self.cache.keys():
            value = self.cache.pop(key)
            cache_value = self._storage[key]
            self.cache[key] = value
        else:
            cache_value = None
        return cache_value

    def set(self, key, value, expire=-1):
        if key in self.cache.keys():
            value = self.cache.pop(key)
            self.cache[key] = value
        else:
            if len(self.cache) == self.capacity:
                old_key, _ = self.cache.popitem(last=False)
                self._storage.delete(old_key)
            expire_time = 0
            if expire != -1:
                expire_time = int(time.time())
            self.cache[key] = expire_time + expire
            self._storage[key] = value
        return True

    def delete(self, key):
        if len(self.cache) == 0:
            return True
        self.cache.pop(key)
        self._storage.delete(key)
        return True

    def clear(self):
        self.cache = OrderedDict()
        self._storage = type(self._storage)()
        return True

    def clear_timeout(self):
        for key in self.cache.keys():
            if self.cache[key] == -1:
                continue
            cur_time = int(time.time())
            if cur_time > self.cache[key]:
                self.delete(key)