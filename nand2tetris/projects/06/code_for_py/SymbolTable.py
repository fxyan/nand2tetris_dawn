class Symbol_Table():
    def __init__(self):
        self.dict = {}
        self.pre_deal()

    def addEntry(self, key, val):
        self.dict[key] = val

    def GerAddress(self, key):
        return self.dict.get(key, None)

    def pre_deal(self):
        self.dict['SP'] = self.deal_bin(0)
        self.dict['LCL'] = self.deal_bin(1)
        self.dict['ARG'] = self.deal_bin(2)
        self.dict['THIS'] = self.deal_bin(3)
        self.dict['THAT'] = self.deal_bin(4)
        self.dict['SCREEN'] = self.deal_bin(16384)
        self.dict['KBD'] = self.deal_bin(24576)
        self.dict['R0'] = self.deal_bin(0)
        self.dict['R1'] = self.deal_bin(1)
        self.dict['R2'] = self.deal_bin(2)
        self.dict['R3'] = self.deal_bin(3)
        self.dict['R4'] = self.deal_bin(4)
        self.dict['R5'] = self.deal_bin(5)
        self.dict['R6'] = self.deal_bin(6)
        self.dict['R7'] = self.deal_bin(7)
        self.dict['R8'] = self.deal_bin(8)
        self.dict['R9'] = self.deal_bin(9)
        self.dict['R10'] = self.deal_bin(10)
        self.dict['R11'] = self.deal_bin(11)
        self.dict['R12'] = self.deal_bin(12)
        self.dict['R13'] = self.deal_bin(13)
        self.dict['R14'] = self.deal_bin(14)
        self.dict['R15'] = self.deal_bin(15)

    def deal_bin(self, fn):
        difference = bin(fn)[2:]
        if len(difference) < 16:
            difference = '0' * (16 - len(difference)) + difference
        return difference


