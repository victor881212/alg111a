# 作者 陳宏遠

#期中期末皆改自 演算法-王者歸來-參考書
---
期中    使用貪婪和遞迴完成
---
期中為backpack problem
依據 '商品', '商品價格 ','商品重量','商品數量'進行貪婪
每一次遞迴會優先選擇價值最高且物品數量大於0的物品進入背包，
然後會判斷剩下的商品是否還能塞入背包，如果不能就return
```python 
#參考書
# ch15_2.py                 
def greedy(things):
    ''' 商品貪婪演算法 '''
    length = len(things)                                    # 商品數量
    things_list = []                                        # 儲存結果
    things_list.append(things[length-1])                    # 第一個商品
    weights = things[length-1][1][1]
    for i in range(length-1, -1, -1):                       # 貪婪選商品
        if things[i][1][1] + weights <= max_weight:         # 所選商品可放入背包
            things_list.append(things[i])                   # 加入貪婪背包
            weights += things[i][1][1]                      # 新的背包重量               
    return things_list
            
things = {'iWatch手錶':(15000, 0.1),                        # 定義商品
          'Asus  筆電':(35000, 0.7),
          'iPhone手機':(38000, 0.3),
          'Acer  筆電':(40000, 0.8),          
          'Go Pro攝影':(12000, 0.1),
         }

max_weight = 1
th = sorted(things.items(), key=lambda item:item[1][0])     # 商品依價值排序  
print('所有商品依價值排序如下')
print('商品', '        商品價格 ',  ' 商品重量')
for i in range(len(th)):
    print("{0:8s}{1:10d}{2:10.2f}".format(th[i][0],th[i][1][0],th[i][1][1]))

t = greedy(th)                                              # 呼叫貪婪選商品
print('貪婪選擇商品如下')
print('商品', '        商品價格 ',  ' 商品重量')
for i in range(len(t)):
    print("{0:8s}{1:10d}{2:10.2f}".format(t[i][0],t[i][1][0],t[i][1][1]))
```
```python
#改進後
import math
def greedy(things,max_weight:float,numlist=[],things_list = [] ,weights=0 ):
    #print(f".......{weights}.......")
    ''' 商品貪婪演算法 '''
    length = len(things)                                    # 商品數量                                       # 儲存結果
    for j in range(length-1, -1, -1):                       # 貪婪選商品
        if (things[j][1][1] + weights) <= max_weight and numlist[j]>0:         # 所選商品可放入背包
            things_list.append(things[j])                   # 加入貪婪背包
            weights += things[j][1][1] # 新的背包重量
            numlist[j]-=1
            break                      #一次只塞一個，所以跳出迴圈
    for i in range(length-1,-1,-1):                         #檢查剩餘重量能否繼續塞東西
        if (round((max_weight-weights),10)>things[i][1][1] and numlist[i]>0):
            print(weights)
            print(round((max_weight-weights),10))
            things_list,weights,numlist=greedy(things,max_weight,numlist,things_list,weights)               #遞迴
    return things_list,weights,numlist
            
things = {'iWatch手錶':(15000, 0.1,100),                        # 定義商品假設商品可以無限取用
          'Asus  筆電':(35000, 0.7,5),
          'iPhone手機':(38000, 0.3,10),
          'Acer  筆電':(40000, 0.8,5),          
          'Go Pro攝影':(12000, 0.1,100),
          "gold      ":(10000000, 10,1)
         }

max_weight = 40
numlist=[]
th = sorted(things.items(), key=lambda item:item[1][0])     # 商品依價值排序  
print('所有商品依價值排序如下')
print('商品', '        商品價格 ',  ' 商品重量' , '商品數量')
for i in range(len(th)):
    print("{0:8s}{1:10d}{2:10.2f}{3:10d}".format(th[i][0],th[i][1][0],th[i][1][1],th[i][1][2]))    #將所有商品依價格print出
    numlist.append(th[i][1][2])
print(numlist)
t,weight,numlist = greedy(th,max_weight,numlist)                                              # 呼叫貪婪選商品
print('貪婪選擇商品如下')
print('商品', '        商品價格 ',  ' 商品重量')
print(weight)
for i in range(len(t)):
    print("{0:8s}{1:10d}{2:10.2f}".format(t[i][0],t[i][1][0],t[i][1][1]))   #將背包中儲存的商品print出
```
---
期末
---

