import pytest
from wordmixer import mix_word, app as wordapp
from test_unit_wordmixer import word



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
    nb_unique_letters = len(set(word))
    if nb_unique_letters > 1:
        assert word not in response.data.decode('utf-8')
    else :
        assert word in response.data.decode('utf-8')
    
    
