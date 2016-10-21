from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import pymysql

bootstrap=Bootstrap()
db=SQLAlchemy()
login_manager=LoginManager()
login_manager.session_protection='strong'
login_manager.login_view='views_blueprint.login'

def create_app():
    app=Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:1111@localhost/devdb'
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
    app.config['SECRET_KEY']='42'
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    from views import views_blueprint
    app.register_blueprint(views_blueprint)
    from modelsAdmin import Admin
    @login_manager.user_loader
    def load_user(id):
        admin=Admin()
        if id==42:
            return admin
        else:
            return None
    return app

app=create_app()
'''
if __name__=='__main__':
    app=create_app()
    app.run(debug=True)
'''