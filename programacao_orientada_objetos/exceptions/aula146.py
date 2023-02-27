# Em Python criamos uma excessão dessa forma, só precisamos herdar a classe error e valeu

class MyError(Exception):
    ...


class OtherMyError(Exception):
    ...


def levantar():
    exception_ = MyError('a', 'b', 'c')
    # exception_.add_note('Olha a nota 1')  Só acontece no Python 11
    raise exception_

try:
    levantar()
except (MyError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error)
    exception_ = OtherMyError('Vou lançar dnv') 
    # exception_.__notes__ += error.__notes__.copy() Só acontece no Python 11
    # Add notas de error em uma nota
    raise exception_ from error