def generate_acronym(s):
    
    words = s.split()
    acronym = ''.join(word[0].upper() for word in words)
    return acronym
print(generate_acronym("National Union of Teachers"))