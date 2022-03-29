class Fraction():
    def __init__(self,n,d):
        self.__num=n
        self.__den=d

    def __str__(self):
         return "{}/{}".format(self.__num,self.__den)

    def decimal(self):
        return self.__num/self.__den
        
    def __add__(self,other):
        temp_num=self.__num*other.__den + other.__num*self.__den
        temp_den=self.__den*other.__den
        simplify(temp_num,temp_den)
        return "{}/{}".format(temp_num,temp_den)

    def __sub__(self,other):
        temp_num=self.__num*other.__den - other.__num*self.__den
        temp_den=self.__den*other.__den
        simplify(temp_num,temp_den)
        return "{}/{}".format(temp_num,temp_den)

    def __mul__(self,other):
        temp_num=self.__num*other.__num
        temp_den=self.__den*other.__den
        simplify(temp_num,temp_den)
        return "{}/{}".format(temp_num,temp_den)

    def __truediv__(self,other):
        temp_num=self.__num*other.__den
        temp_den=self.__den*other.__num
        simplify(temp_num,temp_den)
        return "{}/{}".format(temp_num,temp_den)   
