# udemy ep10


def custom_fence(fence: str = "+"):
    def fence_decorator(func):
        def wrapper(text: str):
            print(fence * len(text))
            func(text)
            print(fence * len(text))

        return wrapper

    return fence_decorator


@custom_fence("ㅗ")
def log(text: str):
    print(text)


log("fuck")
