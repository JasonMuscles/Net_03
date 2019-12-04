import urllib.request
import ssl


def main():
    context = ssl._create_unverified_context()
    req = urllib.request.urlopen("https://huyaimg.msstatic.com/cdnimage/game/5485-MS.jpg", context=context)
    img_content = req.read()
    with open("2.jpg", "wb") as f:
        f.write(img_content)


if __name__ == '__main__':
    main()



