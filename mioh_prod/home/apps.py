from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class HomeConfig(AppConfig):
    name = "mioh_prod.home"
    verbose_name = _("Home")

    def ready(self):
        try:
            import mioh_prod.home.signals  # noqa F401
        except ImportError:
            pass
