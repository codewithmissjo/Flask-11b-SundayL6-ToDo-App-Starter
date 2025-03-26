# ToDo App Project Planning

## The Phases
1. Setup the project (using the starter kit)
2. Plan and implement the database
3. Plan and implement CRUD operations:
    *  **(Read)** Reading ToDo Tasks
    *  **(Create)** Adding ToDo Tasks
    *  **(Delete)** Deleting ToDo Tasks
    *  **(Update)** Editing ToDo Tasks
4. Customization and/or Challenges

## The Starter Kit
*  How many templates are there?
*  Do any of the templates "fit" inside of other templates? Which ones?
*  Which templates include a form?
    *  In any forms, do all of the text inputs have a name attribute?
*  Which templates include an HTML table?
  *  How many columns are in the table?
*  List the Jinja2 template tags/placeholders in each template.
    *  For example: layout.html -- {{user}}

## The Database
### Planning
*  What will you name the database file?
*  What will you name the database table?
*  How many columns will you need in the database table?
    *  What are their names and what data types are they?
### Database Knowledge
*  What other code do you need to include in app.py in order to work with a database? Such as imports, connections, etc.
*  When do you need to "commit" changes to a database?
*  What character do you use within a SQLite query to represent a placeholder?
*  How many tables can you create within a single database?

## CRUD
Each CRUD operation needs a route, one or more methods, actions, and something to return. Plan out your routes below, using the example as your template.

NOTE: You can save the Update operation for next class, because it's the most complex.

### Read
*  **Route URL:** '/'
*  **Route variables:** none
*  **Methods:** get
*  **Template:** home.html
*  **Actions:** get all the records from the database table
*  **SQL query needed:** 'SELECT * FROM table_name'
*  **Return:** render the template, include {{list}} to populate the HTML table

### CREATE
*  **Route URL:** 
*  **Route variables:** 
*  **Methods:** 
*  **Template:** 
*  **Actions:** 
*  **SQL query needed:** 
*  **Return:**

### DELETE
*  **Route URL:** 
*  **Route variables:** 
*  **Methods:** 
*  **Template:** 
*  **Actions:** 
*  **SQL query needed:** 
*  **Return:**

### UPDATE
*  **Route URL:** 
*  **Route variables:** 
*  **Methods:** 
*  **Template:** 
*  **Actions:** 
*  **SQL query needed:** 
*  **Return:** 
