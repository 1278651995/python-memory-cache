# coding=gbk
from abc import ABCMeta, abstractmethod

from memory_cache.storage import SimpleStorage

"""
������API
"""


class BaseCacheAPI(metaclass=ABCMeta):
    def __init__(self, storage=None, max_size=1024):
        """
        :param storage: �洢�࣬[storage.BaseStorage]
        :param max_size: Ĭ�ϴ洢����ڴ�Ϊ1024�ֽڵ�����
        """
        self._storage = storage if storage is not None else SimpleStorage()

    @abstractmethod
    def set(self, key, value, expire=-1):
        """
        �洢key-value����
        :param key: �洢��key
        :param value: �洢��key��Ӧ��ֵ
        :param expire: �洢��ʱʱ�䣬Ĭ���ǲ������
        """
        self._hash_storage[key] = value

    @abstractmethod
    def get(self, key):
        """
        ����keyȡֵ
        :param key: �洢�ļ�
        :return: value: ��ȡ��ֵ
        """
        return self._hash_storage.get(key, None)

    @abstractmethod
    def delete(self, key):
        """
        ɾ���洢�ļ�ֵ��
        :param key: ��
        :return: items: �洢�ļ���ֵ
        """
        value = self._hash_storage.get(key, None)
        del self._hash_storage[key]
        return value
