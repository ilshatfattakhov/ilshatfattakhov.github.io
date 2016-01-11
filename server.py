from flask import Flask, request
# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')

@app.route('/spb')
def spb():
    return app.send_static_file('map_spb.html')
@app.route('/mgn')
def mgn():
    return app.send_static_file('map_mgn.html')
if __name__ == "__main__":
    app.run()
