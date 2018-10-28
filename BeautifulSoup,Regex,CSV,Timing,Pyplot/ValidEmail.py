import re

def is_valid_email_address(mystr):
    match=re.fullmatch('[^._%+-][\w]+[^._%+-]@([\w.]+)\w', mystr)
    return match is not None

if __name__ == '__main__':
    assert is_valid_email_address('rhanspal@smu.edu')==True
    assert is_valid_email_address('rhanspal@gmail.com') ==True
    assert is_valid_email_address('rhanspal@smu.org') == True
    assert is_valid_email_address('Rhanspal@smu.org') == True
    assert is_valid_email_address('RHANSPAL@smu.org') == True
    assert is_valid_email_address('rhanspal113@gmail.com') ==True
    assert is_valid_email_address('.rhanspal@smu.edu') ==False
    assert is_valid_email_address('rhanspal@smu.edu.') ==False
    assert is_valid_email_address('.rhanspal@smu.edu.') ==False
    assert is_valid_email_address('_rhanspal@smu.edu') ==False
    assert is_valid_email_address('rhanspal_@smu.edu') ==False