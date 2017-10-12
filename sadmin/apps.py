from django.apps import AppConfig


class SadminConfig(AppConfig):
    name = 'sadmin'

    # def ready(self):
    #     import sadmin.signals
    #     from django.contrib.auth import models as auth_model
    #     sadmin = auth_model.Group.objects.get_or_create(name="univhub_super_admin")[0]
    #     auth_model.Group.objects.get_or_create(name='univhub_moderator')
    #     auth_model.Group.objects.get_or_create(name="consultancy_admin")
    #     auth_model.Group.objects.get_or_create(name='consultancy_moderator')
    #     root = auth_model.User.objects.get_or_create(password="you get nothing",
    #                                                  email='paradox@localhost.com',
    #                                                  username='paradox',
    #                                                  is_staff=True
    #                                                  )[0]
    #     root.groups.add(sadmin);
    #     root.save()
