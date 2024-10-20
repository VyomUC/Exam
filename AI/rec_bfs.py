from collections import defaultdict

def rbfs(graph, start, f_limit, g_cost, heuristic):
  successors = []
  for (neighbor, cost) in graph[start]:
    g = g_cost + cost
    f = g + heuristic[neighbor] # f = g + h
    successors.append([neighbor, g, f])
  
  if len(successors) == 0: return None, float('inf')

  while True:
    successors.sort(key=lambda x:x[2])
    best = successors[0]
    if best[0] == "B": return [best[0]], best[2]
    
    alternate = successors[1][2] if len(successors) > 1 else float('inf')
    if best[2] > f_limit: return None, best[2]
    result, best[2] = rbfs(graph, best[0], min(f_limit, alternate), best[1], heuristic)

    if result: return [best[0]] + result, best[2]
    if best[2] > f_limit: return None, best[2]

def add(graph, u, v, cost):
  graph[u].append((v, cost))
  graph[v].append((u, cost))

def main():
  graph = defaultdict(list)
  add(graph, "A", "Z", 75)
  add(graph, "A", "T", 118)
  add(graph, "A", "S", 140)
  add(graph, "Z", "O", 71)
  add(graph, "O", "S", 151)
  add(graph, "T", "L", 111)
  add(graph, "L", "M", 70)
  add(graph, "M", "D", 75)
  add(graph, "D", "C", 120)
  add(graph, "S", "R", 80)
  add(graph, "S", "F", 99)
  add(graph, "R", "C", 146)
  add(graph, "C", "P", 138)
  add(graph, "R", "P", 97)
  add(graph, "F", "B", 211)
  add(graph, "P", "B", 101)
  add(graph, "B", "G", 90)
  add(graph, "B", "U", 85)
  add(graph, "U", "H", 98)
  add(graph, "H", "E", 86)
  add(graph, "U", "V", 142)
  add(graph, "V", "I", 92)
  add(graph, "I", "N", 87)

  heuristic = {
    "A":  366, "B": 0, "C": 160, "D": 242, "E": 161, "F": 178, "G": 77,
    "H": 151, "I": 226, "L": 244, "M": 241, "N": 234, "O": 380, "P": 98,
    "R": 193, "S": 253, "T": 329, "U": 80, "V": 199, "Z": 374
  }

  start = input("Enter start node: ")
  path, cost = rbfs(graph, start, float('inf'), 0, heuristic)
  if path:
    print(f"Path from {start}: {path}")
    print(f"Cost: {cost}")
  else: print("No path found")

if __name__ == '__main__': main()