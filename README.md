# DogeGames
## Overview:
GitHub repository link (https://github.com/Chris67813/Project_132.git)

DogeGames is an NFT purchasing website using emulated digital currency that a user can phone through playing a range of online games available on the website. 
Each user we need to register to create their own DogeGames account on their first time visiting the site. After the user logs in with their respective username and password, 
(currently) they can play one of four games to start earning coins. The Quiz, Coin Flip, Snake or Paper Scissors Rock. They can then visit the shop and browse through the 
library of NFTs that are available for purchase (a dynamic library that will periodically be updated with new NFTs). The customer can then “put in the request” to purchase the NFT. 
If the user has sufficient funds, the transaction can proceed. The user can then visit the library of their NFTs or check the current rank on the leaderboard. As the user purchases more 
NFTs, they will increase in the leaderboard rankings. 


## Students:

Student ID || Student Name    || GitHub Username

23775973   || Andrew Mekhail  || AndrewMekhail

23485147   || Rifqi Rahman    || rr1904

23324022   || Chit Thway      || Chris67813

23318983   || Kyaw Paing Hein || AndrewHein999



## How to launch Website:

After downloading and extracting the zip file, browse through the files and open the index.html file.

## Flask API Documentation Endpoints

### /api/store

POST /api/store: Add a new item to the store.

GET /api/store: Retrieve all items from the store.

GET /api/store/int:item_id: Retrieve a store item by its ID.

PUT /api/store/int:item_id: Update a store item by its ID.

DELETE /api/store/int:item_id: Delete a store item by its ID.




### /api/transaction

POST /api/transaction: Add a new transaction to the transaction table.

GET /api/transaction: Retrieve all transactions from the transaction table.

GET /api/transaction/int:trans_id: Retrieve a transaction by its ID.

PUT /api/transaction/int:trans_id: Update a transaction by its ID.

DELETE /api/transaction/int:trans_id: Delete a transaction by its ID.


## How to conduct testing:
1. open bash
2. cd to your directory with our zip file in it.
3. after getting to the root of our project file type in bash "python -m unittest discover -s tests"

## Reference:
[1] ChatGPT. "GameOver function." 2024. ChatGPT. Web. https://chatgpt.com/

[2] Flask-Bcrypt. (2011). Flask-Bcrypt Documentation (Version 1.0.1). Retrieved from https://flask-bcrypt.readthedocs.io/en/1.0.1/index.html

[3] Flask-CORS. (2013). Flask-CORS Documentation. Retrieved from https://flask-cors.readthedocs.io/en/latest/

[4] Werkzeug. (2007). Werkzeug Utilities Documentation (Version 3.0.x). Retrieved from https://werkzeug.palletsprojects.com/en/3.0.x/utils/

[5] W3Schools. (2024). HTML Game Setup Tutorial. Retrieved from https://www.w3schools.com/html/html5_canvas.asp
   


