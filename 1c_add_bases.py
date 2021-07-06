#!python
import os, codecs, configparser, sys

def add_database_from_file(src):
    global CONF_FILE_1C, CONF_FILE_1C_ENCODING
    with codecs.open(src, 'r', CONF_FILE_1C_ENCODING) as fs, codecs.open(CONF_FILE_1C, 'a', CONF_FILE_1C_ENCODING) as fd:
        fd.writelines(fs.readlines())
        fd.writelines(os.linesep)

def clean_user_config():
    global DIR
    F1=os.path.join(DIR, '1CEStart.cfg')
    F2=os.path.join(DIR, 'ibases.v8i')
    if not os.path.exists(DIR):
        os.makedirs(DIR)
        open(F2, 'w').close()
        return
    if os.path.exists(F1): open(F1, 'w').close()
    if os.path.exists(F2): open(F2, 'w').close()    

DIR=os.path.join(os.environ['AppData'], r'1C\1CEStart')
CURRENT_USER = os.environ['UserName'].lower()
CURRENT_USER_NEEDS_CLEAN = True
CONF_FILE_1C=os.path.join(DIR, '1CEStart.cfg')
CONF_FILE_1C_ENCODING='UTF-16LE'
CONFIG_NAME='1c_add_bases.conf'
CONFIG=os.path.join(os.path.dirname(sys.argv[0]), CONFIG_NAME)
config = configparser.ConfigParser()
config.read(CONFIG)
for section in config.sections():
    if 'Users' not in config[section]: break
    section_users=[u.strip().lower() for u in config[section]['Users'].split(',')]    
    if CURRENT_USER in section_users:
        if (CURRENT_USER_NEEDS_CLEAN):
            clean_user_config()
            CURRENT_USER_NEEDS_CLEAN = False
        add_database_from_file(section)
