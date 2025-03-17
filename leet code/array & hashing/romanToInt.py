def romanToInt(s):
  l = list(s)
  res = 0
  for i in range(0,len(l)):
        if l[i] == 'I':
          res += 1
        elif l[i] == 'V':
          res += 5
        elif l[i] == 'X':
          res += 10
        elif l[i] == 'L':
          res += 50
        elif l[i] == 'C':
          if l[i-1] == 'D':
            res += 500
          if l[i - 1] == 'M':
            res += 100
        elif l[i] == 'D':
          res += 500
        elif l[i] == 'M':
          res += 1000
        print(res)
  print(res)
if __name__ == '__main__':
  romanToInt("MCMXCIV")
  

  
  
  
  
  


