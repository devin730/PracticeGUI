#!/usr/bin/python
# encoding: UTF-8
#
# @module yield
#
# @author: Zengming Deng
#
# @description:
#
# @since: 2020-03-03 15:25:53
# -------------------------------

def yield_test(n):
    for i in range(n):
        yield call(i)
        print("i=", i)
    print("do something")
    print("end.")

def call(i):
    return i*2

# 使用for循环
# for i in yield_test(5):
#     print("main: ", i)
