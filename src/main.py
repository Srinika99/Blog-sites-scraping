from data_loaders.websites import load_urls


def main():
    urls = load_urls()
    print(f'got {len(urls)} urls')


if __name__ == '__main__':
    main()
