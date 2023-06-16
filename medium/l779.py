class Solution:
    def flipBits(self, num):
        num = 5
        bit_length = num.bit_length()
        mask = (1 << bit_length) - 1 - (1 << (bit_length - 1))
        flipped = num ^ mask
        flipped_binary = format(flipped, 'b').zfill(bit_length)
        return flipped_binary

    def constructNewRow(self, prev):
        prev = int(prev, 2)
        prevFlipped = self.flipBits(prev)
        newRow = str(prev) + str(prevFlipped)

    def kthGrammar(self, n: int, k: int) -> int:
        return self.constructNewRow('0')