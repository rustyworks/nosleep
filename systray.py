import pystray
from pystray import Menu as menu, MenuItem as item
# import threading

# from PIL import Image, ImageDraw
from PIL import Image


state = False


def create_image(width, height, color1, color2):
    # image = Image.new("RGB", (width, height), color1)
    # dc = ImageDraw.Draw(image)
    # dc.rectangle(
    #     (width // 2, 0, width, height // 2), fill=color2
    # )
    # dc.rectangle(
    #     (0, height // 2, width // 2, height), fill=color2
    # )
    try:
        image = Image.open("./red-eye.png")
    except Exception:
        image = Image.open("./nosleep/red-eye.png")

    return image


def on_clicked(icon, item):
    global state
    state = not item.checked


def systray_icon():
    icon = pystray.Icon(
        "nosleep",
        icon=create_image(64, 64, "magenta", "orange"),
        menu=menu(
            item(
                'Checkable',
                on_clicked,
                checked=lambda item: state
            )
        )
    )

    # threading.Thread(target=icon.run).start()
    # icon.run()
    return icon
