# Simple-emailbox

### About the project  
The project is a purely backend Django apllication which uses the Django Rest Framework to host simple API.  
The backend enables to send mails with customly configuered emailbox.

### Dependencies

  - Python 3.8.5
  - Django 2.2.16
  - Django Rest Framework 3.12.1
  - Celery 5.0.2
  - Django-filter 2.4.0
  - Django-environ 0.4.5
  - (PostgreSQL) psycopg2-binary 2.8.6
  - RabbitMq
  
Clik [RabbitMq](https://www.rabbitmq.com/) to learn more about installation.
  
### How to start?
Make sure you have a new working directory and RabbitMQ installed and active, than run the following commands to get started:
  ```
  python3 -m venv venv
  git clone https://github.com/wayzor9/Simple-emailbox.git
  pip3 install -r requirements/base.txt
  python3 manage.py runserver
  ```
  
  ### Browse
  
  ```Base URL: http://127.0.0.1:8000/api/v1/```  
  
|  Method |Endpoint   |Usage   | 
|---|---|---|
|GET, POST |mailbox/   |Get a list of mailboxes or create emailbox | 
|GET, PUT, PATCH, DELETE   |mailbox/{mailbox_id}/   |Get, update, delete mailbox   | 
|GET, POST   |template/   |Get a list of templates or create template   | 
|GET, PUT, PATCH, DELETE   |template/{template_id}   |Get, update, delete template  |
|GET   |mail/   |Get list of mails   |   
|POST   |mail/   |Create mail   | 
