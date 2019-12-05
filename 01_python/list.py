# list的使用
# 1.新建一个列表fruits
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# 新增一个元素
# append: 在list列表后增加元素
fruits.append("pear")  
print(fruits)
# insert: 指定位置增加元素
fruits.insert(0, "pear")
print(fruits)
# 指定元素的位置
# count：从1开始 
print(fruits.count("pear"))
print(fruits.count("apple"))
# 搞错了，这个不是指定元素的位置，这个是指定元素的个数
# index：从0开始
print(fruits.index("pear"))
print(fruits.index("pear", 6))  #从5开始计数，则pear出现的位置是在什么地方呢？

# list推导式
result = [len(fruit) for fruit in fruits]  # 显示的是所有水果的字符串大小
print(result)