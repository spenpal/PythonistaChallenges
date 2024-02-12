# February Challenge
*find the bomb*

The mythbusters are conducting an experiment. They've placed 3 sensors and a bomb in a flat 50x50km field, and want you to find where the bomb is based on the sensor data.
Each sensor records the time from the bomb exploding to the time the blast reaches it. Based on the location of each sensor, and the amount of time it took for the blast wave to arrive (in seconds), you'll need to find where the bomb is placed in the field. The coordinates start from the top left of the field, and only whole coordinates are relevant.
Each sensor provides its data as a tuple: `(x, y, time)`

note: the speed of sound is 0.343 km/sec

Your code should contain a `find` function that takes 3 arguments, the sensor tuples, and returns a tuple containing the x and y coordinates of the bomb.
```py
def find(s1: tuple[int, int, float], s2: tuple[int, int, float], s3: tuple[int, int, float]) -> tuple[int, int]:
  ...
```

Your test cases:
1. `(5, 8, 48.872), (12, 21, 35.107), (24, 20, 22.203)` -> `(21, 13)`
2. `(18, 42, 35.558), (39, 16, 106.004), (7, 24, 32.202)` -> `(8, 35)`
3. `(42, 19, 98.004), (3, 17, 122.484), (28, 29, 61.294)` -> `(29, 50)`

### Bonus challenges:
Because I'm late this month, no extra challenges aside from onelining.