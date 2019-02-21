def is_pal(word):
   # reverse_string = word[::-1]
    if word == word[::-1]:
        return False
    else:
        return True
print(is_pal('naman'))
print(is_pal('tot'))





