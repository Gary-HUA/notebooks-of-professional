## algorithms(趣味算法_陈小玉)

### Greedy algorithm

#### bubbling sort

~~~ python 
# to understand greedy_algorithm . bubble sort
lis = [10, 15, 5, 2, 8, 7, 35, 6, 4, 9, 1]  # data
tem = 0  # support space
#  start
if len(lis) > 0:  # judge list is null ?
    for i in range(len(lis)):
        for j in range(len(lis)-1-i):  # -i for  not match passed num
            if lis[j] > lis[j+1]:
                tem = lis[j]
                lis[j] = lis[j+1]
                lis[j+1] = tem
            j += 1
        i += 1
# end
print(lis)
~~~

#### 加勒比海盗船_最优装载问题

~~~python
~~~



