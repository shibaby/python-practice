class Student(object):

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def get_name(self):
        return self.__name
        
    def set_name(self, name):
        self.__name = name
        
    def get_age(self):
        return self.__age
        
    def set_age(self, age):
        self.__age = age
    
    def print_stu(self):
        print('%s: %s' % (self.__name, self.__age))