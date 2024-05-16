#Flask, fill up the functions below

from flask import Flask, request, jsonify, session, redirect, url_for
from flask_bcrypt import Bcrypt
from flask_cors import cross_origin
from flask_sqlalchemy import SQLAlchemy
import os

#Initialise Flask Application and configure the Bcrypt extension
app = Flask(__name__)
bcrypt = Bcrypt(app)

#Configuring SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


def handle_options(response):

def allowed_file(filename):

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
    

def add_played():
    
def get_played_by_id(played_id):
    

# API to get a list of all users and the quests they have played
def get_users_with_quest():

def uploaded_file(filename):
