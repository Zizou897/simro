EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'azeridwan10@gmail.com'
EMAIL_HOST_PASSWORD = 'gqoezayyalfqbhhz'
EMAIL_PORT = 587


def send_email(admin_email, user_email, username, password):
    subject = "<strong>Création de compte</strong>"
    message = f"Votre compte vient d'etre créer. Voici vos access \nUsername: {username} \nPassword: {password} "
    from_email = admin_email
    to_email = user_email
    
    #send_mail(subject, message, from_email, to_email, fail_silently=False)
