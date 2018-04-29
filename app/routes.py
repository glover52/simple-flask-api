from flask import request
from flask import jsonify
from flask_api import status
from re import escape

from app import app
from app import mc  # The cache


@app.route('/')
@app.route('/index')
def index():
    return ""


@app.route('/messages', methods=['GET', 'POST'])
@app.route('/messages/<path:key>', methods=['GET'])
def messages(key=None):
    if request.method == "POST":
        # Check if required POST body elements exist to form document
        if not request.form.get('id'):
            return "ERROR: No ID entered", status.HTTP_400_BAD_REQUEST
        if not request.form.get('message'):
            return "ERROR: No message entered", status.HTTP_400_BAD_REQUEST

        # Set the id of the new message and check for abnormalities
        try:
            key = str(int(escape(request.form['id'])))
            if mc.get(key) is not None:
                return "ID already exists", status.HTTP_400_BAD_REQUEST
        except ValueError:
            return "ID must be an integer", status.HTTP_400_BAD_REQUEST

        message = escape(request.form['message'])

        # Set time to live (TTL) for document
        ttl = 30
        if request.form.get('ttl'):
            try:
                ttl = int(escape(request.form['ttl']))
                if ttl <= 1:
                    return "TTL must be above 0", status.HTTP_400_BAD_REQUEST
            except ValueError:
                return "TTL must be an integer", status.HTTP_400_BAD_REQUEST

        # Add message to the cache and return success message
        mc.set(key, message, time=ttl)
        return "Message \"{}\" added with ID of: {} (TTL:{}s)".format(
            message,
            key,
            ttl
        )

    else:
        # Return message with given id
        if key is not None:
            try:
                key = str(int(escape(key)))
                message = mc.get(key)
                if message is not None:
                    return message
                else:
                    return "Resource not found", status.HTTP_404_NOT_FOUND
            except ValueError:
                return "Please enter a number", status.HTTP_400_BAD_REQUEST

        # Return all messages if no id was given
        # json_data = [{"id": k, "message": x} for k, x in cache.items()]
        json_data = []
        return jsonify(Messages=json_data)


@app.route('/clearCache', methods=['POST'])
def clear_cache():
    mc.flush_all()
    return "Cache cleared!"
