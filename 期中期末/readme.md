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
---
期末
---

