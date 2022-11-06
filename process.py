from PIL import Image


def paste_frame():
    img_path = "images/cat.png"
    frame_path = "images/frame.png"
    output_path = "images/out.png"

    img = Image.open(img_path)
    frame = Image.open(frame_path)

    resized_frame = frame.resize((img.width, img.height))
    img.paste(resized_frame, (0, 0), resized_frame)

    img.save(output_path)
    img.show()


def main():
    paste_frame()


if __name__ == "__main__":
    main()
