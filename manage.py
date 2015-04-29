#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
from app import create_app, db
from app.models import User#, Role
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand


## Create app from configurate file 
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    #return dict(app=app, db=db, User=User, Role=Role)
    return dict(app=app, db=db, User=User)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


## 装饰器用于作为参数选项自动加载到 manager
@manager.command
def test():
    '''Run the Unit Tests.'''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()