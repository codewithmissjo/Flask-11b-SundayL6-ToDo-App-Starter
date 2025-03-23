from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# routes
@app.route('/')
def index():
  return render_template('home.html')

if __name__ == '__main__':
  #main()
  app.run(debug=True)
