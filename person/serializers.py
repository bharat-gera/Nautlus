from rest_framework import serializers
from person.models import Profile,Person,ProfileImage
import re

class ProfileSerializer(serializers.ModelSerializer):
    person_name = serializers.CharField(max_length=255,source='owner.name',required=False)
    contact_num = serializers.CharField(max_length=10,required=False)
    about_yourself = serializers.CharField(max_length=150,required=False)
    
    class Meta:
        model = Profile
        fields = ('contact_num','state', 'country','about_yourself','person_name' )

    '''def validate_contact_num(self, value):
        phone_number = value
        phone_valid = re.compile( r'^(0)([1-9])([0-9]){8}$')
        match = phone_valid.search(str(phone_number))
        if match:
            return attrs
        else:
            raise serializers.ValidationError("Invalid Contact Number")'''


class ProfileImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileImage
        fields = ('image',)        

class PersonSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    profile_image = ProfileImageSerializer()
    
    class Meta:
        model = Person
        fields = ('email',  
                  'profile', 'profile_image',)        