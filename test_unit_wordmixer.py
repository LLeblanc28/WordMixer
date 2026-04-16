import pytest
from wordmixer import result
from wordmixer_service import MixWordService
import flask


# Comment faire pour tester avec d'autres valeurs ?
words = ['aaaa', 'abab', 'hello', '']

@pytest.mark.parametrize('word', words)
def test_mix_word(word):
    actual = MixWordService.mix_word(word)
    assert len(word) == len(actual)
    for letter in word:
        assert letter in actual
    nb_unique_letters = len(set(word))
    if nb_unique_letters > 1:
        assert word != actual
    else:
        assert word == actual


class MockArgs:
    
    def __init__(self, word):
        self.__word = word
        
    def get(self, *args, **kwargs):
        return self.__word

class MockRequest:
    
    def __init__(self, word):
        self.__word = word
        
    @property
    def args(self):
        return MockArgs(self.__word)

@pytest.mark.parametrize('word', words)
def test_mix_word_result(monkeypatch, word):
    monkeypatch.setattr(flask, 'request', MockRequest(word))
    monkeypatch.setattr(MixWordService, 'mix_word', lambda word: word)
    monkeypatch.setenv('SLEEP_TIME', 0)
    mix_word_result = result()
    assert word == mix_word_result

invalid_sleep_times = ['notvalid', -1, None]
@pytest.mark.parametrize('invalid_sleep_time', invalid_sleep_times)
def test_mix_word_result_invalid_sleep_time(monkeypatch, invalid_sleep_time):
    expected = ''
    monkeypatch.setattr(flask, 'request', MockRequest(expected))
    monkeypatch.setattr(MixWordService, 'mix_word', lambda word: word)
    monkeypatch.setenv('SLEEP_TIME', str(invalid_sleep_time))
    
    with pytest.raises(ValueError):
        result()
