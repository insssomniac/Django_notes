import pytest

from django.contrib.auth.models import User
from notes.models import Notes

@pytest.mark.django_db
def test_list_endpoint_return_user_notes(client):
    user = User.objects.create_user(username='testuser', email='test@email.com', password='password')
    client.login(username='testuser', password='password')

    Notes.objects.create(title='Test note', text='Test text', user=user)
    Notes.objects.create(title='Test note 2', text='Test text 2', user=user)

    response = client.get('/smart/notes/')
    assert 200 == response.status_code
    content = str(response.content)
    assert 'Test note' in content
    assert 'Test text' in content
    assert 'Test note 2' in content
    assert 'Test text 2' in content
    assert 2 == content.count('<h3>')

@pytest.mark.django_db
def test_list_endpoint_only_list_notes_from_authenticated_user(client):
    john = User.objects.create_user(username='john', email='john@email.com', password='password')
    Notes.objects.create(title="Johns note", text='Test text', user=john)

    clara = User.objects.create_user(username='clara', email='clara@email.com', password='password')
    Notes.objects.create(title="Claras note", text='Test text 2', user=clara)

    client.login(username='clara', password='password')

    response = client.get('/smart/notes/')
    assert 200 == response.status_code
    content = str(response.content)
    assert "Johns note" not in content
    assert "Claras note" in content
