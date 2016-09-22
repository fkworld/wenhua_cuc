from flask_login import UserMixin

class Admin(UserMixin):
    def __init__(self):
        self._id=42

    def get_id(self):
        return self._id

    def get_self_object(self):
        return self
