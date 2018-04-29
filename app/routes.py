from app import app
from flask import request
from flask import jsonify
# from app import cache
from app import mc


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/messages', methods=['GET', 'POST'])
@app.route('/messages/<path:id>', methods=['GET'])
def messages(id=None):
    if request.method == "POST":
        if not request.form.get('id'):
            return "ERROR: No ID entered"

        # Check if 'message' key exists
        if not request.form.get('message'):
            return "ERROR: No message entered"

        mId = request.form['id']
        message = request.form['message']
        ttl = int(request.form['ttl']) if request.form.get('ttl') else 30

        if mc.get(mId) is not None:
            return "Key already exists"

        # if cache.get(mId) is not None:
        #     return "Key already exists!"

        # cache[mId] = message
        mc.set(mId, message, time=ttl)
        return "Done"

    else:
        # Return message with given id
        if id is not None:
            # message = cache.get(id)
            message = mc.get(id)
            # Return message if found else return error message
            return message if message is not None else ("Resource not found", 404)

        # Return all messages if no id was given
        # json_data = [{"id": k, "message": x} for k, x in cache.items()]
        json_data = []
        return jsonify(Messages=json_data)


@app.route('/clearCache', methods=['POST'])
def clear_cache():
    # cache.clear()
    mc.flush_all()
    return "Cache cleared!"


@app.route('/setTTL', methods=['POST'])
def set_ttl():
    if request.form.get('ttl'):
        try:
            ttl = int(request.form.get['ttl'])
            # cache.max_age = ttl
            return "Cache TTL set to {} seconds.".format(ttl)
        except ValueError:
            return "Invalid time"
    else:
        return "No TTL time entered."
