"""
    Endpoints for the links service:
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
            - Returns newly created link identifier if not exists, otherwise code 400 with link identifier
        - DELETE /api/v1/users/{username}/links/{link_id}/delete: Delete specific link
            - username : Authenticated user identifier
            - link_id : Shortened link identifier
            - Returns code 200 if deleted successfully, otherwise code 400
"""
from api.services.links import links_bp


@links_bp.route('/<link_id>', methods=['GET'])
def get_longer_link(link_id):
    pass


@links_bp.route('/users/<username>/links', methods=['GET'])
def get_user_links(username):
    pass


@links_bp.route('/users/<username>/links/<link_id>', methods=['GET'])
def get_user_link(username, link_id):
    pass


@links_bp.route('/users/<username>/links/new', methods=['POST'])
def create_link(username):
    pass


@links_bp.route('/users/<username>/links/<link_id>/delete', methods=['DELETE'])
def delete_link(username, link_id):
    pass
