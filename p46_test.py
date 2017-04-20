itemsA = {"蘋果", "香蕉", "鳳梨", "芭樂"}
itemsB = {"鳳梨", "蘋果", "水梨", "蓮霧"}
temp1 = itemsA.union(itemsB)
temp2 = itemsA.intersection(itemsB)
temp3= temp1-temp2
#temp3 =temp1.difference(temp2)
lst =list(temp3)
lst.sort()
print(lst)
