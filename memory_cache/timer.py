# coding=gbk

"""
��ʱ��
"""
import threading


class Timer:
    def __init__(self, interval_time=5):
        self.interval_time = 5

    def do(self, func):
        func()
        timer = threading.Timer(self.interval_time, self.do)
        timer.start()
