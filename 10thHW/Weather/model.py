from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

def GetWeather(): 
    owm = OWM('OWN API key')   
    mngr = owm.weather_manager()
    observation = mngr.weather_at_place('Saint Petersburg, RU')
    w = observation.weather
    print(w.temperature('celsius'))