def count_vowels(phrase):
 
    vowels = 'aeiouAEIOU'
    count = sum(1 for char in phrase if char in vowels)
    return count
print(count_vowels("phrase"))