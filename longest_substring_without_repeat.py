sentence = "abcabcdbb"
hash_map = {}
right = 0
substring = ""
max_length = 0
while right < len(sentence):
    if sentence[right] in hash_map:
        substring = sentence[right]
        right += 1
        hash_map = {}
        max_length = max(max_length, len(substring))
    else:
        substring += sentence[right]
        right += 1
        max_length = max(max_length, len(substring))
    hash_map[sentence[right - 1]] = right - 1 
print(max_length)



