from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
 
owm = OWM('6eb60b5fc9bbb98369ba61684926f218')
mgr = owm.weather_manager()
 
 
observation = mgr.weather_at_place('London,GB')
w = observation.weather
 
print(w.temperature('celsius'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}