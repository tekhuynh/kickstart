class Node:
    def __init__(self):
        self.children = dict()
        self.visits = 0
    
class Trie:
    def __init__(self):
        self.nodes = [0] * (2 * 10 ** 6)
        self.node = Node()
        self.index = 0
    def add_word(self, s):
        node = self.node
        while s:
            if not s[0] in node.children:
                self.nodes[self.index] = Node()
                node.children[s[0]] = self.index
                self.index += 1
            node.visits += 1
            node = self.nodes[node.children[s[0]]]
            s = s[1:]
        node.visits += 1

    def score(self, k):
        score = 0
        for n in range(self.index):
            score += int(self.nodes[n].visits / k)
        return score


def case():
    n, k = [int(x) for x in input().split()]
    t = Trie()
    for _ in range(n):
        t.add_word(input())
    return t.score(k)

t = int(input())
for i in range(1, t+1):
    print("Case #{}: {}".format(i, case()))