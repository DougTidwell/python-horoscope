from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/horoscope/<sign>')
def getHoroscope(sign):
    match sign.lower():
        case "aries":
            return jsonify(
                horoscope="With the moon in the dining room of Cassiopeia, avoid making any financial decisions today.",
                provider="Planetary Motion",
                css="color: green;"
            )
        case "taurus":
            return jsonify(
                horoscope="Despite Orion roaming the meadows of Capricorn, the pen remains mightier than the sword. Still, " \
                          "the stars say you should definitely not go to work without your sword.",
                provider="Planetary Motion",
                css="color: green;"
            )
        case "gemini":
            return jsonify(
                horoscope="Even though Saturn is retrograde, don't be afraid " \
                          "to rock the boat today. Unless you're actually in a boat, in which case " \
                          "you should just sit down and shut up.",
                provider="Planetary Motion",
                css="color: green;"
            )
        case "cancer":
            return jsonify(
                horoscope="As Libra scampers through the tulip fields of Zeus, " \
                          "the stars suggest you ignore all the warning signs and have a great day.",
                provider="Planetary Motion",
                css="color: green;"
            )
        case "leo":
            return jsonify(
                horoscope="You wouldn't think it would be possible with the Pleiades " \
                          "in the powder room of Sagittarius, but it's happening today anyway. " \
                          "Good luck with that.",
                provider="Planetary Motion",
                css="color: green;"
            )
        case "virgo":
            return jsonify(
                horoscope="Neptune, relaxing in a hammock at Cygnus's place, " \
                          "casually mentioned he knows what you did last summer.",
                provider="Planetary Motion",
                css="color: green;"
            )
        case "libra":
            return jsonify(
                horoscope="Hercules has nothing to do with the stars, but " \
                          "he stopped by to suggest you stay in bed with the covers pulled up " \
                          "to your ears until Pisces enters the back yard of Jupiter.",
                provider="Planetary Motion",
                css="color: green;"
            )
        case "scorpio":
            return jsonify(
                horoscope="While Venus enjoys a mimosa on Bacchus's front porch, " \
                          "the stars say this is a perfect time to save money on car insurance.",
                provider="Planetary Motion",
                css="color: green;"
            )
        case "sagittarius":
            return jsonify(
                horoscope="As long as Taurus is swimming laps in the pool of " \
                          "Olympus, the stars aren't giving back your passport.",
                provider="Planetary Motion",
                css="color: green;"
            )
        case "capricorn":
            return jsonify(
                horoscope="Mercury said to tell you not to call the cops, or else. " \
                          "The stars assume you know what that's all about.",
                provider="Planetary Motion",
                css="color: green;"
            )
        case "aquarius":
            return jsonify(
                horoscope="Yes, you're an Aquarius, the water sign and all that, " \
                          "but the stars emphatically said not to get on any boat of any size " \
                          "until Mars starts wearing age-appropriate bathing suits.",
                provider="Planetary Motion",
                css="color: green;"
            )
        case "pisces":
            return jsonify(
                horoscope="Leda, enjoying some well-deserved downtime in the " \
                          "guest house of Scorpio, says the wolf at your door would probably " \
                          "make a great pet.",
                provider="Planetary Motion",
                css="color: green;"
            )
    return jsonify(
        horoscope="Sorry, you need to tell me your sign.",
        provider="Planetary Motion",
        css="color: red;"
    )


if __name__ == '__main__':
    app.run()
