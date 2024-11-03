from Pytest_topics.utils.config_parser import getSectionParam

def test_get_gmail_url():
    print(getSectionParam('gmail','url'))
    assert getSectionParam('gmail','url') == 'qa.gmail.com'

def test_get_gmail_user():
    print(getSectionParam('gmail','user'))
    assert getSectionParam('gmail','user') == 'gmail.user1'

def test_get_fl_data():
    print(f'\n{getSectionParam('fl_1','iin')}')
    print(getSectionParam('fl_1','phone'))
    # assert getSectionParam('gmail','user') == 'gmail.user1'