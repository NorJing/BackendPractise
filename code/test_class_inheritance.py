class A(object):
    def __init__(self, para):
        self.para = para
        print('A')

class B(A):
    def __init__(self, para):
        super(B, self).__init__(para)
        self.para = para
        print('B')

if __name__ == "__main__":
    # print A first, then print B
    b = B("para")