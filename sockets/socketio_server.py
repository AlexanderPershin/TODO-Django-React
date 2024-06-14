import socketio
import redis
import logging
import json
from urllib import parse

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

sio = socketio.AsyncServer(async_mode="asgi")
app = socketio.ASGIApp(sio)

redis_client = redis.StrictRedis(host="redis", port=6379, db=1)


def get_sid(user_id):
    logger.debug(f"get_sid user_id == {user_id}")
    return redis_client.get(user_id)


def store_sid(user_id, sid):
    logger.debug(f"store_sid user_id == {user_id} sid == {sid}")
    redis_client.set(str(user_id), sid)


def remove_sid(sid):
    user_ids = redis_client.keys("*")
    for user_id in user_ids:
        if redis_client.get(user_id).decode("utf-8") == sid:
            redis_client.delete(user_id)


@sio.event
async def connect(sid, environ):
    user_id = None
    try:
        query_params = dict(parse.parse_qsl(environ["QUERY_STRING"]))
        user_id = query_params["user_id"]
    except KeyError:
        logger.info("System call")
    except Exception as e:
        logger.error(f"Error connecting to server: {e}", exc_info=True)

    if user_id:
        store_sid(user_id, sid)


@sio.event
async def disconnect(sid):
    logger.debug(f"Disconnected; sid == {sid}")
    remove_sid(sid)


@sio.event
async def django_message(sid, data):
    logger.debug("django_message triggered...")
    parsed_data = data
    try:
        parsed_data = json.loads(data)
    except:
        pass

    user_id = parsed_data.get("user_id", None)
    message = parsed_data.get("message", None)
    user_sid = get_sid(user_id).decode("utf8")
    if user_sid:
        await sio.emit("message_from_django", message, room=user_sid)


@sio.event
async def my_event(sid, data):
    logger.debug("my_event triggered")
    logger.debug(f"sid == {sid}")
    logger.debug(json.dumps(data, indent=4, default=str))
    await sio.emit("my_event", data)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8765)
