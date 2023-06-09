import flask
import flask_cors

app = flask.Flask(__name__)
flask_cors.CORS(app)

@app.route('/horoscope/<sign>')
def getHoroscope(sign):
  match sign.lower():
    case "aries":
      return flask.jsonify(
        horoscopeText="You will be arrested today. You will never be told the nature of the charges against you. Your life will be bleak and miserable.",
        serviceName="Kafkaesque",
        css="color: green;"
      )
    case "taurus":
      return flask.jsonify(
        horoscopeText="You will feel your father\'s disapproval keenly today. Pretty much like every other day. Your life will be bleak and miserable.",
        serviceName="Kafkaesque",
        css="color: green;"
      )
    case "gemini":
      return flask.jsonify(
        horoscopeText="After tomorrow, let\'s just say you\'ll be wearing shoes six at a time. Shop accordingly. Your life will be bleak and miserable.",
        serviceName="Kafkaesque",
        css="color: green;"
      )
    case "cancer":
      return flask.jsonify(
        horoscopeText="You will write the person you love, telling them your relationship will never happen. They will never write back. Your life will be bleak and miserable.",
        serviceName="Kafkaesque",
        css="color: green;"
      )
    case "leo":
      return flask.jsonify(
        horoscopeText="The excitement of finding a new form of disappointment will fade quickly. Your life will be bleak and miserable.",
        serviceName="Kafkaesque",
        css="color: green;"
      )
    case "virgo":
      return flask.jsonify(
        horoscopeText="You will have a sudden insight that will bring you lasting peace and contentment. Just kidding. Your life will be bleak and miserable.",
        serviceName="Kafkaesque",
        css="color: green;"
      )
    case "libra":
      return flask.jsonify(
        horoscopeText="Your lawyer will assure you that this will all be over soon. He is correct, but not in a good way. Your life will be bleak and miserable.",
        serviceName="Kafkaesque",
        css="color: green;"
      )
    case "scorpio":
      return flask.jsonify(
        horoscopeText="What happens today won\'t be any more bearable if the stars tell you about it beforehand, so let\'s leave it at that. Your life will be bleak and miserable.",
        serviceName="Kafkaesque",
        css="color: green;"
      )
    case "sagittarius":
      return flask.jsonify(
        horoscopeText="Not everybody would keep pursuing an unobtainable goal, but you seem to have a real flair for it. Your life will be bleak and miserable.",
        serviceName="Kafkaesque",
        css="color: green;"
      )
    case "capricorn":
      return flask.jsonify(
        horoscopeText="You will start the day with a really good cappuccino. Like, seriously good. But it\'ll all be downhill from there. Your life will be bleak and miserable.",
        serviceName="Kafkaesque",
        css="color: green;"
      )
    case "aquarius":
      return flask.jsonify(
        horoscopeText="You don\'t have a dog, but even if you did, it wouldn\'t like you. Your life will be bleak and miserable.",
        serviceName="Kafkaesque",
        css="color: green;"
      )
    case "pisces":
      return flask.jsonify(
        horoscopeText="Your city will have an amazing zoo, but you\'ll never live to see it. Your life will be bleak and miserable.",
        serviceName="Kafkaesque",
        css="color: green;"
      )
  return flask.jsonify(
    horoscopeText="Sorry, you need to tell me your sign.",
    serviceName="Kafkaesque",
    css="color: red;"
  )


if __name__ == '__main__':
  app.run()
