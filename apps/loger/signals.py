from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from apps.loger.models import Log
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.signals import user_logged_in


# @receiver(signal=pre_save, sender=User)
# def login_user_profile(sender, instance, **kwargs):
#     object_ide = instance.id
#     print(instance)
#     print(instance.check())
#     print(object_ide)
#     print(sender)
#     content = ContentType.objects.get(model='user')
#     Log.objects.create(user=instance, action_type='logging', content_type=content, object_id=object_ide)


@receiver(signal=post_save)
def login_user_profile(sender, instance, **kwargs):

    object_ide = instance.id
    action_type = False
    if isinstance(instance, User):
        if instance._last_name != instance.last_name:
            action_type = 'change_last_name'

        elif instance._last_login != instance.last_login:
            action_type = 'logging'

        if action_type:
            print('log')
            print(type(instance))
            content = ContentType.objects.get(model='user')
            Log.objects.create(user=instance, action_type=action_type, content_type=content, object_id=object_ide)