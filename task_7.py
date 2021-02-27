class ComplexNumber:
    __Rez = 0
    __Imz = 0

    def __init__(self, rez, imz):
        self.__Rez = rez
        self.__Imz = imz

    def __add__(self, other):
        return ComplexNumber(self.__Rez + other.__Rez, self.__Imz + other.__Imz)

    def __mul__(self, other):
        rez = self.__Rez * other.__Rez - (self.__Imz * other.__Imz)
        imz = self.__Rez * other.__Imz + self.__Imz * other.__Rez
        return ComplexNumber(rez, imz)

    def __str__(self):
        return f'{self.__Rez} {"+" if self.__Imz > 0 else "-"} {abs(self.__Imz)}i'


cn1 = ComplexNumber(1, -1)
cn2 = ComplexNumber(3, 6)

print(cn1 + cn2)
print(cn1 * cn2)
