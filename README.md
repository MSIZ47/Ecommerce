
## **Ecommerce**

Dockerized Ecommerce project with Django and Postgres with Zarinpal Payment Gataway that I did in last section of django course in Codingyar.com

## **Introduction**

a typical Ecommerce website with different products for sale.customers register and search through the website,choose those products they wanna buy,then complete their shopping with placing the order and then they pay!!!
although i simiulate the payment with Zarinpal and real payments yet not ready in this project.

##  **Description**

In this project i use *Django All_Auth* for authentication,placed a really powerfull shopping cart that tracks the session of the customer(using context processors) and including in templates.I used message framework in django
to send message to the user about different things such as login or adding something to the shoppingcart.I used Internationaliztion in this project to get familiare with it.on the other hand,I used *django-rosetta*
for i18n too.I used *Django_jalali_data* to use shamsi date in the website and the admin area.Also, i created a templatetag to convert english numbers to persian.I used *Rich_text_editor* in the admin area for description
of the products.I created a comlete order app for managing the order of the customer and save all the details of an order in the database.at last i simiulate a Zarinpal payment gataway for the payment proccess of the website that its
not yet complete(its fully programmed but requiers some debug with real zarinpal merchant_id).

## **Installation**

To install Project Title, follow these steps:

1. Clone the repository
2. Navigate to the project directory
3. create an .env file
4. go to djecrety.ir and generate a fake django secret key and place it in the .env file
5. then put the DJANGO_DEBUG(set it to True for debug) , DJANGO_ZARINPAL_MERCHANT_ID, DATABASE_PASSWORD, DATABASE_NAME, DATABASE_USER On the .env file of the project
6. in this step you must have a .env file in root of the project with data of  DJANGO_SECRET_KEY, DJANGO_DEBUG, DJANGO_ZARINPAL_MERCHANT_ID, DATABASE_NAME, DATABASE_USER and DATABASE_PASSWORD
7. Install dependencies: **pipenv install**
8. you should have gettexttools and gettextruntime installed and added to path in windows for using the internationaliztion(search *cant find mesguinq, make sure gettexttools installed windows* and follow stackoverflow steps)its pretty straight forward.
9. activate virtual env :  **pipenv shell**
10. use docker **docker compose up --build**
12. makemigration for every app in the project(its nessessory) forexample docker compose exec web python manage.py makemigrations products -->**docker compose python manage.py makemigrations**
13. the migration of the database -->**docker compose python manage.py migrate**
14. add a superuser to the project -->**docker compose python manage.py createsuperuser**
15. Start the project: **docker compose exec web python manage.py runserver**
16. go to http://127.0.0.1:8000/admin and with superuser create some dummydata and fake products and comments for better understanding the website if you want.
  

## **Usage**

follow these steps:

1. Open the project in your favorite code editor.
2. Modify the source code to fit your needs.
3. start the project: **docker compose up**
4. Use the project as desired.



## **Conclusion**

The Ecommerce website with advanced concepts of Django.I learned some advance topics and tools for django with **Ecommerce** Project and I did my best to practice Django completing this project.i will complete the payment process in the website soon.
