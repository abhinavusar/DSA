def bubble_sort(l):
    #for n elements there will be n-1 steps
    for i in range(1,len(l)):
    
      #for r th step there will be len(l)-r comparisons
      for j in range(0,len(l)-1):
    
        #if the next element is smaller then swap
        if l[j]>l[j+1]:
          temp=l[j]
          l[j]=l[j+1]
          l[j+1]=temp
    return l
