class ClassTest:
    name = ''

    def __init__(self, name):
        self.name = name

    def printName(self):
        print(self.name)


if __name__ == '__main__':
    cls = ClassTest('classA')
    cls.printName()