import pytest
from wordmixer import mix_word


def test_mix_word():
    word = 'aaaa'
    actual = mix_word(word)
    assert len(word) == len(actual)
    for letter in word:
        assert letter in actual



# @pytest.fixture()
# def app():
#     app = create_app()
#     app.config.update({
#         "TESTING": True,
#     })

#     # other setup can go here

#     yield app

#     # clean up / reset resources here


# @pytest.fixture()
# def client(app):
#     return app.test_client()

# def test_request_example(client):
#     response = client.get("/posts")
#     assert b"<h2>Hello, World!</h2>" in response.data

