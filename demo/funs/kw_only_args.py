# keyword-only args
def wish(*, message, name):
    print(message, name)


# wish("Garry", "Hi")
wish(message="Hello", name='Larry')
