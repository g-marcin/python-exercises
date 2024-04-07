from custom_module.test import test
from custom_module.info_messages import info_messages
class Super():
    #class attr
    staticAttribute = info_messages["staticAttributeMsg"]
    #class constructor method
    def __init__(self):
        #constructor assigned instance attr
        self.instanceAttribute = info_messages["instanceAttributeMsg"]
    def method(self):
        #method assigned instance attr
        self.instanceAttribute = info_messages["instanceAttributeMsg"]
        return info_messages["methodMsg"]
    def delegate(self):
        self.action()
test(Super)

class Inheritor(Super):
    pass
test(Inheritor)

class Extender(Super):
    def method(self):
        Super.method(self)
        print('side effect!')
        return info_messages["methodMsg"]   
test(Extender)

class Provider(Super):
    def action(self):
        print('this is action implemented in Provider class')
test(Provider)

class Replacer(Super):
    def method(self):
        print('method replaced!')
        return info_messages["methodMsg"]   
test(Replacer)


if __name__ == '__main__':
    print('python process!')