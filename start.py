from flask import Flask
from flask_login import LoginManager

from modelsAdmin import Admin
from views import views_blueprint

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'views_blueprint.login'


def create_app():
    app=Flask(__name__)
    login_manager.init_app(app)
    app.register_blueprint(views_blueprint)


    @login_manager.user_loader
    def load_user(id):
        admin=Admin()
        if id==42:
            return admin
        else:
            return None
            
    return app

#app=create_app()
if __name__=='__main__':
    app=create_app()
    app.run(debug=True)