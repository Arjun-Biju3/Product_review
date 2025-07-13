Product Review System API
=========================

This is a RESTful API built using Django and Django REST Framework that supports product management and user reviews with role-based access.

----------------------------------------------------
👤 Roles:
- Admin: Can add, update, and delete products.
- Registered User: Can post one review per product.
- Public: Can view products and reviews.
----------------------------------------------------

Admin Credentials
-----------------
Username: admin
Password: admin

📮 API Endpoints
================

🔐 Authentication
------------------
POST   /api/register/         - Register a new user
POST   /api/auth/             - Login to get token

Authorization Required:
------------------------
Add this header in Postman or any client:

Authorization: Token <your_token>

📦 Product Endpoints
---------------------
GET    /api/products/             - List all products (public)
GET    /api/products/<id>/        - Retrieve product by ID
POST   /api/products/             - Create product (admin only)
PUT    /api/products/<id>/        - Update product (admin only)
DELETE /api/products/<id>/        - Delete product (admin only)

📝 Review Endpoints
--------------------
GET    /api/products/<id>/reviews/     - List reviews for a product
POST   /api/products/<id>/reviews/     - Submit review (auth users only, 1 per product)

Review Body Example:
---------------------
{
  "rating": 4,
  "feedback": "Great product!"
}

💡 Token Authentication
------------------------
- First POST to /api/auth/ with username & password to get a token
- Use that token in all secured API calls:
  Authorization: Token your_token_here

🧪 Example Review Submission
-----------------------------
POST /api/products/1/reviews/
Headers:
  Authorization: Token your_token
  Content-Type: application/json

Body:
{
  "rating": 5,
  "feedback": "Excellent product!"
}

✅ Technologies Used
---------------------
- Django 5.x
- Django REST Framework
- Token Authentication

