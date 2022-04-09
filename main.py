# Flat List
nl = []

def flatten(ls):
    for i in ls:
        if(isinstance(i, list)):
            flatten(i)
        else:
            nl.append(i)


l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

flatten(l)

print(nl)
print("-------------------------------------------------")
# Reverse List

l2 = [0, [1, 2], [3, 4], [5, 6, 7], [8, [9,10],[11,12,[13,14]]]]

def reverse_list(ls):
    ls.reverse()
    for i in ls:
        if(isinstance(i, list)):
            reverse_list(i)

print("Before:", l2)
reverse_list(l2)
print("After:", l2)