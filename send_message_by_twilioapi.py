import requests
from twilio.rest import Client

account_sid= 'AC31c011ec7c1e650d88df4dce91ce6147' #account_sid
auth_token= 'ee4cb042973b6ce8c53396650f3d5c79' #auth_token

client =Client(account_sid,auth_token)

number_to_text = '+9183475545454' #+1-(949)-441-3233
twilio_number = '+13214246562 ' #+1-(747)-233-2016
message_body = 'client test'
media_url ='https://cdn.pixabay.com/photo/2016/02/19/15/46/dog-1210559_960_720.jpg'

messages = client.messages.create(
    to=number_to_text,
    from_=twilio_number,
    body=message_body,
    media_url=media_url,


)
print(messages.sid)
print(messages.media_list.list()[0])





def xml_pretty(xml_string):
    import xml.dom.minidom
    xml = xml.dom.minidom.parseString(xml_string)
    pretty_xml_ = xml.toprettyxml()
    print(pretty_xml_)

base_url = 'https://api.twilio.com/2010-04-01/Accounts'
