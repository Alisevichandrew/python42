# class Table:
#     def __init__(self, w, h, l):
#         self.height = h
#         self.width = w
#         self.lenght = l
    
#     def set_places(self, p):
#         return p

# class WorkTable(Table):
#     def square(self):
#         return self.width * self.lenght
    
#     def set_places(self, p):
#         self.places = p
#         return super().set_places(p)

# class KitchenTable(WorkTable):
#     def set_places(self, p):
#         p = super().set_places(p) * 2
#         return p

# kt = KitchenTable(1, 2, 3)
# print(kt.set_places(10))

# wt = WorkTable(3,2,1)
# print(wt.square())

# class IncapsTest:

#     def __init__(self, value):
#         self.__private_value = value

#     @property
#     def privat_value(self):
#         return self.__private_value
    
#     @privat_value.setter
#     def privat_value(self, val):
#         self.__private_value = val

# p = IncapsTest(1234)
# print(p.privat_value)
# p.privat_value = 43212
# print(p.privat_value)

class Point:
    def __init__(self, *args):
        for arg in args:
            if type(arg) not in (float, int):
                raise ValueError('Invalid argument')
        self.__point = args

    def __repr__(self):
        return f'Point {self.__point}'

    @property
    def shape(self):
        return len(self.__point)
    
    def get_choords(self):
        return self.__point
    
    def dst(self, choord):
        if type(choord) != Point:
            raise ValueError('Invalid type')
        if choord.shape != self.shape:
            raise ValueError('Incorrect shape')
        
        sum = 0
        for (x1, x2) in zip(choord.get_choords(), self.get_choords()):
            sum += (x1 - x2) ** 2
        
        return sum ** 0.5

    def dst_0(self):
        args = tuple([0] * self.shape)
        p0 = Point(*args)
        return self.dst(p0)


class Line:

    def __init__(self, p1, p2):
        point1 = Point(*p1)
        point2 = Point(*p2)
        if point1.shape != point2.shape:
            raise ValueError('Incorrect shape')
        self.first_point = point1
        self.second_point = point2
    
    def dst(self):
        return self.first_point.dst(self.second_point)
    
    def parallel_move(self):
        for i in range(0, self.first_point.shape):
            self.second_point[i] -= self.first_point[i]
            self.first_point[i] = 0
    
    def __repr__(self):
        return f'Line: Start {self.first_point} and Finish {self.second_point}'

# p1 = Point(6, 9)
# p2 = Point(0, 0)
# print(p1.dst(p2))
# print(p1.shape)

l = Line((1, 2, 3), (2, 4, 6))
l.parallel_move()
print(l)