#To check if a list is sorted or not
def sorted(ls,i=0):
    if i==len(ls)-1:
      return True
    else:
      if ls[i]<=ls[i+1]:
        i+=1
        return True and sorted(ls,i)
      else:
        return False
