import flask
import flask_cors

app = flask.Flask(__name__)
flask_cors.CORS(app)

@app.route('/horoscope/<sign>')
def getHoroscope(sign):
  match sign.lower():
    case "aries":
      return flask.jsonify(
        horoscopeText="The stars suggest you talk to your friends and loved ones today.",
        serviceName="Optimistic",
        css="color: green;"
      )
    case "taurus":
      return flask.jsonify(
        horoscopeText="The stars say it\'s time for a vacation!",
        serviceName="Optimistic",
        css="color: green;"
      )
    case "gemini":
      return flask.jsonify(
        horoscopeText="The stars say you should put your irrational fears behind you and make the most of the day!",
        serviceName="Optimistic",
        css="color: green;"
      )
    case "cancer":
      return flask.jsonify(
        horoscopeText="The stars say something hilarious will happen to you today. Laugh hard!",
        serviceName="Optimistic",
        css="color: green;"
      )
    case "leo":
      return flask.jsonify(
        horoscopeText="The stars say your enemies will forgive you today.",
        serviceName="Optimistic",
        css="color: green;"
      )
    case "virgo":
      return flask.jsonify(
        horoscopeText="The stars say something will weigh heavily on your mind. Stay positive!",
        serviceName="Optimistic",
        css="color: green;"
      )
    case "libra":
      return flask.jsonify(
        horoscopeText="The stars say to stand up for yourself - today is no time to back down. You can do this!",
        serviceName="Optimistic",
        css="color: green;"
      )
    case "scorpio":
      return flask.jsonify(
        horoscopeText="The stars say you should be grateful for all the wonderful friends in your life.",
        serviceName="Optimistic",
        css="color: green;"
      )
    case "sagittarius":
      return flask.jsonify(
        horoscopeText="The stars say a financial windfall could be yours today.",
        serviceName="Optimistic",
        css="color: green;"
      )
    case "capricorn":
      return flask.jsonify(
        horoscopeText="The stars say you should treat yourself to a lavish dinner tonight. You\'ve earned it!",
        serviceName="Optimistic",
        css="color: green;"
      )
    case "aquarius":
      return flask.jsonify(
        horoscopeText="The stars say you should make a generous, unexpected gift to someone you barely know today.",
        serviceName="Optimistic",
        css="color: green;"
      )
    case "pisces":
      return flask.jsonify(
        horoscopeText="The stars say to approach a confrontation with kid gloves and everything will be fine.",
        serviceName="Optimistic",
        css="color: green;"
      )
  return flask.jsonify(
    horoscopeText="Sorry, you need to tell me your sign.",
    serviceName="Optimistic",
    css="color: red;"
  )


if __name__ == '__main__':
  app.run()
