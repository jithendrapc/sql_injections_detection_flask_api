  
from flask import Flask, jsonify, request,json
import re as re
app = Flask(__name__)

@app.route('/v1/sanitized/input/<string:str>', methods=['POST'])
def sql_injection_detection():
    data = json.loads(request.data)
    # Creating regular expression for sql injection string types
    sql_injection_regexpression = re.compile(r"(?i)(union|select|insert|update|delete|drop|alter|create|rename|truncate|replace|exec|declare|\$|;)")


    # Check if input string contains any disallowed characters
    if sql_injection_regexpression.search(data['input'],re.IGNORECASE):
        return jsonify({'result':'unsanitized'})
    return jsonify({'result':'sanitized'})
    

if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)