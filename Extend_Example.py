class Animal():
    def get_legs(self):
        print ('into get legs')

class Dog(Animal):
    def get_dog(self):
        print ('into get dog')

    def say_hau(self):
        print ('into say hau')


    def get_legs_dog(self,num_of_legs):
        print ('dog legs is ',num_of_legs)


class Cat():

    def get_cat(self):
        print('into get cat')


animal = Animal()
animal.get_legs()
rexy = Dog()
star = Dog()
miao = Cat()

rexy.get_legs_dog(4)
star.get_legs_dog(3)
rexy.say_hau()
star.say_hau()
rexy.get_legs()

