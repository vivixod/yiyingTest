from app.extension import db
from werkzeug.security import generate_password_hash, check_password_hash


class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_number = db.Column(db.Integer, nullable=False)
    book_name = db.Column(db.String(255), nullable=False)
    book_type = db.Column(db.String(255), nullable=False)
    book_price = db.Column(db.Float, nullable=False)
    author = db.Column(db.String(255))
    book_publisher = db.Column(db.String(255))

    @staticmethod
    def init_db():
        rets = [
            (1, '001', '活着', '小说', 39.9, '余华', '某某出版社'),
            (2, '002', '三体', '科幻', 99.8, '刘慈欣', '重庆出版社')
        ]
        for ret in rets:
            book = Book()
            book.id = ret[0]
            book.book_number = ret[1]
            book.book_name = ret[2]
            book.book_type = ret[3]
            book.book_price = ret[4]
            book.author = ret[5]
            book.book_publisher = ret[6]
            db.session.add(book)
        db.session.commit()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(255), nullable=False, unique=True)
    user_password = db.Column(db.String(255), nullable=False)

    @staticmethod
    def init_db():
        rets = [
            (1, '朱陶涛', 'gyztt030607'),
            (2, '缪尔赛思', 'lysm')
        ]
        for ret in rets:
            user = User()
            user.id = ret[0]
            user.user_name = ret[1]
            user.password = ret[2]
            db.session.add(user)
        db.session.commit()

    # 保护字段，不让别人看我，比如xxx.password,直接报错
    @property
    def password(self):
        raise ArithmeticError("password是不可读字段")

    # 设置密码，加密，比如,xxx.password=xxxx
    @password.setter
    def password(self, password):
        self.user_password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.user_password, password)
