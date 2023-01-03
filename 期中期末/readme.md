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
```python
#參考書範例
# ch15_4.py
def greedy(graph, cities, start):
    visited = []                                    # 儲存已拜訪城市
    visited.append(start)                           # 儲存起點城市
    start_i = cities.index(start)                   # 獲得起點城市的索引
    distance = 0                                    # 旅行距離
    for outer in range(len(cities) - 1):            # 尋找最近城市
        graph[start_i][start_i] = INF               # 將自己城市距離設為極大值
        min_dist = min(graph[start_i])              # 找出最短路徑
        distance += min_dist                        # 更新總路程距離        
        end_i = graph[start_i].index(min_dist)      # 最短距離城市的索引
        visited.append(cities[end_i])               # 將最短距離城市列入已拜訪
        for inner in range(len(graph)):             # 將已拜訪城市距離改為極大值
            graph[start_i][inner] = INF
            graph[inner][start_i] = INF
        start_i = end_i                             # 將下一個城市改為新的起點
    return distance, visited    
        
INF = 9999                                          # 距離極大值
cities = ['新竹', '竹南', '竹北', '關西', '竹東']
graph = [[0, 12, 10, 28, 16],                   #        '新竹', '竹南', '竹北', '關西', '竹東'             距離表
         [12, 0, 20, 35, 19],                   #   新竹
         [10, 20, 0, 21, 11],                   #   竹南
         [28, 35, 21, 0, 12],                   #   竹北
         [16, 19, 11, 12, 0]                    #   關西
        ]                                       #   竹東

dist, visited = greedy(graph, cities, '新竹')
print('拜訪順序 : ', visited)
print('拜訪距離 : ', dist)
```
```python
#改進後
def greedy(graph, cities, start,visited = [],distance = 0):
    visited.append(start)                           # 儲存起點城市
    start_i = cities.index(start)
    graph[start_i][start_i] = INF
    min_dist = min(graph[start_i])
    if(min_dist==INF):
        return distance, visited
    distance += min_dist
    end_i = graph[start_i].index(min_dist)
    for inner in range(len(graph)):             # 將已拜訪城市距離改為極大值
            graph[start_i][inner] = INF
            graph[inner][start_i] = INF
    distance,visited =greedy(graph,cities,cities[end_i],visited,distance)
    return distance, visited
        
INF = 9999                                          # 距離極大值
cities = ['新竹', '竹南', '竹北', '關西', '竹東']
graph = [[0, 12, 10, 28, 16],                   #        '新竹', '竹南', '竹北', '關西', '竹東'             距離表
         [12, 0, 20, 35, 19],                   #   新竹
         [10, 20, 0, 21, 11],                   #   竹南
         [28, 35, 21, 0, 12],                   #   竹北
         [16, 19, 11, 12, 0]                    #   關西
        ]                                       #   竹東

dist, visited = greedy(graph, cities, '新竹')
print('拜訪順序 : ', visited)
print('拜訪距離 : ', dist)
```

