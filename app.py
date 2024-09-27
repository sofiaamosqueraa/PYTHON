from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def microservices_doc():
    return render_template('documentacao/microservicos.html')

if __name__ == '__main__':
    app.run(debug=True)