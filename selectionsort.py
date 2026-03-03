def selection_sort(l):
  #for n elements , n-1 steps are required
  for i in range(len(l)-1):
    #assuming the i index to be smallest element
    index=i
    #element at index=i will be compared to elements from index i+1 to len(l)-1
    for j in range(i+1,len(l)):
      #if element at index j is smaller than element at index then change the value of index to j
      if l[index]>l[j]:
        index=j
    #swapping by tuple packing and unpacking
    l[i],l[index]=l[index],l[i]
  return l
