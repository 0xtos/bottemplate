import configparser

inifile = configparser.SafeConfigParser()
inifile.read('settings.ini')

bybitApiKey = inifile.get('')
bybitSecret = inifile.get('')

lot = inifile.get('LOT', '0.1')
max_lot = inifile.get('LOT', '0.5')
interval = inifile.get('LOT', '15')
