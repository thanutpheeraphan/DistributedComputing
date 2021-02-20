import easyimap

def test_send_email():
    login = 'toonkunggs@gmail.com'
    password = 'gvtmqzqtwhwhdpjh'

    imapper = easyimap.connect('imap.gmail.com', login, password)


    for mail_id in imapper.listids(limit = 20):
        mail = imapper.mail(mail_id)

        if 'toonkunggs@gmail.com' in mail.from_addr and 'Your fortune cookie today' in mail.title:
            return True
        else:
            return False
