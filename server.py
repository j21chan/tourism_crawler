from flask import Flask, request
import json
from tourism_database import tourism_database

# Create Server
app = Flask(__name__)


@app.route("/crawling_tourism", methods = ["GET"])
def crawling_tourism():
    ct = tourism_database()
    data = ct.get_tourism_list()
    return json.dumps(data, ensure_ascii=False)


# Main
if __name__ == "__main__":
    # Run Server
    app.run(debug=True, host="127.0.0.1", port="5009")