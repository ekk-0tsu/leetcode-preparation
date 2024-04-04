# BFS solution
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        if end not in bank:
            return -1
        queue = [(start, 0)]
        while queue:
            gene, step = queue.pop(0)
            if gene == end:
                return step
            for i in range(len(gene)):
                # Why we need to iterate over 'ACGT'?
                # Because we can only change one character at a time
                for c in 'ACGT':
                    if c != gene[i]:
                        new_gene = gene[:i] + c + gene[i+1:]
                        if new_gene in bank:
                            queue.append((new_gene, step+1))
                            bank.remove(new_gene)
        return -1

# DFS solution

