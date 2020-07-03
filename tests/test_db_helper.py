from unittest import TestCase
from unittest.mock import patch
import unittest 

from src.db_helper import DbHelper
y=DbHelper()

class TestHelper(unittest.TestCase):
     #@patch('db_helper.DbHelper')
     def test_max_salary_is_greater_than_min_salary(self):
          a=y.get_maximum_salary()
          b=y.get_minimum_salary()
          self.assertGreater(a.Salary.values[0],b.Salary.values[0])

x=TestHelper()
x.test_max_salary_is_greater_than_min_salary()
