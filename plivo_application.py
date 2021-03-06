import plivo


auth_id = ""
auth_token = ""

p = plivo.RestAPI(auth_id, auth_token)


# Create application
params = {
    'app_name' : 'Gandalf the Gray',
    'answer_url' : 'http://example.com/answer_url',
    'answer_method' : 'POST',
    'hangup_url' : 'http://example.com/hangup_url',
    'hangup_method' : 'POST',
    'fallback_url' : 'http://example.com/fallback_url',
    'fallback_method' : 'POST',
}
response = p.create_application(params)


# Modify application
response = p.modify_application(params)


# Delete application
params = {
    'app_id' : 'XXXXXXXXXXXXXXXXXXXXX',
}
response = p.delete_application(params)


# Create subaccount application
params = {
    'subaccount' : ' XXXXXXXXXXXX',
    'app_name' : 'Gimli the dwarf',
    'answer_url' : 'http://example.com/answer_url',
    'answer_method' : 'POST',
    'hangup_url' : 'http://example.com/hangup_url',
    'hangup_method' : 'POST',
    'fallback_url' : 'http://example.com/fallback_url',
    'fallback_method' : 'POST',
}
response = p.create_application(params)
