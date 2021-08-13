
""" wejscie: [4, 8, 9, 0, 12, 1, 4, 2, 12, 12, 4, 4, 8, 11, 12, 0]
# wyjscie: [0, 12], [4, 8], [4, 8], [11, 1], [12 ,0]
*/
"""

def solve(l):
  cnt = [0 for i in range(13)]
  # print(cnt)
  for e in l:
    cnt[e] += 1
  # print(cnt)


  res = []
  for e0 in range(7):
    e1 = 12 - e0

    for i in range(min(cnt[e0], cnt[e1]) if e0 != e1 else cnt[e0] // 2):
      res.append([e0, e1]) 
      # print(res)
  return res

def test_from_input():
  l = eval(input())
  print(*solve(l))

if __name__ == '__main__':
  print(*solve([1,11,6,6,6,4,8,5,7,7,5]), sep = ', ')
