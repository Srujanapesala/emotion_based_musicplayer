# Setup
## 1. Install Python Verion Python 3.11.0
## 2. Create Virtual Environment (run below commands)
### python -m vene venv

## 3. Ativate Virtual Environment (run below commands)
### venv\Scripts\activate

## 4. Install Required Dependencies (run below commands)
### pip install -r requirements.txt

## 5. create ".env" file in the root of Project 

## 6. Generate API KEY for getting songs
### Go to this link:- https://rapidapi.com/Glavier/api/spotify23
### Login and you will get the API key in column "X-RapidAPI-Key" as shown in image
![alt text](<spotify api key.PNG>)

## 7. Add API Key to .env file (Add Below line Replace <API_Key> with the api key copied from last step)
### SPOTIFY_API_KEY=<API_Key>

## 8. run Application using Below Command
### streamlit run .\app.py

# Use
## 1. We have Optional field to add Singer
## 2. Click on get emotion button.
## 3. A camera window will open with box surrounding your face and detected emotion on top of box
## 4. Click "Q" to capture the emotion
## 5. It will Display all the songs based on your emotion
## 6. click on the songs from  the list, it will redirect it to a youtube to play the song