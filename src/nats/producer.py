import asyncio

import nats


async def main():

    nc = await nats.connect("nats://localhost:4222")
    js = nc.jetstream()
    await js.publish("bar", b'Hello World!', stream="foo")
    while True:
        await asyncio.sleep(4)
        print("Sleeping...")
        await js.publish("bar", b'Hello World!', stream="foo")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
