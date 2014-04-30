from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
    id = db.Column('id', db.Integer, primary_key = True)
    username = db.Column('username', db.String(64), index = True, unique = True)
    email = db.Column('email', db.String(120), index = True, unique = True)
    password = db.Column('password', db.String(120))
    role = db.Column('role', db.SmallInteger, default = ROLE_USER)

    def __init__(self , username ,password , email):
        self.username = username
        self.password = password
        self.email = email

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.username)

    # def __init__(self , username ,password , email):
    #     self.username = username
    #     self.password = password
    #     self.email = email
    #     self.registered_on = datetime.utcnow()

# What do you call these Users.properties?
    # def register(self):
    #     import redis
    #     r = redis.StrictRedis(host='localhost', port=6379, db=0)
    #     r.set("id_"+form.username.data, unicode(24))
    #     r.set("username_"+form.username.data, form.username.data)
    #     r.set("email_"+form.username.data, form.email.data)
    #     r.set("password_"+form.username.data, form.password.data)



        # from passlib.apps import custom_app_context as pwd_context


    # def hash_password(self, password):
        # self.password_hash = pwd_context.encrypt(password)

    # def verify_password(self, password):
        # return pwd_context.verify(password, self.password_hash)
