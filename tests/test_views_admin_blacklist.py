""" venv/bin/python probemanager/manage.py test suricata.tests.test_views_admin_blacklist --settings=probemanager.settings.dev """
from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.utils import timezone

from suricata.models import BlackListSuricata


class ViewsBlacklistAdminTest(TestCase):
    fixtures = ['init', 'crontab', 'init-suricata', 'test-core-secrets', 'test-suricata-signature',
                'test-suricata-script', 'test-suricata-ruleset', 'test-suricata-source', 'test-suricata-conf',
                'test-suricata-suricata']

    def setUp(self):
        self.client = Client()
        User.objects.create_superuser(username='testuser', password='12345', email='testuser@test.com')
        if not self.client.login(username='testuser', password='12345'):
            self.assertRaises(Exception("Not logged"))
        self.date_now = timezone.now()

    def tearDown(self):
        self.client.logout()

    def test_blacklist(self):
        response = self.client.get('/admin/suricata/blacklistsuricata/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(BlackListSuricata.get_all()), 0)
        response = self.client.post('/admin/suricata/blacklistsuricata/add/', {'type': 'IP',
                                                                               'value': '192.168.0.1',
                                                                               'comment': 'test',
                                                                               'rulesets': [1, ]
                                                                               },
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(BlackListSuricata.get_all()), 1)
        response = self.client.post('/admin/suricata/blacklistsuricata/',
                                    {'action': 'delete_blacklist',
                                     '_selected_action': BlackListSuricata.get_by_value('192.168.0.1').id},
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(BlackListSuricata.get_all()), 0)
        response = self.client.post('/admin/suricata/blacklistsuricata/add/', {'type': 'HOST',
                                                                               'value': 'test.com',
                                                                               'comment': 'test',
                                                                               'rulesets': [1, ]
                                                                               },
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(BlackListSuricata.get_all()), 1)
        response = self.client.post('/admin/suricata/blacklistsuricata/',
                                    {'action': 'delete_blacklist',
                                     '_selected_action': BlackListSuricata.get_by_value('test.com').id},
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(BlackListSuricata.get_all()), 0)
        response = self.client.post('/admin/suricata/blacklistsuricata/add/',
                                    {'type': 'MD5',
                                     'value': 'e41c0631f6f2c138a417b59bcb880fce',
                                     'comment': 'test',
                                     'rulesets': [1, ]
                                     },
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(BlackListSuricata.get_all()), 1)
        response = self.client.post('/admin/suricata/blacklistsuricata/',
                                    {'action': 'delete_blacklist',
                                     '_selected_action': BlackListSuricata.
                                     get_by_value('e41c0631f6f2c138a417b59bcb880fce').id},
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(BlackListSuricata.get_all()), 0)
