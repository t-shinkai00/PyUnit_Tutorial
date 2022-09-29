import sys
from io import StringIO

import unittest

from main import main as func


class Test(unittest.TestCase):
  def setUp(self):
    self._captor = StringIO()
    sys.stdout = self._captor

  def tearDown(self):
    sys.stdout = sys.__stdout__

  def test1(self):
    in_ = open("case/test1.in", "r")
    out_ = open("case/test1.out", "r")
    func(in_.read())
    value = self._captor.getvalue()
    assert value == out_.read(), f"[ValueError] "
    in_.close()
    out_.close()

  def test2(self):
    in_ = open("case/test2.in", "r")
    out_ = open("case/test2.out", "r")
    func(in_.read())
    value = self._captor.getvalue()
    assert value == out_.read(), f"[ValueError] "
    in_.close()
    out_.close()


if __name__ == '__main__':
    unittest.main()