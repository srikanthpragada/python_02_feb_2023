def details(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


def process(*args, **kwargs):
    pass


details(a=10, b=20)
details(x=10, y=20, z=30)
details(name="Python", version="3.10")
# details(10, 20)
process(10, 20, a=1, b=2)
