from tasks import email_sender


if __name__ == '__main__':
    emails = [email for email in open('emails.txt')]
    message = ""
    with open('message.txt') as f:
        for line in f:
            message += line
            
    result  = email_sender.delay(emails,message)
    
    