from flask import Flask, request
import redis
import logging
import os

app = Flask(__name__)

# Configuración de Redis
redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_port = int(os.getenv('REDIS_PORT', 6379))
redis_password = os.getenv('REDIS_PASSWORD', '')

r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

# Configuración de logging
log_file = 'logs/log.txt'
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s %(message)s')

@app.route('/')
def hello():
    count = r.incr('counter')
    app.logger.info(f'Page visited {count} times.')
    return f'Hello! This page has been visited {count} times.'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
