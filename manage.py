from app import create_app, db
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app.models import User

app = create_app('development')

manager = Manager(app)
manager.add_command('server', Server)

@manager.shell

def shell():
    return dict(app = app, User=User)

# migrate = Migrate(app, db)
# manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()