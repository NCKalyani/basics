def palindrome(string):
  forward = ''.join(re.findall(r'[a-z]',string.lower()))
  backward = forward[::-1]
  return forward == backward
