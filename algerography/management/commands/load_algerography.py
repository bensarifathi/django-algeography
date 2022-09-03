from typing import Any, Optional
from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from django.utils.translation import gettext as _


class Command(BaseCommand):
    help = 'Load algeria wilaya and daira data to the db'

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        try:
            call_command("loaddata", "wilaya.json")
            call_command("loaddata", "daira.json")
        except Exception:
            raise CommandError(_("Unexpected error occur"))
        
        self.stdout.write(self.style.SUCCESS(_('Algerography data successfully loaded')))
        