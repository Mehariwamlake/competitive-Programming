class UnionFind:
    def __init__(self, N):
        self.parent = [i for i in range(N)]

    def root(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.root(self.parent[x])
        return self.parent[x]

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def connect(self, x, y):
        rootX = self.root(x)
        rootY = self.root(y)
        if rootX != rootY:
            self.parent[rootY] = rootX

n = int(input())
valya = input()
tolya = input()

graph = UnionFind(26)
spells = []
for i in range(n):
    if valya[i] == tolya[i]:
        continue
    Vnum = ord(valya[i]) - ord("a")
    Tnum = ord(tolya[i]) - ord("a")
    if graph.same(Vnum, Tnum):
        continue
    graph.connect(Vnum, Tnum)
    spells.append(valya[i] + " " + tolya[i])
print(len(spells))
print("\n".join(spells))
    	 	 		    				 	 	 								