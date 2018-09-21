from contextlib import contextmanager
import posixpath

from patchwork.files import exists

@contextmanager
def virtualenv(c, path):
    activate = posixpath.join(path, 'bin/activate')
    if not exists(c, activate):
        raise OSError("Cannot activate virtualenv %s" % path)
    with c.prefix('. %s' % activate):
        yield
