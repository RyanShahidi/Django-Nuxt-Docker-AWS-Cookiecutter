from rest_framework import serializers, validators
from apps.accounts.models import CustomUser

class UserDisplaySerializer(serializers.ModelSerializer):
    email = serializers.CharField(
        write_only=True, validators=[validators.UniqueValidator(
            message='This email already exists',
            queryset=CustomUser.objects.all()
        )]
    )
    password = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser
        fields = ["email", "username", "password"]

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.save()
        return instance

class UserFunctionsMixin:
    def get_user(self, is_active=True):
        try:
            user = CustomUser._default_manager.get(
                is_active=is_active,
                **{self.email_field: self.data.get(self.email_field, "")},
            )
            if user.has_usable_password():
                return user
        except CustomUser.DoesNotExist:
            pass
        
class PasswordResetSerializer(serializers.Serializer, UserFunctionsMixin):
    default_error_messages = {
        "email_not_found": "User with given email does not exist."
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.email_field = 'email'
        self.fields[self.email_field] = serializers.EmailField()