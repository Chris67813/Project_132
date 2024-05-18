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
    
class Quest(db.Model):

class QuestImage(db.Model):

class Played(db.Model):

class Store(db.Model):                     

class Transaction(db.Model):

#Initialising the Database
@app.before_first_request
def create_tables():
    db.create_all()

# Function to perform login
def login():
    

# Function for registration
def register():
    

# Function for logout
def logout():
    

# Function to get user data by username
def get_user_by_username(username):
    

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
