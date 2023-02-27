# Em Python criamos uma excessão dessa forma, só precisamos herdar a classe error e valeu

class MyError(Exception):
    ...


class OtherMyError(Exception):
    ...


def levantar():
    exception_ = MyError('a', 'b', 'c') 
    raise exception_

try:
    levantar()
except (MyError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error)
    exception_ = OtherMyError('Vou lançar dnv') 
    raise exception_ from error