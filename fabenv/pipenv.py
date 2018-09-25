import posixpath


class pipenv():
    def __init__(self, c, path):
        self._c = c
        self._path = path

    def __enter__(self):
        activate = posixpath.join(self._path, 'bin/activate')
        self._c.command_prefixes.append('. %s' % activate)
        return self

    def __exit__(self, type, value, traceback):
        self._c.command_prefixes.pop()

    def install(self):
        raise NotImplementedError

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
