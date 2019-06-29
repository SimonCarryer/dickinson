with open('deep_dickinson.txt', 'r') as f:
    texts = f.read().split('<|endoftext|>')

print(len(texts))