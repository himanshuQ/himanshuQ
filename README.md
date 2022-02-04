- 👋 Hi, I’m Himanshu
- 👀 I’m a full stack developer
- 🌱 I’m currently learning Machine learning and python frameworks
- 📫 How to reach me ...https://www.linkedin.com/in/himanshu-singh-200291/
<h1>The ABProject is relevant to a very specific usecase. It has a basic implementation of API and caching</h1>
- Setup steps
  - Install python 3.* on your machine
  - Install pip on your machine
  - Create virtual env
    - Run command <pip install virtualenv>
    - Run command to create a virtual environment <virtualenv mypython>
    - To activate in windows run command <mypthon\Scripts\activate>
  - Place the data file in you home directory
    -   IFSC File – Google Drive Link
        https://docs.google.com/spreadsheets/d/1149Ps2PCafaKjHHkUYw5PmeiY5skg3tY/edit?usp=sharing&ouid=105581454063004875005&rtpof=true&sd=true
  - Run command on console <pip install requirements.txt> 
  - copy the code folder on your machine
  - To Run flask app:
    - Run command on console <flask run>
  - To run Django app:  
    - Python manage.py runserver
  - Setup postman app
    - Import collection from this repo
  - Happy testing.
  
  Solution overview
The following depiction illustrates the solution workflow. The diagram shows the process and a summary of what is being performed and delivered:

Diagram illustrating the process and summary of a typical manual deployment using the various open source tools.

<!---
himanshuQ ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
<img src="https://github.com/himanshuQ/himanshuQ/blob/main/aws_Flask-Microservice_f1.png">
  - Security cosiderations
    - enable basic auth module using a ldap provider like Oracle Unified Directory or token based authentication
    - enable https port for clients to access the API, secured via SHA2/TLS 1.2 
