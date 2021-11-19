from rest_framework import fields, serializers
from . models import Category,Textbook,Novels


class Categoryserializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=(
            'id',
            'category'
        )


class Textbookserializer(serializers.ModelSerializer):
    class Meta:
        model=Textbook
        fields=(
            'id',
            'name',
            'price',
            'booktype',
            'pages',
            'date_created'
        )


class Novelsserializer(serializers.ModelSerializer):
    class Meta:
        model=Novels
        fields=(
            'id',
            'name',
            'price',
            'novelcategory',
            'pages',
            'date_created'
        )