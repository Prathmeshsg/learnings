def calculate_love_score(name1, name2):
  # your code here
  # Convert names to lowercase
    combined_names = (name1 + name2).lower()
    
    # Count occurrences of TRUE letters
    true_count = sum(combined_names.count(letter) for letter in "true")
    
    # Count occurrences of LOVE letters
    love_count = sum(combined_names.count(letter) for letter in "love")
    
    # Combine to form love score
    love_score = int(str(true_count) + str(love_count))
    
    # print(f"T occurs {combined_names.count('t')} times")
    # print(f"R occurs {combined_names.count('r')} times")
    # print(f"U occurs {combined_names.count('u')} times")
    # print(f"E occurs {combined_names.count('e')} times")
    # print(f"Total = {true_count}")
    
    # print(f"L occurs {combined_names.count('l')} times")
    # print(f"O occurs {combined_names.count('o')} times")
    # print(f"V occurs {combined_names.count('v')} times")
    # print(f"E occurs {combined_names.count('e')} times")
    # print(f"Total = {love_count}")
    
    # print(f"Love Score = {love_score}")
    print(love_score)
    
    return love_score
 
# Call your function with hard coded values
calculate_love_score("Kanye West", "Kim Kardashian")