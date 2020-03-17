import os
import sentry_sdk

from bottle import route, run
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    dsn="https://70e4a0d5f8564afa85b908c5c5e948b2@sentry.io/2823624",
    integrations=[BottleIntegration()]
)

# app = Bottle()

@route('/')  
def root():
    print('i am here')
    return "OK"

@route('/fail')  
def fail_func():  
    raise RuntimeError("There is an error!")  
    return  

@route('/success')  
def success_func():  
    return "success"
  
  
# app.run(host='localhost', port=8080)
if os.environ.get("APP_LOCATION") == "heroku":
    run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    run(host="localhost", port=8080, debug=True)
