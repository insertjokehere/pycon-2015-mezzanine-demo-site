def management_command():

    import os
    import sys

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pycon_demo.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
