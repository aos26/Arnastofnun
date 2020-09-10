from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from random import randrange
import os

app = Flask(__name__)
CORS(app)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ldfrovvhtipeme:e3582d741179079bf39de8245ecd5de33a70cfea4dce98dd85dc98195cb25cd7@ec2-34-194-198-176.compute-1.amazonaws.com:5432/d2u1f498k23d6j'#'sqlite:///database.db'
db = SQLAlchemy(app)

class WordModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flid = db.Column(db.Integer, nullable=False)
    ord = db.Column(db.String(255), nullable=False)
    ordflokkur = db.Column(db.String(10), nullable=False)
    texti = db.Column(db.String(500), nullable=False)


db.create_all()
db.session.commit()

word_put_args = reqparse.RequestParser()
word_put_args.add_argument("flid", type=int, help = "Auðkenni í íslenskri nútímamálsorðabók")
word_put_args.add_argument("ord", type=str, help = "Orðið")
word_put_args.add_argument("ordflokkur", type=str, help = "Orðflokkurinn")
word_put_args.add_argument("texti", type=str, help = "Skýring úr orðabókinni")



resource_fields = {
    'id': fields.Integer,
    'flid': fields.Integer,
    'ord': fields.String,
    'ordflokkur': fields.String,
    'texti': fields.String,
}

class  WordFetcher(Resource):
    @marshal_with(resource_fields)
    def get(self, word_id):
        count = WordModel.query.count()
        print(count)
        results = []
        for i in range(word_id):
            randomId = randrange(0, count)
            results.append(WordModel.query.filter_by(id = randomId).first())


        if not results:
            abort(404, message="Ekkert orð fannst með þessu Id")
        return results, 200

    @marshal_with(resource_fields)
    def put(self, word_id):
        args = word_put_args.parse_args()
        print(args)
        word = WordModel(id=word_id, flid=args['flid'], ord=args['ord'], ordflokkur=args['ordflokkur'], texti=args['texti'])
        db.session.add(word)
        db.session.commit()
        return word, 201

    def delete(self, word_id):
        num_rows_deleted = db.session.query(WordModel).delete()
        db.session.commit()
        return num_rows_deleted, 204

api.add_resource(WordFetcher, "/words/<int:word_id>")


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)