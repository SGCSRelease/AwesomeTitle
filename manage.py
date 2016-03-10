#!env python

from os import urandom, makedirs
from os.path import abspath, dirname, exists, join

from flask_script import (
        Manager,
        prompt,
        prompt_bool,
        prompt_pass,
)
from flask_migrate import MigrateCommand
from jinja2 import Template

try:
    from AwesomeTitleServer import create_app
except ImportError:
    from . import create_app


app = create_app()
manager = Manager(app) #, with_default_commands=False)
manager.add_command('db', MigrateCommand)
_default = 'awesometitle'
_server = 'localhost'
_folder = 'datas/DOWNLOADED/'


@manager.command
def run():
    app.run(debug=True)

@manager.command
def config(
        mysql=None,
        username=_default,
        password=None,
        server=_server,
        database=_default,
        folder=_folder,
):
    """Generate config.py for AwesomeTitle.

    If there were some given parameters, those questions will be handled
    automatically.
    """
    # TODO : Is Existed config.py?

    base = dirname(abspath(__file__))
    if '.pex' in base:
        base = '.'

    # XXX : Check '-m' or '--mysql' options entered.
    if mysql is None:
        use_mysql = prompt_bool("Use MySQL?", default=True)
    else:
        if mysql == "True":
            use_mysql = True
        elif mysql == "False":
            use_mysql = False
        else:
            raise Exception("`-m` or `--mysql` needed `True` or `False`.")
    if use_mysql is True:
        # XXX : Check '-u' or '--username' options entered.
        if username is _default:
            username = prompt("MySQL DB Username", default=username)
        # XXX : Check '-p' or '--password' options entered.
        if not password:
            password = prompt_pass("MySQL DB Password")
        # XXX : Check '-s' or '--server' options entered.
        if server is _server:
            server = prompt("MySQL DB Server", default=server)
        # XXX : Check '-d' or '--database' options entered.
        if database is _default:
            database = prompt("MySQL DB Database", default=database)
    # XXX : Check '-f' or '--folder' options entered.
    if folder is _folder:
        folder = prompt("Image Upload Folder", default=folder)
    folder = join(base, folder)
    if not exists(folder):
        makedirs(folder)
    secret_key = urandom(24)
    output = "config.py"
    if exists("AwesomeTitleServer"):
        output = join("AwesomeTitleServer", output)
    with open("confs/config.py.tmpl") as tmpl:
        Template(
            tmpl.read()
        ).stream(
            base=base,
            username=username,
            password=password,
            server=server,
            database=database,
            folder=folder,
            secret_key=secret_key,
            use_mysql=use_mysql,
        ).dump(output)


def main():
    manager.run()


if __name__ == '__main__':
    main()
