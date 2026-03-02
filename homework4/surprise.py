# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.

for star in targets:
    print(star)

# 2) Write a function that uses a loop to print the name of each star with its spectral type.

for star, info in targets.items():
    print(star, info["Spectral Type"])

# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.

def bright_stars(targets):
    result = []
    for star, info in targets.items():
        if info["Magnitude"] > 0.1:
            result.append(star)
    return result

print(bright_stars(targets))

# 4) Look up another target, add all the necessary information to the targets list. 

targets["Deneb"] = {
    "RA": "20h 41m 25.9s",
    "Dec": "+45° 16′ 49″",
    "Magnitude": 1.25,
    "Spectral Type": "A2Ia"
} # summer triangle!!
## print(targets) # view updated dictionary

# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
"""
kept getting error because dec is currently a string not a int/float so it needs to be converted according to google.
data type conversion:
"""
def dec_data_adjust(dec_str):
    sign = 1 if dec_str[0] == '+' else -1
    parts = dec_str[1:].replace('°',' ').replace('′',' ').replace('″',' ').split() # hopefully i did this right to make it a float
    deg, minutes, seconds = map(float, parts)
    return sign * (deg + minutes/60 + seconds/3600)

def brightest_near_dec20(targets):
    target_star = None
    most_accurate = None  # (declination difference, magnitude)

    for star, info in targets.items():
        dec = dec_data_adjust(info["Dec"])
        mag = info["Magnitude"]

        dec_diff = abs(dec - 20)

        score = (dec_diff, mag)

        if most_accurate is None or score < most_accurate:
            most_accurate = score
            target_star = star

    return target_star

print(brightest_near_dec20(targets)) 

# 6) What is your favorite constellation?
"""
My favorite constellation is probably Orion because I love Greek Mythology (Artemis in particular, hence I know the story of Orion),
and because it contains Betelgeuse, which is my/one of my favorite stars (honestly partly because it's so easy for me to identify with/without a telescope even with my eye/depth perception issues).
"""