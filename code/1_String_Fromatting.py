n = 17

# format을 이용하여 10진수 , 2진수, 8진수를 변경함
width = len("{0:b}".format(n))
for i in range(1,n+1):
  print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))