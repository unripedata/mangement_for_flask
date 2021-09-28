#!/usr/local/bin/python3
#-*- encoding: utf-8 -*-
import threading


class ThreadDev:
    _instance = None
    _job = {}

    def __new__(cls):
        if not cls._instance:
            cls._instance = object.__new__(cls)
        return cls._instance

    def run(cls, name, function, arg):
        if not cls.alive(name):
            if name in cls._job:
                del cls._job[name]
        if not cls._job.get(name):
            t = threading.Thread(target=function, args=arg)
            t.daemon = True
            cls._job[name] = t
            cls._job[name].start()

    def alive(cls, name):
        if cls._job.get(name):
            return cls._job.get(name).is_alive()
        else:
            return False

    def getThread(cls):
        return cls._job
