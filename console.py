#!usr/bin/python
import datetime

class Car:
    def __init__(self, make, model, release_year):
        self.make = make
        self.model = model
        self.release_year = release_year

    def display_info(self):
        print(f"This is a car that has a {self.make} version, {self.model} model, and was made in {self.release_year}.")

car1 = Car("Toyota", "Corolla", 2015)
car1.display_info()
car2 = Car("Honda", "Civic", 2017)
car2.display_info()
     
class Extended(Car):
    def __init__(self, make, model,release_year):
        super().__init__(make, model, release_year)


    @classmethod
    def age(cls ,release_year):
        current_date = datetime.datetime.now()
        return current_date.year - release_year


    @staticmethod
    def is_vintage(release_year):
        vintage = Extended.age()
        if Vintage > 25:
            return True
        else:
            return False
Test = Extended("Toyota", "Corolla", 2015)
print(f"Age: {Extended.age(Test.release_year)} years")  # Example of class method usage
print(f"Is Vintage: {Extended.is_vintage(Test.release_year)}")