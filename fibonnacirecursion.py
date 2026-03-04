#n th term of fibonnaci series (n>0)
def fibonnaci(n):
  if n==1:
    return 0
  elif n==2:
    return 1
  else:
    return fibonnaci(n-1)+fibonnaci(n-2)

print(fibonnaci(10))
