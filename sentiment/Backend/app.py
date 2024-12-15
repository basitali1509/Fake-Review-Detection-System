
# import numpy as np
# import pandas as pd
# from transformers import AutoTokenizer, AutoModelForSequenceClassification
# import torch
# import requests

# import re

# from flask import Flask , request
# from pymongo import MongoClient
# from werkzeug.utils import secure_filename
# import hashlib
# from flask import Flask, request, jsonify
# from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required
# import datetime
# import hashlib


# import os
# # import tensorflow as tf
# # from pymongo import ObjectId
# from bson.objectid import ObjectId



# import requests

# from io import BytesIO



# app = Flask(__name__)
# jwt = JWTManager(app) # initialize JWTManager
# app.config['JWT_SECRET_KEY'] = '38dd56f56d405e02ec0ba4be4607eaab'
# app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)
# app.config['UPLOAD_FOLDER'] = 'csv_data'
# #region  
# client = MongoClient('mongodb+srv://aza-e-hussain:cz9Am1Y4VJHrf8ZY@cluster0.oakgoec.mongodb.net/')
# #endregion


# db=client.sentimental_analysis


# user = db.user
# sentiment=db.sentimental
# result = db.result


# tokenizer = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

# model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

# def sentiment_score(review):
#     tokens = tokenizer.encode(review, return_tensors='pt')
#     result = model(tokens)
#     return int(torch.argmax(result.logits))+1

# ALLOWED_EXTENSIONS = {'csv'}

# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS







# @app.route('/', methods=('GET', 'POST'))
# def index():
#     if request.method == "GET":
#     #    doctor.insert_one({"name":""})
#        return 'saved'




# # region begin for user


# @app.route("/api/user/signup",methods=["POST"])
# def userregister():
#     if request.method == "POST":
#         new_user = request.get_json() # store the json body request
#         # Creating Hash of password to store in the database
#         new_user["password"] = hashlib.sha256(new_user["password"].encode("utf-8")).hexdigest() # encrpt password
#         # Checking if user already exists
#         doc = user.find_one({"username": new_user["username"]}) # check if user exist
#         # If not exists than create one
#         if not doc:
#             # Creating user
#             new_user["createdAt"]= datetime.datetime.today()
#             user.insert_one(new_user)
#             return jsonify({'msg': 'User created successfully'}), 201
#         else:
#             return jsonify({'msg': 'Username already exists'}), 409
        




# @app.route("/api/user/login", methods=["post"])
# def userlogin():
#     # Getting the login Details from payload
#     login_details = request.get_json() # store the json body request
#     # Checking if user exists in database or not
#     user_from_db = user.find_one({'username': login_details['username']})  # search for user in database
#     # If user exists
#     if user_from_db:
#         # Check if password is correct
#         encrpted_password = hashlib.sha256(login_details['password'].encode("utf-8")).hexdigest()
#         if encrpted_password == user_from_db['password']:
#             # Create JWT Access Token
#             access_token = create_access_token(identity=user_from_db['username']) # create jwt token
#             # Return Token
#             return jsonify(access_token=access_token), 200
#     return jsonify({'msg': 'The username or password is incorrect'}), 401    


# @app.route("/user/sentimental/upload",methods=["POST"])
# def sentimental():
#     if 'file' not in request.files:
#         return jsonify({'error': 'No file part'}), 400
#     file = request.files['file']
#     if file.filename == '':
#         return jsonify({'error': 'No selected file'}), 400
#     if file and allowed_file(file.filename):
#         filename = secure_filename(file.filename)
#         print(filename)
#         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#         df=pd.read_csv(os.path.join(app.config['UPLOAD_FOLDER'], filename))

#         df.columns = map(str.upper, df.columns)
        
#         # Ensure 'review' column exists
#         if 'REVIEW' not in df.columns:
#             return jsonify({'error': 'No review column in the dataframe'}), 400
#         else:
#             try:
#                 df['sentiment'] = df['REVIEW'].apply(lambda x: sentiment_score(x[:512]))
#             except TypeError or ValueError:
#                 return jsonify({'error': 'Error calculating sentiment score. Type Error or Value error'}), 400
#         json=df.to_json(orient='records', indent=4)
#         data = df.to_dict(orient='records')

#         if(json):
#             sentiment.insert_one({"result":data}) 
#         print(json)  
                               
#         return json


#         # return jsonify({'message': 'File successfully uploaded'}), 200
#     else:
#         return jsonify({'error': 'Allowed file types are csv'}), 400





