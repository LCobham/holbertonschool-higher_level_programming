#!/usr/bin/python3
def magic_string(li=[]):
    li.append(1)
    return "{}{}".format("BestSchool, " * (sum(li) - 1), "BestSchool")
