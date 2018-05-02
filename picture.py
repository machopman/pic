from flask import Flask
import tkinter
from PIL import Image, ImageTk
from io import BytesIO
import requests
from pandas._libs import window

app = Flask(__name__)

@app.route('/image/<string:event>', methods=['GET'])
def pic(event):

    Movie_URL= 'http://mandm.plearnjai.com/API/detailMovie.php?idmovie='+event
    r = requests.get(url=Movie_URL)
    data = r.json()
    r = data['response'][0]['detailMovie'][0]['Poster']
    return r


if __name__ == '__main__':
    app.run()