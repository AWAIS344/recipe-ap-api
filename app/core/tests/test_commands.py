from unittest.mock import patch
from psycopg2 import OperationalError as Psycopg2error

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase

@patch("core.management.commands.wait_for_db.db.Command.check")
class CommandTests(SimpleTestCase):
    """Test the wait_for_db command"""

    def test_wait_for_db_ready(self,patched_check):
        """Test waiting for db when db is available"""
        patched_check.return_value = True
        call_command("wait_for_db")
        

        

