from abc import ABCMeta, abstractmethod

# abstract class: 有一個或以上的 abstract method
class Product(metaclass=ABCMeta):
    @abstractmethod
    def price(self):
        pass

# abstract class不能創出實例，會出錯:
# TypeError: Can't instantiate abstract class Product with abstract method price
# p = Product()

# abstract class(寫來被繼承的，不能創實例)
class Animal(metaclass=ABCMeta):
    # abstract method(寫來被override)
    # 全部的abstract method都要override才行
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def my(self):
        pass


class Dog(Animal):
    def make_sound(self):
        print('Wang')

    def my(self):
        print('我是狗狗')


class Cat(Animal):
    def make_sound(self):
        print('Meow')

    def my(self):
        print('我是貓咪')

d = Dog()
c = Cat()

for animal in [d, c]:
    animal.make_sound()
    animal.my()
# Wang
# 我是狗狗
# Meow
# 我是貓咪
