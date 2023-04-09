def print_bit_manip(a, b):
    print('a      ', bin(a), a)
    print('b      ', bin(b), b)
    print('bin a|b', bin(a|b), a|b)
    print()

    print('a      ', bin(a), a)
    print('b      ', bin(b), b)
    print('bin a&b', bin(a&b), a&b)
    print()

    print('a          ', bin(a), a)
    print('~b        ', bin(~b), ~b)
    print('bin a & ~b', bin(a & ~b), a & ~b)
    print()

    print('a           ', bin(a), a)
    print('-b         ', bin(~b), ~b)
    print('bin a & ~b ', bin(a & ~b))
    print()

    print("Set bit 2 of a to 1", bin(a | (1 << 2)), a | (1 << 2))
    print("Clear bit 2 of a to 0", bin(a & ~(1 << 2)), a & ~(1 << 2))
    print("Test bit 2 of a", (a & (1 << 2)) != 0)
    print("Extract last bit of a", bin(a & 1), bin(a & -a), bin(a & ~(a-1)))
    print("Remove last bit of a", bin(a & (a-1)))
   
if __name__ == '__main__':
    print_bit_manip(10, 13)
