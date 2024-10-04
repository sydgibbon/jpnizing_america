from flask import Blueprint, request, jsonify
from .models import Class, User
from flask_jwt_extended import ( jwt_required, get_jwt_identity
)

classes_bp = Blueprint('classes', __name__)

@classes_bp.route('/classes', methods=['GET'])
@jwt_required
def get_classes():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    classes = Class.query.all()
    return jsonify([cls.to_dict() for cls in classes])

# @classes_bp.route('/classes', methods=['POST'])
# @jwt_required
# def create_class():
#     db = get_db()
#     data = request.json
#     new_class = Class(title=data['title'], video_url=data['video_url'], section_id=data['section_id'])
#     db.session.add(new_class)
#     db.session.commit()
#     return jsonify(new_class.to_dict()), 201

# @classes_bp.route('/classes/<int:id>', methods=['PUT'])
# @jwt_required
# def update_class(id):
#     db = get_db()
#     cls = Class.query.get_or_404(id)
#     data = request.json
#     cls.title = data.get('title', cls.title)
#     cls.video_url = data.get('video_url', cls.video_url)
#     cls.section_id = data.get('section_id', cls.section_id)
#     db.session.commit()
#     return jsonify(cls.to_dict())

# @classes_bp.route('/classes/<int:id>', methods=['DELETE'])
# @jwt_required
# def delete_class(id):
#     db = get_db()
#     cls = Class.query.get_or_404(id)
#     db.session.delete(cls)
#     db.session.commit()
#     return '', 204
