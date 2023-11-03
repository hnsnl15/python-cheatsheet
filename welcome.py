import asyncio

def greet(name: str) -> str:
    """
    Prints a welcome message with the name surrounded by asterisks.

    Args:
        name (str): The name of the person to greet.

    Returns:
        None: The function does not return any value. It only prints the welcome message.
    """
    line01 = "********************"
    line02 = "*                  *"
    line03 = f"*  WELCOME {name}! *"

    return "\n".join([line01, line02, line03, line02, line01])

def isHandsome(name):
    return name.lower() == "henson"

# type checking in python
async def main(message: str = "") -> None:
    """
    An asynchronous function that waits for 3 seconds and prints a message based on the input.

    Args:
        message (str, optional): The message to be printed. Defaults to "".

    Returns:
        None: The function does not return any value.
    """
    await asyncio.sleep(3)
    print("Hello world!" if message.lower() == "hi" else "sup?!")
    
def add(a: int, b: int) -> int:
    return a + b

print(add(4, 4))

# input in python
name = input("Please enter your name: ")
print(greet(name))
print(f"{isHandsome(name)}, {name} is handsome...")

# asynchronous in python
asyncio.run(main())