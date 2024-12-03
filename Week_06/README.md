## Python for Begineers - Week 6

### Unit 3: Exercise

Import the `random` library and have a look at the function `gauss()` which gives back a random float number. Which parameters are required?
Write a function `gaussian_distribution()` that returns a list of 1000 random numbers with a mean of 100 and a standard deviation of 10. Invoke this function.

For the resulting list calculate and print the mean and the standard deviation using the respective functions from the `statistics` library.
Re-run the program and observe, if the values change.

Below is the output of an example execution of the program. Note that the values of the standard derivation and the mean might be different in your case.
```text
    Mean: 100.15215154056546
    Standard Deviation: 9.93532937167394
```

[Solution](./6.3/sol.py)
___
### Assignment - Accessing the Apple iTunes Search Service

In this assignment you are going to build a Python program to access the [Apple iTunes Search Service](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/Searching.html). This service can be used to search information about musicians, albums, songs and so on.

Using the following URL, a search for the term _ramones_ and for the entity type _album_ is performed: [https://itunes.apple.com/search?term=ramones&entity=album](https://itunes.apple.com/search?term=ramones&entity=album)

Other possible entity types are musicArtist, musicTrack or song. Below is an (abbreviated) example result of the service:
```json
    {
    "resultCount": 1,
    "results": [
        {
        "wrapperType": "collection",
        "collectionType": "Album",
        "artistId": 60715,
        "amgArtistId": 5223,
        "artistName": "Ramones",
        "collectionName": "Ramones",
        "collectionPrice": 9.99,
        "collectionExplicitness": "notExplicit",
        "trackCount": 14,
        "copyright": "℗ 1976 Sire Records. Marketed by Rhino Entertainment Company, a Warner Music Group Company.",
        "country": "USA",
        "currency": "USD",
        "releaseDate": "1976-04-23T08:00:00Z",
        "primaryGenreName": "Punk"
        }
    ]
    }
```
The response in the example above consists of one result (`resultCount` is 1). This result is the album "Ramones" (element `collectionName`) by the artist "Ramones" (element `artistName`). The response is in [JSON](https://en.wikipedia.org/wiki/JSON) format.

The [Requests](https://docs.python-requests.org/en/latest/) library can be used to invoke the Apple iTunes Search Service. In order to perform a search, a [GET request](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#Request_methods) needs to be performed. This is done using the `get()` function of the Requests library.
After that, the method `json()` of the Requests library can be used to map the response from [JSON](https://en.wikipedia.org/wiki/JSON)
qo the Python 🐍 data types `dict` and `list`.

Write a program that asks the user for a search term. Perform a search using the iTunes search service for the entity type album. The program should then print how many search results where returned.
For each result print the artist name, the album name and track count.

Below is an example execution of the program. Note that the output is abbreviated.
```text
    Please enter a search term: cash
    The search returned 50 results.
    Artist: Luke Bryan - Album: Crash My Party - Track Count: 13
    Artist: Johnny Cash - Album: The Essential Johnny Cash - Track Count: 36
    Artist: Dave Matthews Band - Album: Crash - Track Count: 12
```
#### Hints

1. In Code Ocean it is not possible to access the iTunes search API. Therefore you should write and test your program on your own computer e.g. in a Jupyter notebook.
1. Our tests in Code Ocean use a [mock object](https://en.wikipedia.org/wiki/Mock_object) to check your program. Therefore only the `get()` function and the `json()` method are supported. All other functions and methods of the Requests library will **not** work.

[Solution](./Assignment/sol.py)
___
### Assignment - Quiz

[Week 06 - Assignment Part-1 (Questions) Solutions](./quizAssg.md)

Note [⚠] <br>
Make sure to solve the quiz on your own. Refer the solutions only after solving the quiz.
___
### Bonus Assignment - Compute π using a random number generator

The number *π (Pi)* can be calculated using random numbers. Suppose you have a circle with radius 1 which is inscribed in a square with a side length of 2 (see figure below). Then the square has an area of *4 (2 \* 2)* and the circle has an area of *π (r = 1*, thus *π \* r² = π*).

![Circle](https://opensap-public.s3.openhpicloud.de/courses/2qRB6Gz3FcfD2OBbnSCf8m/rtfiles/3zuTN0fWCxUJlHG2ZzSc5f/img1.png)

If thousands of points are randomly created within the square, then some points are inside the square _and_ inside the circle, others are inside the square and _not_ inside the circle. 
The situation can be simplified if you just consider the upper right quadrant of the above figure. This square has a side length of 1. Each point within the square can be described by the coordinates *x* and *y* where ***(0 < x, y < 1)***. If ***x² + y² < 1***, then a point specified by ***(x, y)*** lies within the circle.

![Quad](https://opensap-public.s3.openhpicloud.de/courses/2qRB6Gz3FcfD2OBbnSCf8m/rtfiles/39m9UzKKSMHhDI3eZNbeBp/img2.png)

As the relation between the sizes of circle and square is *π/4*, the relation between the points in the circle and the points in the square must be *π/4* as well. Using this formula, one can now use a random number generator to calculate π.

#### Your Task

Using the library `random` create 10,000 random points inside the square. That means generate 10,000 random pairs of values for *x* and *y*. The random value must be between 0 and 1 in order for a point to be inside the square.
For each point check if ***x² + y² is < 1***. If this is the case, then the point is within the circle. Count the total number of points and the points which are in the circle. Use these numbers to calculate *π*.
Finally compare your calculated value of *π* with the value of *π* found in the `math` library. Do this by printing the calculated value of *π*, the value from the math library as well as the difference.

Below is an example execution of the program. Note that your values might be different.
```text
    Calculated value of π: 3.1396
    Value of π from math library: 3.141592653589793
    Difference: -0.0019926535897929476
```

#### Additional Challenge

Can you solve the bonus exercise without a for loop using list comprehension? [Solution (List Comprehension)](./Bonus/alt_sol)

[Solution](./Bonus/sol.py)