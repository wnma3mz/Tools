import qrcode
import qrcode.image.svg
from PIL import Image


def make_qr(string, logo=None):
    # 配置文件
    qr = qrcode.QRCode(
        version = 4,
        error_correction = qrcode.constants.ERROR_CORRECT_Q,
        box_size = 8,
        border = 2
    )
    # 添加字符
    qr.add_data(string)
    qr.make(fit=True)
    img = qr.make_image()
    img = img.convert("RGBA")
    # 制作icon
    icon = Image.open(logo)
    img_w, img_h = img.size
    factor = 4
    size_w = int(img_w / factor)
    size_h = int(img_h / factor)
    icon_w, icon_h = icon.size
    if icon_w > size_w:
        icon_w = size_w
    if icon_h > size_h:
        icon_h = size_h
    icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)
    w = int((img_w - icon_w) / 2)
    h = int((img_h - icon_h) / 2)
    icon = icon.convert("RGBA")
    img.paste(icon, (w, h), icon)
    # 保存二维码
    img.save("qrcode.png")


if __name__ == "__main__":
    logo = input("Please input logo path")
    string = input("Please input string")
    make_qr(string, logo)
