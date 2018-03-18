""" venv/bin/python probemanager/manage.py test suricata.tests.test_tasks --settings=probemanager.settings.dev """
from django.test import TestCase

from core.tasks import reload_probe, deploy_rules
from suricata.tasks import upload_url_http
from suricata.models import Suricata, SourceSuricata


class TasksSuricataTest(TestCase):
    fixtures = ['init', 'crontab', 'test-core-secrets', 'test-suricata-signature', 'test-suricata-script', 'test-suricata-ruleset',
                'test-suricata-source', 'test-suricata-conf', 'test-suricata-suricata']

    @classmethod
    def setUpTestData(cls):
        pass

    # @skip
    def test_deploy_rules(self):
        suricata = Suricata.get_by_id(1)
        response = deploy_rules(suricata.name)
        self.assertEqual(0, response['result'])

    # @skip
    def test_reload_probe(self):
        suricata = Suricata.get_by_id(1)
        response = reload_probe(suricata.name)
        self.assertEqual(0, response['result'])

    # @skip
    def test_upload_url_http(self):
        source = SourceSuricata.get_by_id(1)
        response = upload_url_http(source.uri)
        self.assertIn('File uploaded successfully : ', response['upload_message'])
