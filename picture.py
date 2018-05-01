from flask import Flask
from PIL import Image
import requests
app = Flask(__name__)
@app.route('/image/<string:event>', methods=['GET'])
def pic(event):

    Movie_URL= 'http://mandm.plearnjai.com/API/detailMovie.php?idmovie='+event
    r = requests.get(url=Movie_URL)
    data = r.json()
    url = data['response'][0]['detailMovie'][0]['Poster']
    image = Image.open(requests.get(url, stream=True).raw)
    return image

if __name__ == '__main__':
    app.run()