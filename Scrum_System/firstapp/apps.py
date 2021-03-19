from django.apps import AppConfig


class FirstappConfig(AppConfig):
    name = 'firstapp'

class ProfilesConfig(AppConfig):
    name = 'profiles'
    def ready(self):
        import profiles.signals