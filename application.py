from flask import Flask

application = Flask(__name__)

@application.route('/')
def Welcome():
    return render_template('index.html')

'''if __name__ == "__main__":
    application.run()'''

port = os.getenv('PORT', '8000')
if __name__== "__main__":
    app.run(host="ec2-54-200-173-41.us-west-2.compute.amazonaws.com", port=int(port))