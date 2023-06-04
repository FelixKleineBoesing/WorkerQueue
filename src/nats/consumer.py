
import asyncio
import json

import nats
from nats.errors import TimeoutError


async def main():

    nc = await nats.connect("nats://localhost:4222")
    js = nc.jetstream()
    await js.add_stream(name="foo", subjects=["bar"])
    sub = await js.pull_subscribe("bar", durable="bar1", stream="foo")
    while True:
        try:
            msg = await sub.fetch(1, timeout=2)
        except TimeoutError:
            msg = None
            await asyncio.sleep(1)
            print("Sleeping...")
        if msg is not None:
            await msg[0].ack()
            print(str(msg[0].data))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
