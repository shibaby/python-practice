class Person(object):

    #__slots__ = ('name', 'age') # 只允许给Person的实例添加name和age属性,使用__slots__后，指定的属性不能再有get/set方法 

    def speak(self):
        print('Person Can Speak ...')

    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, sex):
        self.__sex = sex

    @property
    def sex(self):
        return self.__sex

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name