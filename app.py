from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    
#    app.run(debug=True)

# By default, Flask binds to 127.0.0.1, which makes the server 
#    only accessible from the local machine. To make it accessible 
#    from other machines, you need to bind it to 0.0.0.0  
    app.run(debug=True, host='0.0.0.0')
