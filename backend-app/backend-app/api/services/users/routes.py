"""
    Endpoint for the users service:
        - GET /api/v1/users/{username} : Get user profile data
            - username : Authenticated user identifier
            - Returns authenticated user data
        - PUT /api/v1/users/{username}/update : Update user profile data
            - username : Authenticated user identifier
            - Returns code 200 if updated successfully, otherwise code 400
"""
from api.services.users import users_bp


@users_bp.route('/<username>', methods=['GET'])
def get_user(username):
    pass


@users_bp.route('/<username>/update', methods=['PUT'])
def update_user(username):
    pass
