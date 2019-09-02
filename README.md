Installeer deze dependencies. [link](https://learn.adafruit.com/neopixels-on-raspberry-pi/python-usage)
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


# Tests

Run voor 18 leds per tegel.
```
sudo python3 18_leds.py
```

Run voor 36 leds per tegel.
```
sudo python3 36_leds.py
```

Run voor alle leds groen.
```
sudo python3 simple.py
```


# Server
Kopieer de server naar een uitvoerbaren locatie.
```
sudo ln -s $(pwd)/led-server /usr/local/bin/led-server
```

Run de server in een nieuwe terminal.
```
led-server
```

# Besturen
Zet de consul tegel aan.
```
curl -XPOST localhost:5000/led/consul
```

Zet de consul tegel uit.
```
curl -XDELETE localhost:5000/led/consul
```

Zet alle tegels aan.
```
curl -XPOST localhost:5000/led/all
```

Vraag de status op van de consul tegel.
```
curl -XGET localhost:5000/led/consul
```

Beschikbare tegels adressen.
```
# Product tegels.
localhost:5000/led/consul
localhost:5000/led/vagrant
localhost:5000/led/packer
localhost:5000/led/terraform
localhost:5000/led/vault
localhost:5000/led/nomad

# Center tegel.
localhost:5000/led/hashicorp

# Alle tegels.
localhost:5000/led/all
```

Beschikbare acties.
```
# Haal informatie over tegel.
curl -XGET

# Zet tegel aan.
curl -XPOST

# Zet tegel uit.
curl -XDELETE
```
