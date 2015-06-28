#-*- utf-8 -*-
from nose.tools import *
from lexicon import parser   #from folder lexicon in project import python source parser.py

def test_peek():
	assert_equal(parser.peek([("test", "1234"), ("test1", "4321")]), "test")
	assert_equal(parser.peek([("321", "test"), ("test1", "4321")]), "321")
	assert_equal(parser.peek([("")]), None)
	assert_equal(parser.peek([("first", "second"), ("second", "first")]), "first")
	
def test_match():
	assert_equal(parser.match([("test1", "fest2"),("test2", "4321")], "test1"), ("test1", "fest2"))
	assert_equal(parser.match([("fest1", "test2")], ("fest2", "test2")), None)
	assert_equal(parser.match([()], "test"), None)
	assert_equal(parser.match([()], ""), None)

def test_skip():
	tuple=[("test1", "fest2"),("test2", "fest3")]
	assert_equal(parser.skip(tuple, "test1"), None)
	assert_equal(parser.match(tuple, "test2"), ("test2", "fest3"))

def test_parse_verb():
	assert_equal(parser.parse_verb([("verb", "go")]), ("verb", "go"))
	assert_equal(parser.parse_verb([("stop", "here"), ("verb", "go")]), ("verb", "go"))
	assert_raises(parser.ParserError, parser.parse_verb, [("noun", "car")])
	assert_raises(parser.ParserError, parser.parse_verb,[("", "")])

def test_parse_object():
	assert_equal(parser.parse_object([("noun", "car")]), ("noun", "car"))
	assert_equal(parser.parse_object([("direction", "north"), ("noun", "car")]), ("direction", "north"))
	assert_equal(parser.parse_object([("stop","here"), ("noun", "car")]), ("noun", "car"))
	assert_equal(parser.parse_object([("stop","there"), ("direction", "north")]), ("direction", "north"))
	assert_raises(parser.ParserError, parser.parse_object, [("verb", "go")])
	assert_raises(parser.ParserError, parser.parse_object, [("stop", "here"), ("verb", "go")])

def test_parse_subject():
	src=parser.parse_subject([("verb", "go"), ("noun", "home")], ("subject", "I"))
	dest=parser.Sentence(("subject", "I"), ("verb", "go"), ("noun", "home"))
	assert_equal(src.verb, dest.verb)
	assert_equal(src.subject, dest.subject)
	assert_equal(src.object, dest.object)
	
	assert_raises(parser.ParserError, parser.parse_subject, [("direction", "north"), ("noun", "home")], ("subject", "I"))
	
def parse_sentence():
	src=parser.parse_sentence([("noun", "I"), ("verb", "go"), ("noun", "home")])
	dest=parser.Sentence(("subject", "I"), ("verb", "go"), ("noun", "home"))
	assert_equal(src.verb, dest.verb)
	assert_equal(src.subject, dest.subject)
	assert_equal(src.object, dest.object)
	
	src=parser.parse_sentence([("stop", "here"),("noun", "I"), ("verb", "go"), ("noun", "home")])
	dest=parser.Sentence(("subject", "I"), ("verb", "go"), ("noun", "home"))
	assert_equal(src.verb, dest.verb)
	assert_equal(src.subject, dest.subject)
	assert_equal(src.object, dest.object)
	
	src=parser.parse_sentence([("verb", "go"), ("noun", "home")])
	dest=parser.Sentence(("noun", "player"), ("verb", "go"), ("noun", "home"))
	assert_equal(src.verb, dest.verb)
	assert_equal(src.subject, dest.subject)
	assert_equal(src.object, dest.object)
	
	assert_raises(parser.ParserError, parser.parse_sentence, [("direction", "north"), ("noun", "home")], ("subject", "I"))