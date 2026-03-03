def modified_bubble_sort(L):
    for i in range(1,len(L)):
      count=0
      for j in range(0,len(L)-1):
        if L[j]>L[j+1]:
          temp=L[j]
          L[j]=L[j+1]
          L[j+1]=temp
        else:
          count+=1
      if count==len(L)-i:
        break
    return L
