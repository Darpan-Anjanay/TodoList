from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Todo
import pandas as pd
from datetime import datetime
from django.utils.timezone import make_aware
from io import BytesIO

class TodoTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.force_login(self.user)
        self.todo = Todo.objects.create(
            user=self.user,
            Title='Task',
            Description='Description',
            CompletionDate=make_aware(datetime(2025, 8, 20, 12, 0)),
            completionStatus=False,
        )

    def login(self):
        self.client.login(username='user', password='password')

    def test_home_page_requires_login(self):
        self.client.logout() 
        response = self.client.get(reverse('Home'))
        self.assertRedirects(response, reverse('Login') + '?next=/')


    def test_home_page_shows_tasks(self):
        
        response = self.client.get(reverse('Home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Task')

    def test_add_task_post(self):
        
        response = self.client.post(reverse('AddTask'), {
            'Title': 'Lorem',
            'Description': 'Lorem description',
            'CompletionDate': '2025-08-20',
            'completionStatus': 'on'
        })
        self.assertRedirects(response, reverse('Home'))
        self.assertEqual(Todo.objects.filter(user=self.user).count(), 2)

    def test_edit_task_post(self):
        
        response = self.client.post(reverse('AddTask') + f'?TID={self.todo.id}', {
            'Title': 'Updated Lorem Task',
            'Description': 'Updated Lorem Desc',
            'CompletionDate': '2025-08-12',
            'completionStatus': 'on'
        })
        self.assertRedirects(response, reverse('Home'))
        self.todo.refresh_from_db()
        self.assertEqual(self.todo.Title, 'Updated Lorem Task')
        self.assertTrue(self.todo.completionStatus)

    def test_delete_task(self):
        
        response = self.client.get(reverse('Delete') + f'?TID={self.todo.id}')
        self.assertRedirects(response, reverse('Home'))
        self.todo.refresh_from_db()
        self.assertTrue(self.todo.IsDelete)

    def test_register_user(self):
        response = self.client.post(reverse('Register'), {
            'username': 'darpan',
            'email': 'darpan@example.com',
            'password': 'pass1234',
            'password2': 'pass1234'
        })
        self.assertRedirects(response, reverse('Home'))
        self.assertTrue(User.objects.filter(username='darpan').exists())

    def test_login_view(self):
        response = self.client.post(reverse('Login'), {
            'username': 'testuser',
            'password': 'password'
        })
        self.assertRedirects(response, reverse('Home'))

    def test_logout_view(self):
        
        response = self.client.get(reverse('Logout'))
        self.assertRedirects(response, reverse('Login'))

    def test_excel_download(self):
        
        response = self.client.get(reverse('TaskasExcel'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    def test_excel_upload(self):
        df = pd.DataFrame([{
            'Title': 'Excel Task',
            'Description': 'From Excel',
            'CreatedAt': datetime(2025, 8, 10, 12, 0),
            'CompletionDate': datetime(2025, 8, 20, 12, 0),
            'CompletionStatus': 'Completed'
        }])
        excel_file = BytesIO()
        df.to_excel(excel_file, index=False)
        
        excel_file.seek(0)  
        excel_file.name = 'test.xlsx' 

        response = self.client.post(reverse('Upload'), {'file': excel_file}, format='multipart')

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Todo.objects.filter(Title='Excel Task').exists())
