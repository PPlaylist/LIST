import random

class SBox:
    def __init__(self, blank_n):
        self.blank_n = blank_n
        self.blanks = sorted(random.sample(range(0x100),self.blank_n))
        self._generate()

    def _rand(self):
        return [0,1][random.random() > 0.5]

    def _xor(self, l):
        result = 0
        for x in l:
            result ^= x
        return result

    def _bits_to_int(self,l):
        l = l[::-1]
        res = 0
        for b in l:
            res = (res<<1) | b
        return res

    def _int_to_bits(self,x):
        return [int(b) for b in bin(x)[2:].zfill(8)][::-1]

    def _generate_yPoly(self):
        yPoly = []
        while len(yPoly) != 8:
            tmp = [self._rand() for _ in range(8)]
            if tmp not in yPoly:
                yPoly.append(tmp)
        return yPoly

    def _generate_SBox(self):
        sbox = [-1 for _ in range(0x100)]
        for i in range(0x100):
            if i in self.blanks:
                continue
            x = self._int_to_bits(i)
            y = [ self._xor([a*b for a,b in zip(x,poly)]) for poly in self.yPoly ]
            y_int = self._bits_to_int(y)
            sbox[i] = y_int
        return sbox

    def _generate(self):
        self.yPoly = self._generate_yPoly()
        self.sbox = self._generate_SBox()
        if not self._check():
            self._generate()

    def set_blanks(self, values):
        try:
            assert all([0x00<=v<0x100 for v in values])
            assert all([v not in self.sbox for v in values])
            assert len(values) == len(set(values))
            assert len(values) == self.blank_n
        except AssertionError:
            print('*** fail to complete the sbox ***')
            exit()

        for blank, value in zip(self.blanks, values):
            self.sbox[blank] = value

    def reset_blanks(self):
        for b in self.blanks:
            self.sbox[b] = -1

    def print(self):
        print("="*79)
        for i in range(16):
            for j in range(16):
                x = self.sbox[i*16+j] 
                if x == -1:
                    print('____',end=' ')
                    continue
                print('0x'+hex(x)[2:].zfill(2), end=' ')
            print()
        print("="*79)

    def __getitem__(self, key):
        return self.sbox[key]
    
    def index(self, item):
        return self.sbox.index(item)

    def _check(self):
        t = []
        for i in self.sbox:
            if i == -1:
                continue
            t.append(i)
        return len(t) == len(set(t)) 
    