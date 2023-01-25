#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    res = []
    for i in range(list_length):
        try:
            if i >= min(len(my_list_1), len(my_list_2)):
                raise IndexError

            if my_list_2[i] == 0:
                raise ZeroDivisionError

            cond1 = isinstance(my_list_1[i], (int, float))
            cond2 = isinstance(my_list_2[i], (int, float))
            if not (cond1 and cond2):
                raise ValueError

            res.append(my_list_1[i] / my_list_2[i])

        except IndexError:
            res.append(0)
            print("out of range")

        except ValueError:
            res.append(0)
            print("wrong type")

        except ZeroDivisionError:
            res.append(0)
            print("division by 0")

        finally:
            continue
    return res
