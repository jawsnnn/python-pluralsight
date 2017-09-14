class Reader:
    def __init__(self, filename):
        self.filename = filename
        self.f = open(self.filename, 'r')

    def read(self):
        print(self.f.read())

    def close(self):
        self.f.close()
