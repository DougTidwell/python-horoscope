import flask

app = flask.Flask(__name__)

@app.route('/horoscope/<sign>')
def getHoroscope(sign):
  match sign.lower():
    case "aries":
      return flask.jsonify(
        horoscope="The stars suggest you talk to your friends and loved ones today.",
        provider="Planetary Motion",
        css="color: green;"
      )
    case "taurus":
      return flask.jsonify(
        horoscope="The stars say it\'s time for a vacation!",
        provider="Planetary Motion",
        css="color: green;"
      )
    case "gemini":
      return flask.jsonify(
        horoscope="The stars say you should put your irrational fears behind you and make the most of the day!",
        provider="Planetary Motion",
        css="color: green;"
      )
    case "cancer":
      return flask.jsonify(
        horoscope="The stars say something hilarious will happen to you today. Laugh hard!",
        provider="Planetary Motion",
        css="color: green;"
      )
    case "leo":
      return flask.jsonify(
        horoscope="The stars say your enemies will forgive you today.",
        provider="Planetary Motion",
        css="color: green;"
      )
    case "virgo":
      return flask.jsonify(
        horoscope="The stars say something will weigh heavily on your mind. Stay positive!",
        provider="Planetary Motion",
        css="color: green;"
      )
    case "libra":
      return flask.jsonify(
        horoscope="The stars say to stand up for yourself - today is no time to back down. You can do this!",
        provider="Planetary Motion",
        css="color: green;"
      )
    case "scorpio":
      return flask.jsonify(
        horoscope="The stars say you should be grateful for all the wonderful friends in your life. ",
        provider="Planetary Motion",
        css="color: green;"
      )
    case "sagittarius":
      return flask.jsonify(
        horoscope="The stars say a financial windfall could be yours today.",
        provider="Planetary Motion",
        css="color: green;"
      )
    case "capricorn":
      return flask.jsonify(
        horoscope="The stars say you should treat yourself to a lavish dinner tonight. You\'ve earned it!",
        provider="Planetary Motion",
        css="color: green;"
      )
    case "aquarius":
      return flask.jsonify(
        horoscope="The stars say you should make a generous, unexpected gift to someone you barely know today.",
        provider="Planetary Motion",
        css="color: green;"
      )
    case "pisces":
      return flask.jsonify(
        horoscope="The stars say to approach a confrontation with kid gloves and everything will be fine.",
        provider="Planetary Motion",
        css="color: green;"
      )
  return flask.jsonify(
    horoscope="Sorry, you need to tell me your sign.",
    provider="Planetary Motion",
    css="color: red;"
  )


if __name__ == '__main__':
  app.run()
