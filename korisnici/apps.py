from django.apps import AppConfig


class KorisniciConfig(AppConfig):
    name = 'korisnici'

    def ready(self):
        import korisnici.signals
