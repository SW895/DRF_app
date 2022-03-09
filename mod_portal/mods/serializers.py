from ast import Mod
from rest_framework import serializers
from mods.mods_models.author import Author
from mods.mods_models.mod import Mods
from mods.mods_models.mod_category import Mod_Category, ModCategory

class ModCategorySerializer(serializers.HyperLinkedModelSerializer):
    mods = serializers.HyperlinkedRelatedField(
        many = True,
        read_only = True,
        view_name = 'mod-detail'
    )

    class Meta:
        model = ModCategory
        fields = (
            'url',
            'pk',
            'name',
            'mods'
        )

class ModSerializer(serializers.HyperlinkedModelSerializer):
    mod_category = serializers.SlugRelatedField(queryset=ModCategory.objects.all(), slug_field='name')
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Mods
        fields = (
            'url',
            'name',
            'mod_category',
            'descr_short',
            'descr_long',
            'date_created',
            'date_updated',
            'game_version',
            'download_count',
        )

class AuthorSerializer(serializers.HyperlinkedModleSerializer):
    
    class Meta:
        model = Author
        fields = (
            'url',
            'name'
        )