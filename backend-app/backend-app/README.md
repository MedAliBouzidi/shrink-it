# Shrink-It Backend Server
This is the backend server for the Shrink-It application.
It is a RESTful API server that provides endpoints for user authentication, link shortening, and user profile management.
The server is built using Python and the Flask web framework.
It uses a MongoDB database to store user and link data.
The server is deployed using Docker.
The server is secured using JWT tokens for user authentication.

## APIs and Methods:
### Links endpoints:
- GET /api/v1/{link_id} : Get longer link
  - link_id : Shortened link ID
  - Returns Link Longer version if exists, otherwise code 404
- GET /api/v1/users/{username}/links : Get user’s links
  - username : Authenticated user identifier
  - Returns list of authenticated user’s links
- GET /api/v1/users/{username}/links/{link_id} : Get user’s specific link data
  - username : Authenticated user identifier
  - link_id : Shortened link identifier
  - Returns authenticated user’s specific link if exists, otherwise code 404
- POST /api/v1/users/{username}/links/new : Create new link
  - username : Authenticated user identifier
  - Returns newly created link identifier if not exists, otherwise code 400 with
  link identifier
- DELETE /api/v1/users/{username}/links/{link_id}/delete: Delete specific link
  - username : Authenticated user identifier
  - link_id : Shortened link identifier
  - Returns code 200 if deleted successfully, otherwise code 400
### User endpoints:
- GET /api/v1/users/{username} : Get user profile data
  - username : Authenticated user identifier
  - Returns authenticated user data
- PUT /api/v1/users/{username}/update : Update user profile data
  - username : Authenticated user identifier
  - Returns code 200 if updated successfully, otherwise code 400
### Authentication endpoints:
- POST /api/v1/auth/login : Login the user
  - email : user email
  - password : user password
  - Authenticate user and returns JWT Token, otherwise code 401
- POST /api/v1/auth/sign-up : Sign Up new user
  - full_name : User full name
  - username : unique user identifier
  - email : user email
  - password : user password
  - confirm_password : user password confirmation
  - Signup user and return code 203, otherwise code 419 if user exists or
  code 400 for invalid inputs
- POST /api/v1/auth/forgot-password : Send reset password token
  - email : user email
  - Send reset password token and returns code 200, otherwise code 404 if
  user doesn’t exists
- PUT /api/v1/auth/reset-password : Reset user password
  - new_password : new password
  - confirm_new_password : new password confirmation
  - Update user password, otherwise returns code 400 for invalid inputs