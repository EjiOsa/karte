from rest_framework import serializers
from .models import *
from applications.master.models import Role
# from django.db.models import fields

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        # fields = '__all__'
        fields = ('id', 'name',)

class StaffSerializer(serializers.ModelSerializer):
    """スタッフ共通シリアライザ"""
    # role関連はスタッフ共通なので、親クラスとして作成
    # role_uidは各職種によって変わるので関数化

    role = RoleSerializer(read_only = True)
    def make_role_uid(self, target):
        role_uid = serializers.PrimaryKeyRelatedField(queryset = Role.objects.filter(target = target),
                                                write_only = True,
                                                label = "権限名",)
        return role_uid

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

class DoctorSerializer(StaffSerializer):
    role_uid = StaffSerializer().make_role_uid("Doctor")
    class Meta:
        model = Doctor
        fields = ('last_name','first_name','last_name_kana','first_name_kana','age','sex','role','role_uid',)

class NurseSerializer(StaffSerializer):
    role_uid = StaffSerializer().make_role_uid("Nurse")
    class Meta:
        model = Nurse
        fields = ('last_name','first_name','last_name_kana','first_name_kana','age','sex','role','role_uid',)

class PharmacistSerializer(StaffSerializer):
    role_uid = StaffSerializer().make_role_uid("Pharmacist")
    class Meta:
        model = Pharmacist
        fields = ('last_name','first_name','last_name_kana','first_name_kana','age','sex','role','role_uid',)

class PhysicalSerializer(StaffSerializer):
    role_uid = StaffSerializer().make_role_uid("Physical")
    class Meta:
        model = Physical
        fields = ('last_name','first_name','last_name_kana','first_name_kana','age','sex','role','role_uid',)

class OccupationalSerializer(StaffSerializer):
    role_uid = StaffSerializer().make_role_uid("Occupational")
    class Meta:
        model = Occupational
        fields = ('last_name','first_name','last_name_kana','first_name_kana','age','sex','role','role_uid',)

class ClerkSerializer(StaffSerializer):
    role_uid = StaffSerializer().make_role_uid("Clerk")
    class Meta:
        model = Clerk
        fields = ('last_name','first_name','last_name_kana','first_name_kana','age','sex','role','role_uid',)
