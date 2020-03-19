#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def countdown(n):
    print("start.")
    while n > 0:
        print(n)
        yield n
        n -= 1
    print("Done!")


c = countdown(3)
next(c)
next(c)
next(c)
# next(c)
# next(c)
