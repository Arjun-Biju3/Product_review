Product Review System API
=========================

This is a RESTful API built using Django and Django REST Framework that supports product management and user reviews with role-based access.

----------------------------------------------------
Roles:
- Admin: Can add, update, and delete products.
- Registered User: Can post one review per product.
- Public: Can view products and reviews.
----------------------------------------------------

Admin Credentials:
------------------
Username: admin
Password: admin

----------------------------------------------------
API Endpoints
----------------------------------------------------

Authentication:
---------------
POST    /api/register/               -> Register a new user  
POST    /api/auth/                  -> Login and get authentication token

Use this header in protected requests:
Authorization: Token <your_token>

----------------------------------------------------

Product Endpoints:
------------------
GET     /api/products/              -> List all products (public)  
GET     /api/products/<id>/         -> Retrieve product by ID (public)  
POST    /api/products/              -> Create new product (admin only)  
PUT     /api/products/<id>/         -> Update product (admin only)  
DELETE  /api/products/<id>/         -> Delete product (admin only)

----------------------------------------------------

Review Endpoints:
-----------------
GET     /api/products/<id>/reviews/     -> List reviews for a product (public)  
POST    /api/products/<id>/reviews/     -> Submit review (auth users only, 1 per product)

----------------------------------------------------

Review Submission Example:
--------------------------
Endpoint:
POST /api/products/1/reviews/

Headers:
Authorization: Token your_token_here  
Content-Type: application/json

Body:
{
  "rating": 5,
  "feedback": "Excellent product!"
}

----------------------------------------------------

Token Authentication Flow:
--------------------------
1. Login using POST /api/auth/ with username and password  
2. Copy the token received  
3. Send this token in headers for authenticated requests:
   Authorization: Token your_token

----------------------------------------------------

Technologies Used:
------------------
- Django 5.x  
- Django REST Framework  
- Token Authentication

