import posixpath
from patchwork.files import exists


class virtualenv():
    def __init__(self, c, path, create_on_missing=False, recreate=False):
        self._c = c
        self._path = path
        self._create = create_on_missing
        self._recreate = recreate

    def __enter__(self):
        activate = posixpath.join(self._path, 'bin/activate')
        c = self._c
        path = self._path

        if not exists(c, activate) and not self._create:
            raise OSError("Cannot activate virtualenv %s" % path)

        elif not exists(c, activate) and self._create:
            create_virtual_env(self._c, self._path)

        elif self._recreate:
            remove_virtual_env(self._c, self._path)
            create_virtual_env(self._c, self._path)

        self._c.command_prefixes.append('. %s' % activate)
        return self

    def __exit__(self, type, value, traceback):
        self._c.command_prefixes.pop()

    def install(self, package):
        self._c.run("pip install {}".format(package))

    def download(self):
        raise NotImplementedError

    def uninstall(self):
        raise NotImplementedError

    def freeze(self):
        raise NotImplementedError

    def show(self):
        raise NotImplementedError

    def upgrade(self, package):
        self._c.run("pip install --upgrade {}".format(package))


def create_virtual_env(c, path):
    c.run("virtualenv {}".format(path))


def remove_virtual_env(c, path):
    c.run("rm -rf {}".format(path))
