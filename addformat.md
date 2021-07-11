# For contributing:

* make sure the below mentioned datapoints are ready for the celestial body you want to add.
* place the data in a dictionary with the keys being the labels mentioned.
* put the dictionary in a .py file and push the file to this repository under the contributions directory.

## Datapoints:

1. Planets:

|Label|Explanation|
|-----|-----------|
|"colors"|a python list of the colors that are predominantly expressed by the planet. Each color is in string format|
|"mass"|mass of the planet in kilograms in string format. (Eg: if its 40495490 kg, then "mass":"4.04x10^7)|
|"temperature"|a python list with two elements. [min temp(night temp), max temp(day temp)]. both elements must be in string format and the temperature is expressed in Celsius scale|
|"star"|name of the star the planet orbits, in string format|
|"status"|status of the planet, "planet", "dwarf", "rogue" etc..|
|"type"|type of the planet "terrestrial" or "giant"|
|"rings"|"yes" or "no" for if the planet has rings|
|"dfromearth"|distance of the planet from earth, in Astronomical Units, in string format|
|"dfromstar"|distance of the planet from it's star, in Astronomical Units, in string format|
|"elements"|python list consisting of the elements mostly found on the planet, in string format|
|"atmosphere"|a python dictionary where the gases are keys and their percentage compositions are the values|
|"atmpressure"|atmospheric pressure on the planet's surface in pascals, in string format. includes multiplier like n, u, m, k etc for nano micro, milli, kilo respectively. for gas giants, surface pressure is undefined so 100kPa is standard|
|"moons"|a python list containing the names of the moons of the planet in string format|