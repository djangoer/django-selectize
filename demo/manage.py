#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo.settings")
    SELECTIZE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    sys.path.append(SELECTIZE_PATH)
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)