def insertion_sort(ls):
  for i in range(1,len(ls)):
    index=i-1
    while index>=0 and ls[index]>ls[i]:
      #swapping by tuple packing and unpacking
      ls[index],ls[i]=ls[i],ls[index]
      i-=1
      index-=1
  return ls

print(insertion_sort())
