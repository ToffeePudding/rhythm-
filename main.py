from flask import Flask, render_template, request, send_from_directory, redirect, url_for
import os

app = Flask(__name__)

# specify the upload folder for songs
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    # get the list of songs in the uploads folder
    songs = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', songs=songs)

@app.route('/play', methods=['POST'])
def play():
    song = request.form['song']
    return render_template('play.html', song=song)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

app.run(host='0.0.0.0', port=81)
