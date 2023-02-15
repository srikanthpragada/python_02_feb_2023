def wish(*users, message="Hello"):
    for u in users:
        print(message, u)


wish("Steve", "Dave")
wish("Steve", "Dave", "Kevin")
wish("Tom", "Bob", message="Hi")
