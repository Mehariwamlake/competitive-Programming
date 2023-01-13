def k_string():
  k =int(input())
  word = input()
  
  wordCount={}
  for w in word:
    wordCount[w] = wordCount.get(w,0)+1
  
  res = ''
  for key, value in wordCount.items():
      if value % k:
          return -1
          
      res += key*(value//k)
      return res*k
   
print(k_string())