# if __name__ == "__main__" :
#     # setup()
#     app.run(debug=True)














import string
import numpy as np
import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import requests
# from bs4 import BeautifulSoup
import re
import pickle
import sklearn
from flask import Flask , request
from pymongo import MongoClient
from werkzeug.utils import secure_filename
import hashlib
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required
import datetime
import hashlib

from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import os
# import tensorflow as tf
# from pymongo import ObjectId
from bson.objectid import ObjectId
from bson.json_util import dumps
import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords




import requests

from io import BytesIO

def open_image_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if request was successful
        image = Image.open(BytesIO(response.content))
        return image
    except Exception as e:
        print("Error:", e)
        return None

app = Flask(__name__)
CORS(app)
jwt = JWTManager(app) # initialize JWTManager
app.config['JWT_SECRET_KEY'] = '38dd56f56d405e02ec0ba4be4607eaab'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)
app.config['UPLOAD_FOLDER'] = 'csv_data'
#region  
client = MongoClient('mongodb+srv://aza-e-hussain:cz9Am1Y4VJHrf8ZY@cluster0.oakgoec.mongodb.net/')
#endregion


db=client.sentimental_analysis


user = db.user
result = db.result
feedback = db.feedback





# Function to scrape product reviews
def scrape_product_reviews(driver, url):
    print(driver)
    print(url)

    driver.get(url)
    time.sleep(5)  # Adjust based on page load time
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    # Find all review divs using their class name
    review_tags = soup.find_all(class_='review-content-sl')
    print(review_tags)
    
    # List to hold all reviews from this page
    reviews = []
    
    # Loop through each review tag and extract the text
    for review_tag in review_tags:
        review_text = review_tag.text.strip() if review_tag else 'Not Found'
        reviews.append(review_text)
    
    return reviews

# Set up WebDriver




tokenizer = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

def sentiment_score(review):
    tokens = tokenizer.encode(review, return_tensors='pt')
    result = model(tokens)
    return int(torch.argmax(result.logits))+1
def text_process(review):
    nopunc = [char for char in review if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]
