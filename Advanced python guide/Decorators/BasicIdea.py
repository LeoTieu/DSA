def mydecorator(function):

    def wrapper():
        '''Wraps the given function'''
        function()
        print("I am decorating your function!")
    
    return wrapper

def hello_world():
    print("Hello world")

mydecorator(hello_world)()