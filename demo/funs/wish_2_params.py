def wish(msg, user):
    print(msg, user)


#Positional args
wish("Hi", "Rosum")
wish("Hello", "Anders")

# keyword args
wish(user="Joe", msg="Good morning")
wish("Hello", user = "Richard")