with open('model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

ALLOWED_EXTENSIONS = {'csv'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS







@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == "GET":
    #    doctor.insert_one({"name":"zaryab"})
       return 'saved'




# region begin for user


@app.route("/api/user/signup",methods=['POST'])
def userregister():
    
        new_user = request.get_json() # store the json body request
        # Creating Hash of password to store in the database
        new_user["password"] = hashlib.sha256(new_user["password"].encode("utf-8")).hexdigest() # encrpt password
        # Checking if user already exists
        doc = user.find_one({"username": new_user["username"]}) # check if user exist
        # If not exists than create one
        if not doc:
            # Creating user
            new_user["createdAt"]= datetime.datetime.today()
            user.insert_one(new_user)
            return jsonify({'msg': 'User created successfully'}), 201
        else:
            return jsonify({'msg': 'Username already exists'}), 409
        




@app.route("/api/user/login", methods=["post"])
def userlogin():
    # Getting the login Details from payload
    login_details = request.get_json() # store the json body request
    # Checking if user exists in database or not
    user_from_db = user.find_one({'username': login_details['username']})  # search for user in database
    # If user exists
    if user_from_db:
        # Check if password is correct
        encrpted_password = hashlib.sha256(login_details['password'].encode("utf-8")).hexdigest()
        if encrpted_password == user_from_db['password']:
            # Create JWT Access Token
            access_token = create_access_token(identity=user_from_db['username']) # create jwt token
            # Return Token
            return jsonify(access_token=access_token), 200
    return jsonify({'msg': 'The username or password is incorrect'}), 401    


@app.route("/user/sentimental/upload",methods=["POST"])
@jwt_required()
def sentimental():
    current_user = get_jwt_identity() # Get the identity of the current user
    user_from_db = user.find_one({'username' : current_user})
    if(user_from_db):
        form = request.form
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print(filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            df=pd.read_csv(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            df.columns = map(str.upper, df.columns)
            
            # Ensure 'review' column exists
            if 'REVIEW' not in df.columns:
                return jsonify({'error': 'No review column in the dataframe'}), 400
            else:
                try:
                    df['sentiment'] = df['REVIEW'].apply(lambda x: sentiment_score(x[:512]))
                    predictions = loaded_model.predict(df['REVIEW'])
                    df['Predictions']=predictions
                    df['Predictions']= df['Predictions'].apply(lambda x: 'Fake' if x == 'CG' else 'Genuine')

                except TypeError or ValueError:
                    return jsonify({'error': 'Error calculating sentiment score. Type Error or Value error'}), 400
            json=df.to_json(orient='records', indent=4)
            data = df.to_dict(orient='records')
            print(user_from_db)
            created_result=result.insert_one({"result":data,"datasetname":form["name"],"userId":str(user_from_db["_id"])})
            # created_result["_id"]=str(created_result["_id"])
            # print(created_result)
            # inserted_document = result.find_one({"_id": created_result["inserted_id"]})
            print(created_result.inserted_id)
            inserted_document = result.find_one({"_id":ObjectId(created_result.inserted_id)})
            inserted_document["_id"] = str(inserted_document["_id"])
            return jsonify(inserted_document)


            # return jsonify({'message': 'File successfully uploaded'}), 200
        else:
            return jsonify({'error': 'Allowed file types are csv'}), 400

@app.route("/user/sentimental/results",methods=["GET"])
@jwt_required()
def all_sentimental():
    current_user = get_jwt_identity() # Get the identity of the current user
    user_from_db = user.find_one({'username' : current_user})
    if(user_from_db):
        get_data=result.find({"userId":str(user_from_db["_id"])})
        print(get_data)
        get_data=list(get_data)
        if(get_data):
            for i in range(len(get_data)):
                get_data[i]["_id"]=str(get_data[i]["_id"])
            return {"result":get_data}
        else:
            return jsonify({"message":"no data found"})


@app.route("/user/sentimental/results/<string:id>",methods=["GET"])
@jwt_required()
def one_sentimental(id):
    current_user = get_jwt_identity() # Get the identity of the current user
    user_from_db = user.find_one({'username' : current_user})
    if(user_from_db):
        get_data=result.find_one({"userId":str(user_from_db["_id"]),"_id":ObjectId(id)})
        print(get_data)
        if(get_data):
            get_data["_id"]=str(get_data["_id"])
           
            return {"result":get_data}
        else:
            return jsonify({"message":"no data found"})



@app.route("/ByLink",methods=["POST"])
def By_link():
    driver = webdriver.Chrome()

# URLs to scrape
    urls = ["https://www.daraz.pk/products/m19-and-m29-f9-tws-airpods_-with-super-sound-high-quality-touch-sensors-true-stereo-headphones-with-built-in-mic-10m-transmission-bluetooth-wireless-earbuds-charging-case-sport-headset-for-all-bluetooth-smart-devices-i420665130-s2238147232.html?&search=0?spm=a2a0e.pdp.recommend_2.5.28401d4eQJtTlK&mp=1&scm=1007.38553.252219.0&clickTrackInfo=0c27c19a-6440-4aa5-913b-15a3e7f02be9__420665130__155__i2i__372903__0.015979873__0.015979873__0.0__0.0__0.0__0.0353324__4__null__null__null__null__null__null____3000.0__0.6836666666666666__4.07568__185__949.0____null__null__null__3650.16544_955.3632_4559.21183__null__28556__null__0.0__0.0________null__null", ]

# Dictionary to hold all product reviews keyed by URL
    all_product_reviews = {}

# Scrape each URL
    for url in urls:
        all_product_reviews[url] = scrape_product_reviews(driver, url)

    # Close the WebDriver
    driver.quit()

# Define CSV output parameters
    csv_file_name = 'product_reviews.csv'

# Write to CSV
    with open(csv_file_name, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['URL', 'Review'])  # Header row
        for url, reviews in all_product_reviews.items():
            for review in reviews:
                writer.writerow([url, review])  # Write each review in its own row, associated with the URL

    print(f"Data has been exported to {csv_file_name}.")


    return "hello"



@app.route("/submit_contact_form",methods=["POST"])
def submit_contact_form():
    if request.method == 'POST':
        form_data = request.json
        
        # Data validation
        if not all(key in form_data for key in ['name', 'email', 'message']):
            return jsonify({'error': 'Missing required fields'}), 400
        
        name = form_data.get('name')
        email = form_data.get('email')
        message = form_data.get('message')
        
        # Check for duplicate message
        if feedback.find_one({'message': message}):
            return jsonify({'error': 'Duplicate message'}), 400
        
        # Processing the form data
        print("Received form data:")
        print("Name:", name)
        print("Email:", email)
        print("Message:", message)
        
        # Insert into MongoDB
        feedback.insert_one(form_data)
        
        return jsonify({'message': 'Form submitted successfully'}), 200



if __name__ == "__main__" :
    # setup()
    app.run(debug=True)