import flask
import flask_cors

app = flask.Flask(__name__)
flask_cors.CORS(app)

@app.route('/horoscope/<sign>')
def getHoroscope(sign):
  match sign.lower():
    case "aries":
      return flask.jsonify(
        horoscopeText="With the moon in the dining room of Cassiopeia, avoid making any financial decisions today.",
        serviceName="Planetary Motion",
        css="color: green;"
      )
    case "taurus":
      return flask.jsonify(
        horoscopeText="Despite Orion roaming the meadows of Capricorn, the pen remains mightier than the sword. Still, " \
                  "the stars say you should definitely not go to work without your sword.",
        serviceName="Planetary Motion",
        css="color: green;"
      )
    case "gemini":
      return flask.jsonify(
        horoscopeText="Even though Saturn is retrograde, don't be afraid " \
                  "to rock the boat today. Unless you're actually in a boat, in which case " \
                  "you should just sit down and shut up.",
        serviceName="Planetary Motion",
        css="color: green;"
      )
    case "cancer":
      return flask.jsonify(
        horoscopeText="As Libra scampers through the tulip fields of Zeus, " \
                  "the stars suggest you ignore all the warning signs and have a great day.",
        serviceName="Planetary Motion",
        css="color: green;"
      )
    case "leo":
      return flask.jsonify(
        horoscopeText="You wouldn't think it would be possible with the Pleiades " \
                  "in the powder room of Sagittarius, but it's happening today anyway. " \
                  "Good luck with that.",
        serviceName="Planetary Motion",
        css="color: green;"
      )
    case "virgo":
      return flask.jsonify(
        horoscopeText="Neptune, relaxing in a hammock at Cygnus's place, " \
                  "casually mentioned he knows what you did last summer.",
        serviceName="Planetary Motion",
        css="color: green;"
      )
    case "libra":
      return flask.jsonify(
        horoscopeText="Hercules has nothing to do with the stars, but " \
                  "he stopped by to suggest you stay in bed with the covers pulled up " \
                  "to your ears until Pisces enters the back yard of Jupiter.",
        serviceName="Planetary Motion",
        css="color: green;"
      )
    case "scorpio":
      return flask.jsonify(
        horoscopeText="While Venus enjoys a mimosa on Bacchus's front porch, " \
                  "the stars say this is a perfect time to save money on car insurance.",
        serviceName="Planetary Motion",
        css="color: green;"
      )
    case "sagittarius":
      return flask.jsonify(
        horoscopeText="As long as Taurus is swimming laps in the pool of " \
                  "Olympus, the stars aren't giving back your passport.",
        serviceName="Planetary Motion",
        css="color: green;"
      )
    case "capricorn":
      return flask.jsonify(
        horoscopeText="Mercury said to tell you not to call the cops, or else. " \
                  "The stars assume you know what that's all about.",
        serviceName="Planetary Motion",
        css="color: green;"
      )
    case "aquarius":
      return flask.jsonify(
        horoscopeText="Yes, you're an Aquarius, the water sign and all that, " \
                  "but the stars emphatically said not to get on any boat of any size " \
                  "until Mars starts wearing age-appropriate bathing suits.",
        serviceName="Planetary Motion",
        css="color: green;"
      )
    case "pisces":
      return flask.jsonify(
        horoscopeText="Leda, enjoying some well-deserved downtime in the " \
                  "guest house of Scorpio, says the wolf at your door would probably " \
                  "make a great pet.",
        serviceName="Planetary Motion",
        css="color: green;"
      )
  return flask.jsonify(
    horoscopeText="Sorry, you need to tell me your sign.",
    serviceName="Planetary Motion",
    css="color: red;"
  )


if __name__ == '__main__':
  app.run()
