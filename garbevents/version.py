# -*- coding: utf-8 -*-
__version__ = "1.1.4"

import os
import sys


def get_garb_events_version():
    pip_pkg_dir = os.path.join(os.path.dirname(__file__), "..", "..")
    pip_pkg_dir = os.path.abspath(pip_pkg_dir)

    return (
        'garbevents {} from {} (python {})'.format(
            __version__, pip_pkg_dir, sys.version[:3],
        )
    )


def show_version():
    sys.stdout.write(get_garb_events_version())
    sys.stdout.write(os.linesep)
    sys.exit()