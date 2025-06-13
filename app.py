import os 
import time
from flask import Flask ,render_template,redirect,request
from werkzeug.utils import secure_filename
from PyPDF2 import PdfReader
import json

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 5*1024*1024
ALLOWED_EXTENSIONS = {'pdf'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST']) 
def uploads():
    username = request.form.get('username')
    file = request.files.get('pdf_file')

    if not file or file.filename == '':
        return "Not file selected"
    if not allowed_file(file.filename):
        return "File must be a PDF"
    
    filename = secure_filename(file.filename) # type: ignore
    timestamp = str(int(time.time()))
    new_filename = f"{timestamp}_{username}_{filename}"
    file_path = os.path.join(app.config['UPLOAD_FOLDER'],new_filename)

    file.save(file_path)

    try:
        reader = PdfReader(file_path)
        num_pages = len(reader.pages)
        metadata = reader.metadata
    except Exception as e:
        return f"Error reading PDF: {str(e)}"
    
    log_data = {
        'username':username,
         'filename':new_filename,
         'pages':num_pages,
         timestamp:time.ctime()
    }
    with open('upload_log.json','a') as log_file:
        log_file.write(json.dumps(log_data)+ '\n')
    return render_template('result.html',username=username,filename=new_filename
                           ,num_pages=num_pages,metadata=metadata)

if __name__ == '__main__':
    app.run(debug=True)
    