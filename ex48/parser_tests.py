from nose.tools import *
from ex48 import lexicon
from ex48.parser import *

def test_sentence():
	phrase = Sentence(('noun','player'),('verb','goes'),('direction','north'))
	assert_equal(phrase.subject, 'player')
	assert_equal(phrase.verb, 'goes')
	assert_equal(phrase.object, 'north')

def test_peek():
	assert_equal(peek([('verb','leave')]),'verb')
	assert_equal(peek([('noun','house')]),'noun')
	assert_equal(peek([('stop','the')]),'stop')
	assert_equal(peek([]),None)
	
def test_match():
	assert_equal(match([('verb','leave')],'verb'),('verb','leave'))
	assert_equal(match([('noun','house')],'noun'),('noun','house'))
	assert_equal(match([('stop','the')],'verb'),None)
	assert_equal(match([],'noun'),None)

def test_skip():
	word_list = [('noun','player'),('verb','goes'),('direction','north')]
	skip(word_list,'noun')
	assert_equal(word_list,[('verb','goes'),('direction','north')])
	word_list = [('noun','player'),('stop','the'),('direction','north')]
	skip(word_list,'stop')
	assert_equal(word_list,[('noun','player'),('stop','the'),('direction','north')])

def test_parse_verb():
	assert_equal(parse_verb([('stop','that'),('verb','goes'),('direction','north')]), ('verb','goes'))
	assert_raises(ParserError, parse_verb, [('stop','the')])
	
def test_parse_object():
	assert_equal(parse_object([('stop','that'),('direction','north')]), ('direction','north'))
	assert_equal(parse_object([('noun','player'),('stop','that')]), ('noun','player'))
	assert_raises(ParserError, parse_object, [('stop','the')])

def test_parse_subject():
	phrase = Sentence(('noun','player'),('verb','goes'),('direction','north'))
	temp = parse_subject([('verb','goes'),('direction','north')],('noun','player'))
	assert_equal(phrase.subject, temp.subject)
	assert_equal(phrase.verb, temp.verb)
	assert_equal(phrase.object, temp.object)

def test_parse_sentence():
	phrase1 = Sentence(('noun','player'),('verb','goes'),('direction','north'))
	phrase2 = Sentence(('noun','man'),('verb','goes'),('direction','north'))
	temp1 = parse_sentence([('stop','yo'),('verb','goes'),('direction','north')])
	temp2 = parse_sentence([('noun','man'),('verb','goes'),('direction','north')])
	
	assert_equal(phrase1.subject, temp1.subject)
	assert_equal(phrase1.verb, temp1.verb)
	assert_equal(phrase1.object, temp1.object)
	
	assert_equal(phrase2.subject, temp2.subject)
	assert_equal(phrase2.verb, temp2.verb)
	assert_equal(phrase2.object, temp2.object)
	
	assert_raises(ParserError, parse_sentence, [('stop','the')])
