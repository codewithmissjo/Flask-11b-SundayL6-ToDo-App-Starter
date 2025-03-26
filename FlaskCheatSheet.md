# Flask Cheat Sheet
## Import
`from flask import Flask`
Other modules include: `render_template`, `request`, `redirect`, `session`
## Create an App
`app = Flask(__name__)`
## Run an App
`app.run()`
## Defining Routes
```
@app.route('/route')
def route_function():
  return 'HTML content'
```
## Route Variables
```
@app.route('/route<routeVariable>')
def route_function(routeVariable):
  return 'HTML content'
```
## Methods and Requests
```
@app.route('/route', methods=['GET', 'POST'])
def route_function():
  if request.method == 'GET':
    return 'HTML content'
  else:
    return 'HTML content'
```
## Get a Form Field Value
`request.form.get('name_attribute')`
## Templates

## Template Variables



