def insertionsort(arr):
  for i in range(1,len(arr)):
    index=i-1
    while index>=0 and arr[i]<arr[index]:
      arr[i],arr[index]=arr[index],arr[i]
      index-=1
  return arr

print(insertionsort([42,1,4,13,24,67,32,78]))
