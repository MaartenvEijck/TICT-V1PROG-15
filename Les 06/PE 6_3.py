invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
lst = invoer.split('-')
lst = [int(i) for i in lst]
print(max(lst))
print(min(lst))
print(len(lst))
print(sum(lst))
