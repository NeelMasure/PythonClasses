from configparser import ConfigParser
from pyjavaproperties import Properties

def getValue(section,option):
    conf =ConfigParser()
    conf.read('data01.ini')
    value=conf.get(section, option)
    return value

def setValue(header,key,value):
    config= ConfigParser()
    config.add_section(header)
    config.set(header,key,value)
    with open("data01.ini","a") as dt:
        config.write(dt)

def getValueFromProp(key):
    prop = Properties
    prop.load(open("config.properties"))
    return prop.getProperty(key)