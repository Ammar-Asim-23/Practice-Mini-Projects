class Fraction():
    def __init__(self,n,d):
        self.__num=n
        self.__den=d

    def __str__(self):
         return "{}/{}".format(self.__num,self.__den)


    def  simplify(num,den):
        if den != 0:
            self.__num=self.__num%self.__den
            self.den=self.__num//self.__den
        else:
             print(infinite)
          
        
    def __add__(self,other):
        temp_num=self.__num*other.__den + other.__num*self.__den
        temp_den=self.__den*other.__den
        simplify(temp_num,temp_den)
        return "{}/{}".format(temp_num,temp_den)

    def __sub__(self,other):
        temp_num=self.__num*other.__den - other.__num*self.__den
        temp_den=self.den*other.den
        simplify(temp_num,temp_den)
        return "{}/{}".format(temp_num,temp_den)

    def __mul__(self,other):
        temp_num=self.num*other.num
        temp_den=self.den*other.den
        simplify(temp_num,temp_den)
        return "{}/{}".format(temp_num,temp_den)

    def __truediv__(self,other):
        temp_num=self.num*other.den
        temp_den=self.den*other.num
        simplify(temp_num,temp_den)
        return "{}/{}".format(temp_num,temp_den)   
