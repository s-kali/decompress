import zipfile
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 1024


def un_zip(path, pwd):
    if pwd is not None and pwd != "":
        with zipfile.ZipFile(path, 'r') as zip_ref:
            zip_ref.extractall('/tmp/unzip/', None, bytes(pwd, encoding='utf8'))
    else:
        with zipfile.ZipFile(path, 'r') as zip_ref:
            zip_ref.extractall('/tmp/unzip/')


@app.route('/unzip', methods=['POST'])
def unzip():
    content = request.get_json()
    zip_path = content['location']
    zip_pwd = content['password']
    un_zip(zip_path, zip_pwd)
    resp = jsonify({'data': zip_path})
    resp.status_code = 200
    return resp


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
