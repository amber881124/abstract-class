from abc import ABCMeta, abstractmethod

# abstract class: 有一個或以上的 abstract method
class Product(metaclass=ABCMeta):
    @abstractmethod
    def price(self):
        pass

# abstract class不能創出實例，會出錯:
# TypeError: Can't instantiate abstract class Product with abstract method price
# p = Product()



