# 剑指offer (包括第一版和第二版) Python实现
**[牛客网](https://www.nowcoder.com/ta/coding-interviews?page=1)中只有第一版的题目，还没有更新第二版的题目，所以只有大部分题目在牛客中AC了，其他的题目大体都没有问题，如果有问题 welcome issue**

## 第二章
### [找出数组中重复的数字](https://github.com/Gustee/CodingInterview-Chinese-version2/blob/master/chap2/3_1.py)
在一个长度为n的数组李的所有数字都在0~n-1的范围内。
数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次
例：输入长度为7的数组[2,3,1,0,2,5,3] 对应的输出是重复的数字2或3

**思路**：
由于数组中数字的范围都在0~n-1，如果数组中没有重复的数字，那么数组排序之后数字i的数组下标也为i，
存在重复数字，则有些位置可能存在多个数字，有些位置没有数字
从头到尾依次扫描数组中的每个数字。当扫描到下标为i的数字时，首先比较这个数字m是不是等于i。
如果是，则继续扫描下一个数字；
如果不是，则再拿它和第m个数字进行比较，如果它和第m个数字相等就找到了一个重复的数字
如果它和第m个数字不相等，则把第i个数和第m个数交换，直到把m放到下标为m的位置

### [不修改数组找出重复的数字](https://github.com/Gustee/CodingInterview-Chinese-version2/blob/master/chap2/3_2.py)
在一个长度为n+1的数组里的所有数字都在1~n+1的范围内，所以数组中至少有一个数字是重复的。
找出数组中任意一个重复的数字， 但不能修改输入的数组

**思路**
我们把从1-n的数字从中间的数字m分为两部分，前面一半为1\~m,后面一半为m+1\~n。如果1~m区间的数字的数目超过m，那么这一半的区间里一定包含重复的数字；
否则，另一半m+1\~n的区间里一定包含重复的数字。那么可以继续把包含重复数字的区间二分，直到找到重复数字。
例：假设数组长度为10，若1\~5之间的数的数目小于等于5时，那么重复数字一定在6\~9之前


## [二维数组中的查找](https://github.com/Gustee/CodingInterview-Chinese-version2/blob/master/chap2/4.py)
在一个二维数组中，每一个都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
完成一个函数输入一个这样的数组和一个整数，判断数组中是否含有该整数

**思路**
因为数组中元素大小的排列方式，从数组的右上角开始查找
若比目标元素大，则向下查找
若比目标元素小，则向左查找


## [替换空格](https://github.com/Gustee/CodingInterview-Chinese-version2/blob/master/chap2/5.py)
请实现一个函数，把字符串中的每个空格替换成"%20".
例如，输入"we are happy." 则输出"we%20are%20happy"

## [从尾到头打印链表](https://github.com/Gustee/CodingInterview-Chinese-version2/blob/master/chap2/6.py)
输入一个链表的头节点，从尾到头反过来打印出每个节点的值

**思路**
将所有节点入栈，然后在依次弹出打印即可
或者使用递归的方式打印

## [重建二叉树](https://github.com/Gustee/CodingInterview-Chinese-version2/blob/master/chap2/7.py)
输入某个二叉树的前序遍历和中序遍历的结果，请重建该二叉树。
例如输入前序遍历序列[1,2,4,7,3,5,6,8]和中序遍历序列[4,7,2,1,5,3,8,6],
则重建如下图所示二叉树
     1
  2     3
4     5   6
  7      8

**思路**


## [二叉树的下一个节点](https://github.com/Gustee/CodingInterview-Chinese-version2/blob/master/chap2/8.py)
给定一颗二叉树和其中的一个节点，如何找出中序遍历序列的下一个节点。
树的节点出了有两个分别指向左、右子节点的指针，还有一个指向父节点的指针

**思路**
