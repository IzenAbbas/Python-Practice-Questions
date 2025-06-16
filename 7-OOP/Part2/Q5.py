class Student:
    def __init__(self):
        self.__student_id=None
        self.__marks=None
        self.__age=None

    def set_id(self, s_id):
        self.__student_id=s_id
    def get_id(self):
        return self.__student_id

    def set_marks(self,m):
        self.__marks=m
    def get_marks(self):
        return self.__marks

    def set_age(self,a):
        self.__age=a
    def get_age(self):
        return self.__age


    def validate_marks(self):
        if isinstance(self.__marks, (float, int)) and 0<=self.__marks<=100:
            return True
        return False

    def validate_age(self):
        if isinstance(self.__age, int) and self.__age>20:
            return True
        return False

    def check_qualification(self):
        if self.validate_age() and self.validate_marks() and self.__marks>=65:
            return True
        return False


