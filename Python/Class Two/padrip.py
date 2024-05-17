class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        if name == "최지훈":
            self._has_mother = False
            self._has_father = False
        else:
            self._has_mother = True
            self._has_father = True

    def myfunc(self):
        print("Hello my name is " + self.name + " and I am " + str(self.age) + " years old")

    def parents(self):
        if self._has_mother:
            print("I have a mother")
        else:
            print("I don't have a mother")
        if self._has_father:
            print("I have a father")
        else:
            print("I don't have a father")

    def __del__(self):
        print("Person object deleted")

    def parents_dead(self, mother, father):
        self._has_mother = mother
        self._has_father = father


p1 = Person("최지훈", 36)

p1.myfunc()
p1.parents()
