class Greeter:

    def __init__(self):
        pass

    def enters(Self, is_boss, name):

        if (is_boss):
            print('Hello ' + name)

        else:
            print('Welcome ' + name)

    def greet(self):
        pass


if __name__ == "__main__":
    g = Greeter()
    persons = ['David', 'Joe', 'David1']
    is_manager = [True, True, False]

    persons_single = ['David_Single']
    is_manager_single = [True]

    assert len(persons) == len(is_manager), "tested lists size [is_manager VS persons] is not equals"

    if (len(persons) > 1):
        g.enters(is_manager[len(is_manager) - 1], persons[len(persons) - 1])

    else:
        g.enters(is_manager[0], persons[0])

    print(g.greet())
