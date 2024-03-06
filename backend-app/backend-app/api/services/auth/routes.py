"""
    Endpoints for the authentication service:
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
            - Signup user and return code 203, otherwise code 419 if user exists or code 400 for invalid inputs
        - POST /api/v1/logout : Log the user out
            - username : unique user identifier
            - Log the user out from the session
        - POST /api/v1/auth/forgot-password : Send reset password token
            - email : user email
            - Send reset password token and returns code 200, otherwise code 404 if user doesn’t exists
        - PUT /api/v1/auth/reset-password : Reset user password
            - new_password : new password
            - confirm_new_password : new password confirmation
            - Update user password, otherwise returns code 400 for invalid inputs
"""
from api.services.auth import auth_bp


@auth_bp.route('/login', methods=['POST'])
def login():
    pass


@auth_bp.route('/sign-up', methods=['POST'])
def register():
    pass


@auth_bp.route('/logout', methods=['POST'])
def logout():
    pass


@auth_bp.route('/forgot-password', methods=['POST'])
def forgot_password():
    pass


@auth_bp.route('/reset-password', methods=['PUT'])
def reset_password():
    pass
