Simple CRUD web application (no security efforts were put, use for local pupuses only):


To run application one need to: 
 - ensure current device can support powershell 
 - install and setup local mongoDB server (with no username or password to authenticate): 
https://www.mongodb.com/docs/manual/installation/#mongodb-installation-tutorials
 - download backend folder (from this repository)
 - install python3: https://www.python.org/downloads/
 - run backend/example_venv/Scripts/Activate.ps1 with powershell
 - type in powershell console "flask run"
 - open website on http:/localhost:5000/






Specs:
 - backend - Flask (Python)
 - interface backend-frontend - REST Api (Json); AJAX requests 
 - frontend - Vue.js
 - database - MongoDB


