from rules.models import ClassType
from suricata.models import ConfSuricata, Suricata, SignatureSuricata, ScriptSuricata, SourceSuricata, RuleSetSuricata, AppLayerType
from rest_framework import serializers


class ClassTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassType
        fields = "__all__"


class ConfSuricataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfSuricata
        fields = "__all__"


class SuricataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suricata
        fields = "__all__"


class SignatureSuricataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignatureSuricata
        fields = "__all__"


class ScriptSuricataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScriptSuricata
        fields = "__all__"


class SourceSuricataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SourceSuricata
        fields = "__all__"


class RuleSetSuricataSerializer(serializers.ModelSerializer):
    class Meta:
        model = RuleSetSuricata
        fields = "__all__"


class AppLayerTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppLayerType
        fields = "__all__"
