from flask_restx import Namespace, Resource, fields
from flask import request, jsonify
from .. import db
from ..models import Review, User, Place

api = Namespace('reviews', description='Review operations')

# Modelo para las reseñas
review_model = api.model('Review', {
    'id': fields.String(readonly=True, description='The review identifier'),
    'text': fields.String(required=True, description='Review text'),
    'user_id': fields.String(required=True, description='User identifier'),
    'place_id': fields.String(required=True, description='Place identifier'),
})

@api.route('/')
class ReviewList(Resource):
    @api.doc('create_review')
    @api.expect(review_model)
    def post(self):
        """Create a new review"""
        data = request.json
        new_review = Review(
            text=data['text'],
            user_id=data['user_id'],
            place_id=data['place_id']
        )
        db.session.add(new_review)
        db.session.commit()
        return jsonify({
            'id': new_review.id,
            'text': new_review.text,
            'user_id': new_review.user_id,
            'place_id': new_review.place_id
        }), 201

    @api.doc('get_reviews')
    def get(self):
        """List all reviews"""
        reviews = Review.query.all()
        return jsonify([
            {'id': r.id, 'text': r.text, 'user_id': r.user_id, 'place_id': r.place_id}
            for r in reviews
        ]), 200

@api.route('/<string:review_id>')
class Review(Resource):
    @api.doc('get_review')
    def get(self, review_id):
        """Get a specific review"""
        review = Review.query.get_or_404(review_id)
        return jsonify({
            'id': review.id,
            'text': review.text,
            'user_id': review.user_id,
            'place_id': review.place_id
        })

    @api.doc('update_review')
    @api.expect(review_model)
    def put(self, review_id):
        """Update a review"""
        review = Review.query.get_or_404(review_id)
        data = request.json
        review.text = data.get('text', review.text)
        review.user_id = data.get('user_id', review.user_id)
        review.place_id = data.get('place_id', review.place_id)
        db.session.commit()
        return jsonify({
            'id': review.id,
            'text': review.text,
            'user_id': review.user_id,
            'place_id': review.place_id
        })

    @api.doc('delete_review')
    def delete(self, review_id):
        """Delete a review"""
        review = Review.query.get_or_404(review_id)
        db.session.delete(review)
        db.session.commit()
        return '', 204
