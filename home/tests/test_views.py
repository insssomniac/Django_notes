import pytest

from django.contrib.auth.models import User

def test_home_endpoint_returns_welcome_page(client):
    response = client.get('/')
    assert  200 == response.status_code
    assert 'Welcome to SmartNotes' in str(response.content)

def test_signup_endpoint_returns_form_for_unauthenticated_user(client):
    response = client.get('/register/')
    assert 200 == response.status_code
    assert 'home/register.html' in response.template_name

@pytest.mark.django_db
def test_signup_endpoint_redirects_authenticated_user(client):
    user = User.objects.create_user(username='testuser', email='test@email.com', password='password')
    client.login(username='testuser', password='password')
    response = client.get('/register/', follow=True)
    assert  200 == response.status_code
    assert 'notes/notes_list.html' in response.template_name

