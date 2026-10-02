if __name__ == '__main__': 
    with open('./tinyshevchenko.txt', 'r') as f: 
        content = f.read() 

    print(f'chars count: {len(content)}')
    print(f'char: {''.join(sorted(set(content)))}')