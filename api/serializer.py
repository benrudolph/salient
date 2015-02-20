from django.forms import widgets
from rest_framework import serializers
from salient.models import Doc, Volume, WordDoc

class WordDocSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordDoc
        fields = ('id', 'word_stemmed', 'word_raw', 'position')

class DocSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doc
        fields = ('id', 'name', 'volumes', 'user')


class DocBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doc
        fields = ('id', 'name')

class DocDetailSerializer(serializers.ModelSerializer):
    # worddoc_set = WordDocSerializer(many=True, read_only=True)

    class Meta:
        model = Doc
        fields = ('id', 'name', 'text')


class VolumeSerializer(serializers.ModelSerializer):
    doc_set = DocBasicSerializer(many=True, read_only=True)

    class Meta:
        model = Volume
        fields = ('id', 'name', 'doc_set', 'user')

