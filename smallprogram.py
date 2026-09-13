from abc import ABC, abstractmethod


class a(ABC):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def should_pass(self):
        """Return True when the value meets the success condition."""
        raise NotImplementedError

    @abstractmethod
    def message(self):
        """Return a readable outcome message."""
        raise NotImplementedError

    def run(self):
        result = self.should_pass()
        return self.message(result)


class ScoreChecker(a):
    def should_pass(self):
        return self.value > 50

    def message(self, result):
        return "pass" if result else "fail"


checker = ScoreChecker(30)
print(checker.run())

print("hemnth reddy")