def show_debug_toolbar(request):
    """
    Default method checks REMOTE_ADDR, which isn't set using domain sockets
    """

    if request.is_ajax():
        return False

    from django.conf import settings
    return bool(settings.DEBUG)


def management_command():

    import os
    import sys

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pycon_demo.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
