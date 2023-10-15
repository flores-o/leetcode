"""
A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.

 

Example 1:

Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1
Example 2:

Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2
 

Constraints:

0 <= bank.length <= 10
startGene.length == endGene.length == bank[i].length == 8
startGene, endGene, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].
"""

from typing import List

class Solution:
    def is_neighbour_gene(self, gene1: str, gene2: str) -> bool:
        assert(len(gene1) == len(gene2))
        diff = 0
        for i in range(len(gene1)):
            if gene1[i] != gene2[i]:
                diff += 1
                if diff > 1:
                    return False
        return diff == 1
    
    def get_neighbour_genes_from_bank(self, gene: str, bank: List[str]) -> List[str]:
        neighbour_genes = []
        for bank_gene in bank:
            if self.is_neighbour_gene(gene, bank_gene):
                neighbour_genes.append(bank_gene)
        return neighbour_genes
    
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        queue = [(startGene, 0)]
        visited = set([startGene])
        while queue:
            current_gene, current_mutation_count = queue.pop(0)
            if current_gene == endGene:
                return current_mutation_count
            for neighbour_gene in self.get_neighbour_genes_from_bank(current_gene, bank):
                if neighbour_gene not in visited:
                    queue.append((neighbour_gene, current_mutation_count+1))
                    visited.add(neighbour_gene)
        return -1
    
if __name__ == '__main__':
    # Test cases
    startGene = "AACCGGTT"
    endGene = "AACCGGTA"
    bank = ["AACCGGTA"]
    print(Solution().minMutation(startGene, endGene, bank))
    assert(Solution().minMutation(startGene, endGene, bank) == 1)

    startGene = "AACCGGTT"
    endGene = "AAACGGTA"
    bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
    print(Solution().minMutation(startGene, endGene, bank))
    assert(Solution().minMutation(startGene, endGene, bank) == 2)
