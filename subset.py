def subset(arr,i=0,res=[]):
  #base case
  if i==len(arr):
    print(res)
    return
  
  #to include
  res.append(arr[i])
  subset(arr,i+1,res)

  #to backtrack
  res.pop()

  #to exclude
  subset(arr,i+1,res)

subset([1,2,3])
