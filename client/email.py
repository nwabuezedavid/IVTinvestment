# from django_email import djemail

# # Simple Usage
# # Admin will receive a message
# djemail.send_email(message="My Message", subject="The Subject")

# # Send an email to a specific email
# djemail.send_email(
#         to="email@test.com",
#         message="My Message",
#         subject="The Subject")

# # Advanced Usage
# djemail.send_email(
#     to="email@test.com",
#     template_name="path/to/template", # .txt and/or .html
#     context={'variable': 'Variable Content'},
#     subject="My Subject"
# )