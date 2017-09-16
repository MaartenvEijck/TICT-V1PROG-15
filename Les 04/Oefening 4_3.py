def swap(lst):
    if len(lst)> 1:
        lst[0], lst[1]= lst[1], lst[0]
        return lst
lst = [1,2,3,4]

res = swap(lst)

print(res)

