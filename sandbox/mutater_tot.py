def ready(betty):
  print(len(betty))
  betty[0].append(betty)
  return betty[0:1]

def get_set(s):
  ready(s)
  return s.pop()

def go(on, up):
    if up:
        return go(on[0], up -1)
    else:
        return on

f = [1, [2]]
g = [[3, 4], [5], 6]
h = [g, g]
  
