#! /usr/bin/python

from flask import Flask, render_template, request, make_response, url_for
import plivo
import smtplib

app = Flask(__name__)

def sendemail(from_addr, to_addr_list, cc_addr_list, subject, message, login,
password, smtpserver='smtp.gmail.com:587'):
    header  = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message                 
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr,to_addr_list, message)
    server.quit()

@app.route('/',methods=['POST'])
def mail_inbound_sms():
    print "\n=======message received:=============>"
    record_action = request.form.items();
    print record_action
    From = request.form.get('From','')
    to = request.form.get('To','')
    text = request.form.get('Text','')
    print "from",From
    print "to",to
    print "text",text
    print "\n==========email message=====>"
    body = "message\n from: "+str(From)+"\n To: "+str(to)+"\n Text: "+text
    sendemail(from_addr    = '<from email address>',
        to_addr_list = ['<to email address>'],
        cc_addr_list = ['email address in cc'],
        subject      = "SMS from "+str(From),
        message      = body,
        login        = '<gmail user name>',
        password     = '<gmail password>')
    return("email sent for inbound sms")

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 5080, debug = True)
