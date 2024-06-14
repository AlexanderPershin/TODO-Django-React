import socketio
import logging
import json

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

sio = socketio.AsyncServer(async_mode="asgi")
app = socketio.ASGIApp(sio)


@sio.event
async def connect(sid, environ):
    user_id = environ.headers["user_id"]
    logger.debug(f"Connected; sid == {sid}")
    # logger.debug(f"environ == {environ}")
    logger.debug(f"user_id == {user_id}")


@sio.event
async def disconnect(sid):
    logger.debug(f"Disconnected; sid == {sid}")


@sio.event
async def message(sid, data):
    logger.debug("my_event triggered")
    logger.debug(f"sid == {sid}")
    logger.debug(json.dumps(data, indent=4, default=str))
    await sio.emit("response", data)


@sio.event
async def my_event(sid, data):
    logger.debug("my_event triggered")
    logger.debug(f"sid == {sid}")
    logger.debug(json.dumps(data, indent=4, default=str))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8765)
