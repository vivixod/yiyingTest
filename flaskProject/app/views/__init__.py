from .book import book_view
from .register import register_view
from .login import login_view
from flask import Blueprint

bp = Blueprint('api', __name__)

bp.add_url_rule('/books', defaults={'book_id': None}, view_func=book_view, methods=['GET'])
bp.add_url_rule('/books', view_func=book_view, methods=['POST'])
bp.add_url_rule('/register', view_func=register_view, methods=['POST'])
bp.add_url_rule('/login', view_func=login_view, methods=['POST'])
bp.add_url_rule('/books/<int:book_id>', view_func=book_view, methods=['GET', 'PUT', 'DELETE'])