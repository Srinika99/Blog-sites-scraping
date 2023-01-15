from data_loaders.interests import load_interests
from data_loaders.websites import load_urls


def main():
    urls = load_urls()
    print(f'got {len(urls)} urls')

    interests = load_interests()
    print(f'got {len(interests)} interests')


if __name__ == '__main__':
    main()
