# Celestial API Documentation:

This API serves as a database of information on several classes of celestial bodies. Contains data on vast array of planets, moons, stars, asteroids, stars and black holes. These are the classes for now, but there may be new classes added later on.

## API Endpoints:

* getdata:
    This endpoint can be used to get all data specific to a celestial body in a neatly labelled dictionary format.

* adddata:
    This can be used by contributors to add data pertaining to a new celestial body that is so far not a part of the database. Data that should be included before contributing is present in this file.

* getlist:
    This can be used to get a list of names of celestial bodies that fit the required parameters. highly flexible endpoint that allows users to specify their exact parameters. 

All endpoints take inputs in dictionary format.

## Formats of data available for each celestial body:

|Planets|Moons|Asteroids|Stars|Blackholes|
|-------|-----|---------|-----|----------|
|Name|Name|Name|Name|Name|
|Colors|Colors|Colors|Colors|Solar masses|
|Mass|Mass|Mass|Solar masses|Location|
|Temperature|Temperature|Location|Temperature|Size|
|Star|Planet name|Distance from Earth|System name|Trivia|
|Distance from Earth|Discovered by|Minerals in crust|Distance from Earth||
|Distance from its star|Minerals in crust|Source|Age||
|Discovered by|Gases in atmosphere|Trivia|Planets||
|Minerals in crust|Atmospheric pressure||Size||
|Gases in atmosphere|Age||Trivia||
|Atmospheric pressure|Trivia||||
|Moons|||||
|Age|||||
|Trivia|||||