
def breakout_room(code, message):
    count = 0
    flag = True
    inf_check = 0
    substring = message
    last_letter = code[len(code)-1]
    
    while flag == True and inf_check < 100:
        for letter in code:
            if not letter in code: # When we no longer find code in the substring then end loop
                flag = False
                exit
            
            new_substring_position = substring.find(letter) # Find next letter from code in substring
            substring = substring[new_substring_position+1:]
            
            if letter == last_letter: # When we have found the last letter then entire code has been found so add count
                count += 1
                        
        inf_check += 1 # Infinite loop stop

    return count

# code1 = "ASDF"
# message1 = "SODIFJOSDIFJASOIDF ASLWEARWOERIMSOEID ENRMFASD"
#                              1
# message1 = "SODIFJOSDIFJASOIDFASLWEARWOERIMSOEIDENRMFASD"


result = breakout_room("ASDF", "SODIFJOSDIFJASOIDFASLWEARWOERIMSOEIDENRMFASD")
print(result)