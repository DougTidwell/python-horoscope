# python-horoscope

A python implementation of the horoscope app. The four `.py` files deliver 
four different horoscopes: 

* **`optimistic`** - Cheery and upbeat. Example: "The stars say to treat yourself to a lavish dinner tonight." 
* **`ominous`** - Scary. Example: "The stars say to treat yourself to a lavish dinner tonight. Their exact words: 'As if it were your last meal.'"
* **`kafkaesque`** - Sad. Always ends with the phrase "Your life will be bleak and miserable." 
* **`planets_in_motion`** - Determined by the movement of planets and stars. Example: "Mercury said to tell you not to call the cops, or else. The stars assume you know what that's all about." 

Each version opens port 5000. The REST endpoint is `host:5000/horoscope/{sign}` with `sign` being one of the twelve (case-insensitive) signs of the zodiac. 

The `Dockerfile` is set up to take a `--build-args` parameter named SOURCE. That should be the filename
you'd like to build for a particular image. So `--build-args SOURCE=kafkaesque.py` will copy that file 
as `app.py` in the container image. 

The `.idea` directory has all of the configuration for PyCharm...there are configurations 
to build the four different images. 
