from configparser import ConfigParser

conf= ConfigParser()
print(conf.read("data01.ini"))
print("Sections",conf.sections())
print("Result:",conf.get('TC001','url'))