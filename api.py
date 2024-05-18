#Flask, fill up the functions below

from flask import Flask, request, jsonify, session, redirect, url_for
from flask_bcrypt import Bcrypt
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os

#Initialise Flask Application and configure the Bcrypt extension
app = Flask(__name__)
app.secret_key = "SessionSecretKey"  #Session's Secret Key

#Configuring SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
cors = CORS(app)

UPLOAD_FOLDER = 'uploads'
app.cofig['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

#Database Model - please fill these classes in, might be changed is it's different
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))
    balance = db.Column(db.Integer, default=0)                
    point = db.Column(db.Integer, default=0)
    
class Quest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    level = db.Column(db.Integer)
    timeout = db.Column(db.Integer)
    created_by = db.Column(db.String(100))
    answer = db.Column(db.String(200))
    
class QuestImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quest_id = db.Column(db.Integer, db.ForeignKey('quest.id'))
    filename = db.Column(db.String(100))

class Played(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quest_id = db.Column(db.Integer, db.ForeignKey('quest.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    answered = db.Column(db.String(200), nullable=True)

class Store(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    price = db.Column(db.Integer)                               
    name = db.Column(db.String(100))                            
    description = db.Column(db.String(200))                     
    category = db.Column(db.String(100))                     

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    status = db.Column(db.String(100))

#Initialising the Database
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    return "<h1>Flask API</h1>"

# Function to perform login
@app.route('/api/login', methods=['POST'])
@cross_origin(supports_credentials=True)
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            response = jsonify({'message': 'Login successful', 'username': username})
            response.headers['Cache-Control'] = 'no-cache'
            response.set_cookie('username', username)  # saving username into cookie
            return response, 200
        else:
            response = jsonify({'error': 'Invalid username or password'})
            response.headers['Cache-Control'] = 'no-cache'
            return response, 401
    

# function to perform registration
@app.route('/api/register', methods=['POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Hash password
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        new_user = User(name=name, username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        response = jsonify({'message': 'Registration successful'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers['Cache-Control'] = 'no-cache'
        return response, 201
    

# function to logout
@app.route('/api/logout', methods=['GET'])
@cross_origin(supports_credentials=True)
def logout():
    session.pop('username', None)  # delete username from session
    response = jsonify({'message': 'Logout successful'})
    response.headers['Cache-Control'] = 'no-cache'
    response.delete_cookie('username')  # delete username's cookie
    return response, 200
    

# function to get user's data by username
@app.route('/api/user/<username>', methods=['GET'])
def get_user_by_username(username):
    user = User.query.filter_by(username=username).first()
    if user:
        user_data = {
            'id': user.id,
            'name': user.name,
            'username': user.username,
            'email': user.email,
            'balance': user.balance,                          
            'point': user.point
        }
        return jsonify({'user': user_data}), 200
    else:
        return jsonify({'error': 'User not found'}), 404
    

# Endpoint to add quests
def add_quest():

    
# Function to update user points by username
def update_user_point(username):

    
# Endpoint to get all quests along with images
def get_quests():
    

# Endpoint to add played data
def add_played():

    
# Endpoint to get data played based on ID    
def get_played_by_id(played_id):
    

# API to get a list of all users and the quests they have played
def get_users_with_quest():

    
# Endpoint to add stores
def add_store():


# Endpoint to add transaction
def add_transaction():


# Endpoint to register store
def get_store():


# Endpoint to get transaction list
def get_transactions():


# Endpoint to load image based on file's name    
def uploaded_file(filename):
