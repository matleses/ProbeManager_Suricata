from suricata.models import Suricata
from django.forms import ModelForm, PasswordInput


class ProbeForm(ModelForm):
    class Meta:
        model = Suricata
        fields = ('name', 'description', 'configuration', 'rulesets', 'host', 'os', 'scheduled_enabled', 'scheduled_crontab', 'ansible_remote_user', 'ansible_remote_port', 'ansible_become', 'ansible_become_method', 'ansible_become_user', 'ansible_become_pass', 'ansible_ssh_private_key_file')
        widgets = {
            'ansible_become_pass': PasswordInput(),
        }
