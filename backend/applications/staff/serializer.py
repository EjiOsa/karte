from django.db.models.enums import Choices
from rest_framework import serializers
from .models import *
from applications.master.models import Role
# from django.db.models import fields

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        # fields = '__all__'
        fields = ('id', 'name',)

class DoctorSerializer(serializers.ModelSerializer):
    # role = serializers.StringRelatedField()
    role = RoleSerializer(read_only = True)
    role_uid = serializers.PrimaryKeyRelatedField(queryset = Role.objects.filter(target = "DOCTOR"),
                                                write_only = True,
                                                label = "権限名",)

    # POST時に権限名の値をroleに渡すため、createメソッドをオーバーライド
    def create(self, validated_data):
        validated_data['role'] = validated_data.get('role_uid', None)

        if validated_data['role'] is None:
            raise serializers.ValidationError("role not found of CREATE.")

        del validated_data['role_uid']
        return Doctor.objects.create(**validated_data)

    # オーバーライドでは他の項目も必要なので、updateを継承して処理追加
    def update(self, instance, validated_data):
        instance.role = validated_data.get('role_uid', None)

        if instance.role is None:
            raise serializers.ValidationError("role not found of UPDATE.")

        del validated_data['role_uid']
        return super().update(instance, validated_data)

    class Meta:
        model = Doctor
        fields = ('last_name','first_name','last_name_kana','first_name_kana','age','sex','role','role_uid',)

class NurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nurse
        fields = ('last_name','first_name','last_name_kana','first_name_kana','age','sex','role',)

class PharmacistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacist
        fields = ('last_name','first_name','last_name_kana','first_name_kana','age','sex','role',)

class PhysicalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Physical
        fields = ('last_name','first_name','last_name_kana','first_name_kana','age','sex','role',)

class OccupationalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occupational
        fields = ('last_name','first_name','last_name_kana','first_name_kana','age','sex','role',)

class ClerkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clerk
        fields = ('last_name','first_name','last_name_kana','first_name_kana','age','sex','role',)
