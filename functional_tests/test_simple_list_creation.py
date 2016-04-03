from selenium import webdriver
from .bse import FunctionalTest
from unittest import skip
import unittest
from django.test import LiveServerTestCase
from selenium.webdriver.common.keys import Keys
import time

class NewVisitorTest(FunctionalTest):
    def test_can_start_a_list_and_retive_it_later(self):
        pass




if __name__=='__main__':
    unittest.main(warnings='ignore')
