from flask import request
from flask.views import MethodView
from app.extension import db
from app.models import Book


class BookApi(MethodView):
    def get(self, book_id):
        if not book_id:
            books: [Book] = Book.query.all()
            results = [
                {
                    'id': book.id,
                    'book_name': book.book_name,
                    'book_type': book.book_type,
                    'book_price': book.book_price,
                    'book_number': book.book_number,
                    'book_publisher': book.book_publisher,
                    'author': book.author,
                } for book in books
            ]
            return {
                'status': 'success',
                'message': '数据查询成功',
                'results': results,
            }
        book: Book = Book.query.get(book_id)
        if book is None:
            return {
                'status': 'error',
                'message': '未找到指定书籍',
            }

        return {
            'status': 'success',
            'message': '数据查询成功',
            'result': {
                'id': book.id,
                'book_name': book.book_name,
                'book_type': book.book_type,
                'book_price': book.book_price,
                'book_number': book.book_number,
                'book_publisher': book.book_publisher,
                'author': book.author,
            }
        }

    def post(self):
        form = request.json
        book = Book()
        book.book_number = form.get('book_number')
        book.book_name = form.get('book_name')
        book.book_type = form.get('book_type')
        book.book_price = form.get('book_price')
        book.book_publisher = form.get('book_publisher')
        book.author = form.get('author')
        db.session.add(book)
        db.session.commit()
        # id, book_number, book_name, book_type, book.book_price, book.book_publisher, book.author

        return {
            'status': 'success',
            'message': '数据添加成功'
        }

    def delete(self, book_id):
        book = Book.query.get(book_id)
        db.session.delete(book)
        db.session.commit()
        return {
            'status': 'success',
            'message': '数据删除成功'
        }

    def put(self, book_id):
        book = Book.query.get(book_id)
        book.book_name = request.json.get('book_name'),
        book.book_type = request.json.get('book_type'),
        book.book_price = request.json.get('book_price'),
        book.book_number = request.json.get('book_number'),
        book.book_publisher = request.json.get('book_publisher'),
        book.author = request.json.get('book_author'),
        db.session.commit()
        return {
            'status': 'success',
            'message': '数据修改成功'
        }


book_view = BookApi.as_view('book_api')
