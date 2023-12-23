# This is a function
def say_hello_to(name, ending="!"):
    # Prints a hello message with the ending punctuation
    print('Hello ' + name + ending)


# Let's say hello to the Silva family!
say_hello_to("Dad")
say_hello_to("Mom")
say_hello_to("Caleb")
say_hello_to("Mason")
say_hello_to("Carter")
say_hello_to("Logan")


# or we can use a for loop and turn 6 lines of code into 3
silva_family = ["Dad", "Mom", "Caleb", "Mason", "Carter", "Logan"]
for persons_name in silva_family:
    say_hello_to(persons_name)


# The function has an optional argument which can come in handy
say_hello_to("the creepy guy looking in the window", "?")