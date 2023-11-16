
import os
from flask import Flask, flash, request, redirect, url_for, send_from_directory, render_template, current_app
from werkzeug.utils import secure_filename
from werkzeug.middleware.proxy_fix import ProxyFix

# set upload target folder path
UPLOAD_FOLDER = '/home/scheehan/my-projects/Flask/file_app/apps/static/uploads/'
# set allowed file format type
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'log', 'tgz', 'zip', 'out', 'py', 'sh', 'mp4', 'mp3', 'iso', 'pcap', 'pcapng', 'ttl', 'xml', 'json', 'tar', 'html', 'xlsx', 'conf', 'har'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['TEMPLATES_AUTO_RELOAD'] = True

app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

# check input file format with allowed extensions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    
# landing URL; accept file input and checking
@app.route('/uploads', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'GET':
        get_file_filename = os.listdir(app.config['UPLOAD_FOLDER'])
        return render_template('index.html', title='Temp Upload File Storage', get_file_filename=get_file_filename)    
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            upload_files = request.files.getlist('file')
            for upload_file in upload_files:
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], upload_file.filename))
            # return redirect('/uploads', code=302)
            # get_filename = os.listdir(app.config['UPLOAD_FOLDER'])
            get_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            my_filename = filename
            html = render_template('uploads.html', get_filename=get_filename, upload_files=upload_files)
            resp = app.make_response(html)
            return resp
        else:
            return redirect('/unsupported_file', code=302)      
        
    
# generate download link for respective file for upload and download event
@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download_file(filename):
    uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
    return send_from_directory(directory=uploads, path=filename)

      
# Notify user about unsupported file; then redirect back to landing page
@app.route('/unsupported_file')
def unsupported():
    return render_template('filelist.html')

# handle 404 respond
@app.errorhandler(404)
def page_not_found(error):
    # return render_template('500.html'), 404
    html = render_template('500.html')
    resp = app.make_response(html)
    return resp


# handle 500 respond
@app.errorhandler(500)
def internal_server_error(error):
    return render_template('404.html'), 500


if __name__ == "__main__":
    app.run(host='0.0.0.0')



    # port = int(os.environ.get('PORT', 5000))
    # app.run(debug=False, host='0.0.0.0', port=port)
