#decorators
#@decorator_function just means diaplay = decorator_function(diaplay)

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("weapper executed this before {}".format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display():
    print("Display function ran")

@decorator_function
def display_info(name, age):
    print("Display function ran with arguments ({}, {})".format(name, age))

if __name__ == '__main__':
    display()
    print("/n/n")
    display_info('john', 25)
    
