#-*- utf-8 -*-
from nose.tools import *
from lexicon import parser   #from folder lexicon in project import python source parser.py

def test_peek():
	assert_equal(parser.peek(["test"]), "test")
	assert_equal(parser.peek(["321"]), "321")
	assert_equal(parser.peek([""]), "")
	assert_equal(parser.peek(["first", "second"]), "first")
	
def test_match():
	assert_equal(parser.match(["test1", "fest2"], "t"), "test1")
	assert_equal(parser.match(["fest1", "test2"], "t"), None)
	assert_equal(parser.match([], "test"), None)
	assert_equal(parser.match([], []), None)

def test_skip():
	assert_equal(parser.skip(["test1", "fest2", "test"], "t"), None)
	