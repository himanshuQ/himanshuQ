- š Hi, Iām Himanshu
- š Iām a full stack developer
- š± Iām currently learning Machine learning and python frameworks
- š« How to reach me ...https://www.linkedin.com/in/himanshu-singh-200291/


**The ABProject is relevant to a very specific usecase. It has a basic implementation of API and caching**
- Setup steps
  - Install python 3.* on your machine
  - Install pip on your machine
  - Create virtual env
    - Run command "pip install virtualenv"
    - Run command to create a virtual environment "virtualenv mypython"
    - To activate in windows run command "mypthon\Scripts\activate"
  - Place the data file in you home directory
    -   IFSC File ā Google Drive Link
        https://docs.google.com/spreadsheets/d/1149Ps2PCafaKjHHkUYw5PmeiY5skg3tY/edit?usp=sharing&ouid=105581454063004875005&rtpof=true&sd=true
  - Run command on console "pip install requirements.txt" 
  - copy the code folder on your machine
  - To Run flask app:
    - Set default flask app; run command "export FLASK_APP=app"
    - Run command on console "flask run"
  - To run Django app:  
    - Run command "Python manage.py runserver"
  - Setup postman app
    - Import collection from this repo
  - Happy testing.
  
  Solution overview
The following depiction illustrates the solution workflow. The diagram shows the process and a summary of what is being performed and delivered:

Diagram illustrating the process and summary of a typical manual deployment using the various open source tools.


<img src="https://github.com/himanshuQ/himanshuQ/blob/main/aws_Flask-Microservice_f1.png">
  - Security cosiderations
    - enable basic auth module using a ldap provider like Oracle Unified Directory or token based authentication
    - enable https port for clients to access the API, secured via SHA2/TLS 1.2 
