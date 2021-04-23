import math

### Edit here ###
wektor = [1,2,3,4,5,6,7,8,9,10]
### _________ ###

def vector_sum(wektor):
    suma = 0
    for _ in wektor:
        suma = suma + _
    return suma


def vector_length(wektor):
    n = 0
    for _ in wektor:
        n = n + 1
    return n


def vector_average(wektor):
    return vector_sum(wektor) / vector_length(wektor)


def variance(wektor):
    average = vector_average(wektor)
    return sum((x - average) ** 2 for x in wektor) / vector_length(wektor)


def vector_standard_deviation(wektor):
        return math.sqrt(variance(wektor))


print("Dla wektora liczb", str(wektor))
print("Średnia wektora", str(vector_average(wektor)))
print("Odchylenie standardowe wektora", str(vector_standard_deviation(wektor)))

