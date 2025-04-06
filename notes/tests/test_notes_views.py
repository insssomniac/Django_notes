import pytest

from notes.tests.factories import UserFactory, NoteFactory

@pytest.fixture
def logged_user(client):
    user = UserFactory()
    client.login(username=user.username, password='password')
    return user

@pytest.mark.django_db
def test_list_endpoint_return_user_notes(client, logged_user):
    note1 = NoteFactory(user=logged_user)
    note2 = NoteFactory(user=logged_user)

    response = client.get('/smart/notes/')
    assert 200 == response.status_code
    content = str(response.content)
    assert note1.title in content
    assert note2.title in content
    assert 2 == content.count('<h3>')

@pytest.mark.django_db
def test_list_endpoint_only_list_notes_from_authenticated_user(client, logged_user):
    note1 = NoteFactory()

    user2 = UserFactory.create()
    client.login(username=user2.username, password='password')

    note2 = NoteFactory(user=user2)

    response = client.get('/smart/notes/')
    assert 200 == response.status_code
    content = str(response.content)

    assert note1.title not in content
    assert note2.title in content
