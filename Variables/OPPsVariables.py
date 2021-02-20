class variabledef():
    vStaticVariable = 100
    print('This is int static variable which is printed from class: ', vStaticVariable)

    def __init__(self, vInstanceVariableCMD, vInstanceVariable=300):
        self.vInstanceVariable = vInstanceVariable
        self.vInstanceVariableCMD = vInstanceVariableCMD

    def method(cls):
        vLocalVariable = 200
        print('This is int static variable which is printed from method: ', cls.vStaticVariable)
        print('This is int local variable which is printed from method: ', vLocalVariable)

    def method_init(self):
        print('This is int instance variable which is printed from method: ', self.vInstanceVariable)
        print('This is int instance variable which is printed from method sent through CLI: ', self.vInstanceVariableCMD)
        print('This is int outside instance variable which is printed from method sent through CLI: ',
              self.vOutsideClassVariable)


# Instantiation of the class
vd = variabledef(400)
vd.vOutsideClassVariable = 500
print(vd.method())
print(vd.method_init())

