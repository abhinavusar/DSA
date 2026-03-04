def binarysearch(arr,target):
  def search(arr,target,start,end):
    half = (start + end) // 2
    #condition for not found- start>end
    if start>end:
      return 'Not Found'
    else:
        if target==arr[half]:
          return half
        elif target<arr[half]:
          return search(arr,target,start,half-1)
        else:
          return search(arr,target,half+1,end)
  return search(arr,target,0,len(arr)-1)
