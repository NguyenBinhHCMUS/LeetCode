symbol = {'I':1, 'V':5, 'X':10, 'L':50, 'C': 100, 'D':500, 'M':1000}
def romanToInt(self, s: str):
  _sum = 0
  i = 0
  while(i < len(s)):
    _curr = symbol.get(s[i])
    if i == len(s) - 1:
      _sum += _curr
      break
    _next = symbol.get(s[i+1])        
    if _curr < _next:
      _sum = _sum + (_next - _curr)
      i += 1
    else:
     _sum += _curr
    i += 1
  return _sum