from person import Person

class Manager(Person):
    def giveRaise(self, percent, bonus=0.1):
        self.pay *= (1.0 + percent + bonus)
if __name__ == '__main__':
    tom = Manager(name='Tom Doe', age=50, pay=50000)
    print(tom.lastName())
    tom.giveRaise(.20)
    print(tom.pay)


#It inherits
#the constructor and last-name methods from its superclass, but it customizes just the
#giveRaise method
#Because this change is being added as a new subclass, the original Person class, and any
#objects generated from it, will continue working unchanged. Bob and Sue, for example,
#inherit the original raise logic, but Tom gets the custom version because of the class
#from which he is created.