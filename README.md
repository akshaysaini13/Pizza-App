# Pizza-App
Pizza App to store information about different types of Pizza

PizzaHub application stores diverse pizzas to choose from. It is a very simple generic interface application for the clients to interact with and choose these favourite 
pizza to have.

Porject has various APIs to perform different tasks.

"", Index API provides with the diverse Pizza menu to choose from for clients
viewpizza/<int:eid>, displays a broader view of each Pizza item
"cart", API provides with the checkout cart which are added by the client from the Pizza menu
_________________________________________________________________________________________________________________________________
Direction for use:

Server side:
For Admin:
Admin portal URL: http://localhost:8000/admin/login/?next=/admin/

username: pizza
password:pizza

Admin will be able to add items to the table "Product" that will dynamically be displayed in the Pizza menu page for clients.
Admin can decide the size, shape and price of each pizza item.

__________________________________________________________________________________________________________________________________

Client Side:
For Client use:

Homepage URL: http://localhost:8000/
Pizza menu URL: http://localhost:8000/pizzacart/
Cart URL: http://localhost:8000/pizzacart/cart/

Client can add or subtract pizza items in the Cart that will dynamically display the final amount of the order that the client has places.

About page: http://localhost:8000/about/
Contact page: http://localhost:8000/contact/

The product page has all items listed from Pizzas to beverages.

This app uses session and cookies to dynamically place client's request and processes it.
