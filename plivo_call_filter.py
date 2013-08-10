import os
import plivoxml as plivo
from flask import Flask, request, make_response

app = Flask(__name__)

# RESET this to your preferred forwarding phone number
forward_number = "xxxxxxxxx"

hangup_static_xml = """
<Response>
<Hangup reason="busy"/>
</Response>
"""

# Block all numbers with prefixes from this list.
blocked_list = ['91','49', '18', 'sip', '14']


# Once hosted the answer_url would be "your_host_url/filter"
@app.route('/filter', methods=['POST'])
def filter_numbers():
    r = plivo.Response()
    from_number = request.form['From']
    if filter(lambda x: from_number.startswith(x), blocked_list):
        return hangup_static_xml
    else:
        r.addDial().addNumber(forward_number) 
        resp = make_response(r.to_xml())
        resp.headers['Content-Type'] = 'text/xml'
        return resp


if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get('PORT',5089)) 
    app.run(host='0.0.0.0',port=port)

