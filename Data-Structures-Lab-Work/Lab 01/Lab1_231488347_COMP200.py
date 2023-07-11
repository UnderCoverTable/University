##TASK1

class Progression:

    def __init__(self, start=0):
        self._current = start

    def _advance(self):
        self._current += 1

    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        return self

    def print_progression(self, n):
        print(' '.join(str(next(self)) for j in range(n)))


class ArithmeticProgression(Progression):

    def __init__(self, increment=1, start=0):
        super().__init__(start)
        self._increment = increment

    def _advance(self):
        self._current += self._increment



class GeometricProgression(Progression):

    def __init__(self, base=2, start=1):
        super().__init__(start)
        self._base = base

    def _advance(self):
        self._current *= self._base


class FibobacciProgression(Progression):

    def __init__(self, first = 0, second = 1):
        super().__init__(first)
        self._prev = second - first

    def _advance(self):
        self._prev, self._current = self._current, self._prev + self._current

##TASK2

class ArithmeticABS(Progression):

    def __init__(self, first = 2, second = 200):
        super().__init__(first)
        self._prev = second - first

    def _advance(self):
        self._prev, self._current = self._current, abs(self._prev - self._current)


abs_test = ArithmeticABS(1,100)
abs_test.print_progression(10)


##TASK 3

from math import sqrt


class SQRT(Progression):

    def __init__(self, start=65536):
        super().__init__(start)
        self._current = start

    def _advance(self):
        self._current = sqrt(self._current)

tesr = SQRT()
tesr.print_progression(5)





