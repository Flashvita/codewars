
"""Task by solution factories
resolve sentence wit max word count
"""  

def resolve_max_words(arr: list) -> int:
    return len(sorted(arr)[-1].split())
        
arr = ["Hello world", 'simple word in sentence', "How old are your?", "How are you"]
print(resolve_max_words(arr))

