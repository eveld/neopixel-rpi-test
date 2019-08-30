Installeer deze dependencies.
```
sudo apt-get update && sudo apt-get install git
sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel
```

Download de code naar de pi.
```
git clone https://github.com/eveld/neopixel-test.git
```

Sluit de data lijn van de neopixel aan op pin18 van de raspberry pi.

Ga naar de directory met de scripts.
```
cd neopixel-test
```

Run voor 18 leds per tegel.
```
python 18_leds.py
```

Run voor 36 leds per tegel.
```
python 36_leds.py
```
