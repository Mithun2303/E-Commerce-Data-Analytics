 # E-Commerce-Data-Analytics

You can clone the project using 
```
git clone https://github.com/Mithun2303/E-Commerce-Data-Analytics.git
```

## This project works on python 3.10
## If you want to install virtual environment 
```python
python3 -m venv venv
source venv/bin/activate
```
## To deactivate virtual environement 
```
deactivate
```

## To install the required libraries 
```
pip install -r requirements.txt
```

## Install postgres and setup your database 
### The table schemas are at 
```schemas/```
### To create a table using python you should import the schema in create_db.py and run it.

<img width="732" alt="Screenshot 2023-06-27 at 7 00 27 PM" src="https://github.com/Mithun2303/E-Commerce-Data-Analytics/assets/84895703/6f92c473-3f54-4b78-b7c5-3c981adeb0f9">

### Repeat this for every table you need to create

## In the database.py file change the username password and the dbname

<img width="710" alt="Screenshot 2023-06-27 at 7 02 21 PM" src="https://github.com/Mithun2303/E-Commerce-Data-Analytics/assets/84895703/d6ea806e-c9c5-45c8-a27e-de6ff2094b5d">

## Add the dataset file in your database using
```
psql -d [databasename] -U [username] -f [schema.sql]
```

## Start the server using uvicorn
```
uvicorn main:app --reload --log-config logging.conf
```
## Make sure you are in virtual environment.
## You can see the swagger UI at
>http://127.0.0.1:8000/docs

## There are 7 APIs in the repo 

```customer/{id}```
### This provides customer details when given a customer id (cust_1234)

```unique/customer```
### Unique customers in January who came back every month over the entire year in 2011

``` product/details/{product_category}```
### This provides the list of product under the given category

```/maxorder/{first}/{off_set}```
### This provides the customer who had the most purchases from the given offset

```/order/{id}```
### This provides the order details when an order id is given (Ord_123)

```/sales```
### This gives the sales made by each product

```/product ```
### This gives the profit made by each product
