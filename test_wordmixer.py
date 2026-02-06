import pytest
from wordmixer import mix_word, app as wordapp

word = ['aaaa','abab','hello']
@pytest.mark.parametrize('word', ['aaaa','abab','hello'])
def test_mix_word(word):
    actual = mix_word(word)
    assert len(word) == len(actual)
    for letter in word:
        assert letter in actual
    assert word != actual



@pytest.fixture()
def app():
    wordapp.config.update({
        "TESTING": True,
    })

    yield wordapp


@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.mark.parametrize('word', word)
def test_mix(client, word):
    response = client.get(f"/mix?word={word}")
    assert word not in response.data.decode('utf-8')

