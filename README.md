# Killerroute server
This is a server for the [killerroute](https://github.com/ldthorne/killerroute) project.

## Setup
You need python3. Run:
```bash
pip install -r requirements.txt
```

on linux you need to run:
```bash
# debian distros
sudo apt-get install libgeos-dev

# hipster distros
sudo yum install libgeos-dev
```

## Run
```bash
python server.py
```

## Use
Send a post request to `http://localhost:5000/crime/api` with the edges of a polygon in which you'd like to get dangerous spots.

Here is an example post:
```json
[
  {
    "lat": 40.7536250,
    "lng": -73.9798130
  },
  {
    "lat": 40.7536250,
    "lng": -73.9536640
  },
  {
    "lat": 40.6777800,
    "lng": -73.9798130
  },
  {
    "lat": 40.6777800,
    "lng": -73.9536640
  }
]
```

Here is the response:
```json
{
  "points": [
    [
      40.751892841,
      -73.969185569
    ],
    [
      40.740824511,
      -73.974260858
    ],
    [
      40.681443469,
      -73.961426743
    ],
    [
      40.679196261,
      -73.973909688
    ],
    [
      40.75044518,
      -73.975736907
    ],
    [
      40.683765609,
      -73.970987385
    ]
  ]
}
```


## Reference
Using [this](https://stackoverflow.com/questions/21328854/shapely-and-matplotlib-point-in-polygon-not-accurate-with-geolocation) for geolocation

The data comes from [here](https://maps.nyc.gov/crime/) and [here](https://data.cityofnewyork.us/Public-Safety/NYPD-Complaint-Data-Current-YTD/5uac-w243/data)