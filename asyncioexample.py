import asyncio


loop = asyncio.get_event_loop()

def long_running_task():

    arguments = [1,2,3,4,5,6,7,8]
    loop.run_in_executor(None, square_function, arguments)


def square_function(args):
    print(args)


if __name__ == '__main__':
    long_running_task()
