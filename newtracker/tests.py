from django.test import LiveServerTestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest

class HomePageTest(LiveServerTestCase):
    
    def test_root_url_resolves_to_home_page_view(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'pages/home.html')
    
    def test_about_url_resolves_to_about_view(self):
        response = self.client.get('/about/')
        self.assertTemplateUsed(response, 'pages/about.html')
        
    def test_users_url_resolves_to_users_view(self):
        response = self.client.get('/users/', follow=True)
        print(response.redirect_chain[-1])
        self.assertRedirects(response, '/accounts/login/?next=/users/')
        
        
    