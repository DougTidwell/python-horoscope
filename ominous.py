import flask
import flask_cors

app = flask.Flask(__name__)
flask_cors.CORS(app)

@app.route('/horoscope/<sign>')
def getHoroscope(sign):
  match sign.lower():
    case "aries":
      return flask.jsonify(
        horoscopeText="The stars won\'t say exactly what will happen today, but they suggest you say goodbye to your friends and loved ones.",
        serviceName="Ominous",
        css="color: green;"
      )
    case "taurus":
      return flask.jsonify(
        horoscopeText="The stars suggest you leave town until the whole thing blows over.",
        serviceName="Ominous",
        css="color: green;"
      )
    case "gemini":
      return flask.jsonify(
        horoscopeText="The stars stand corrected: turns out your irrational fears are completely justified.",
        serviceName="Ominous",
        css="color: green;"
      )
    case "cancer":
      return flask.jsonify(
        horoscopeText="The stars say something hilarious will happen to you today. Keep in mind that the stars have a really mean sense of humor.",
        serviceName="Ominous",
        css="color: green;"
      )
    case "leo":
      return flask.jsonify(
        horoscopeText="The stars say your enemies will forgive you today. They\'ll still press charges, but it won\'t be anything personal.",
        serviceName="Ominous",
        css="color: green;"
      )
    case "virgo":
      return flask.jsonify(
        horoscopeText="The stars say a steamroller figures prominently in your future. You shouldn\'t worry, as long as you drive a steamroller for a living.",
        serviceName="Ominous",
        css="color: green;"
      )
    case "libra":
      return flask.jsonify(
        horoscopeText="The stars say to stand up for yourself - today is no time to back down. They recommend standing up to someone small and unarmed.",
        serviceName="Ominous",
        css="color: green;"
      )
    case "scorpio":
      return flask.jsonify(
        horoscopeText="The stars say you should be grateful for all the wonderful friends in your life. All your friends are imaginary, so that\'s probably not a big deal.",
        serviceName="Ominous",
        css="color: green;"
      )
    case "sagittarius":
      return flask.jsonify(
        horoscopeText="The stars say a financial windfall could be yours today. The stars also rolled their eyes and said, \"Yeah, right.\"",
        serviceName="Ominous",
        css="color: green;"
      )
    case "capricorn":
      return flask.jsonify(
        horoscopeText="The stars say you should treat yourself to a lavish dinner tonight. Their exact words: \"As if it were your last meal.\"",
        serviceName="Ominous",
        css="color: green;"
      )
    case "aquarius":
      return flask.jsonify(
        horoscopeText="The stars say you should make a generous, unexpected gift to someone you barely know today. It probably won\'t get you out of hot water with Human Resources, but it couldn\'t hurt.",
        serviceName="Ominous",
        css="color: green;"
      )
    case "pisces":
      return flask.jsonify(
        horoscopeText="The stars say to approach a confrontation with kid gloves and everything will be fine...for your opponent, who\'s wearing brass knuckles.",
        serviceName="Ominous",
        css="color: green;"
      )
  return flask.jsonify(
    horoscopeText="Sorry, you need to tell me your sign.",
    serviceName="Ominous",
    css="color: red;"
  )


if __name__ == '__main__':
  app.run()
