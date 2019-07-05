from app import app


# from flask import Flask, jsonify, abort, make_response, request
#
#
# @app.route('/fakeDMP/api/v1.0/users', methods=['GET'])
# def get_user_info():
#     users = source[source["id"] == request.args.get("id")].to_dict(orient='records')
#     if (len(users) == 0):
#         abort(404)
#
#     coded_data = encode_data(users[0])
#     return jsonify(coded_data)
#
#
# @app.errorhandler(404)
# def not_found(error):
#     return make_response(jsonify({'error': 'not found'}), 404)
#
#
# if (__name__ == '__main__'):
#     app.run(debug=True)
