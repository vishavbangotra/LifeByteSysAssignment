# LifeByteSysAssignment
Full Stack Developer assignment for LifeByte Systems

## Live application
https://vishavbangotra.pythonanywhere.com/

## DB Structure
id
___
name
___
age
___

Backend is developped using flask, SQLAlchemy

"/"  - Endpoint renders the landing html page
"/api/data" - Endpoint gets list of all dammy data in Json
"/api/data/<id>" - Endpoint gets the dummy object with id = <id>


Frontend using HTML, CSS, Bootstrap, JavaScript, AJAX

on click of the Load data button a GET request is sent /api/data and all dummy data is fetched.
the PlotGraph() funtion handles the Graph creation
the PlotTable() funtion plots the table


