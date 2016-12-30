#!/usr/bin/python

def reverse(text):
    x = len(text)-1
    text2 = []
    while x >= 0:
        text2.append(text[x])
        x=x-1
    print "".join(text2)
    return text2

reverse("Python!")
