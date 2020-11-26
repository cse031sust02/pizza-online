
# Overview 

This is a **very simple** project to get my hands on Django Framework. Please note that this is a **WIP**(work in progress) and I am not sure when it will complete!

# Pizza-Online :

Pizza Online is a On-Demand <s>Pizza</s> Food Delivery Platform. There are two components :

1. A Mobile App: Allows Customers to search for different restaurants and order foods.
2. A Web Dashboard: Allows Restaurant Owners to manager their restaurant details, menu etc.

Here is the flow :
- Customers login to the Mobile App using their phone number and password
- Customer orders food from nearby restaurants
- Restaurant Owners view the customer orders and deliver to customers
- Customer will get notification in Mobile APP when the order is accepted/delivered

## Customer App

The Customer App is the mobile app for the customers so that they can search for different restaurants and place orders from their Smart Phones.

- Registration – Customer can register from the App
- Login - Customer can login using their phone number and password
- Profile Management -  Customers can keep their profiles updated
- Search – Customers can explore new dishes and restaurants
- Order Management - Customer can place orders and view order history

## Web Dashboard

The Web Dashboard is the Admin Panel for Restaurants. A restaurant owner can add their restaurant details, menu etc. Note that, for the sake of simplicity there is only one restaurant for one owner.

- Registration - Restaurant Owners can register
- Login - Restaurant Owners can login using email and password
- Restaurant Details - Restaurant Owners can update details for his/her restaurant
- Menu Management -  Restaurant Owners can manage menu(dishes) for the restaurant
- Order Management - Restaurant Owners can view and update orders places by customers

# Technology

- Django
- DRF
- Celery
- PostgreSQL
- RabbitMQ
- Firebase
- Docker

# Development :

This Django Project contains (so far) two apps :
1) api : The API Backend for the mobile app (including registration, login for customers) 
2) web : codes for the Web Dashboard (including registration, login for restaurant owners)

# Architecture :
Under Construction!
