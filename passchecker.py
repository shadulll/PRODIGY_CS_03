import re

# Define the banner with ANSI escape codes for red color
banner = """
\033[91m
 _______  _______  _______  _______    _______           _______  _______  _        _______  _______ 
(  ____ )(  ___  )(  ____ \(  ____ \  (  ____ \|\     /|(  ____ \(  ____ \| \    /\(  ____ \(  ____ )
| (    )|| (   ) || (    \/| (    \/  | (    \/| )   ( || (    \/| (    \/|  \  / /| (    \/| (    )|
| (____)|| (___) || (_____ | (_____   | |      | (___) || (__    | |      |  (_/ / | (__    | (____)|
|  _____)|  ___  |(_____  )(_____  )  | |      |  ___  ||  __)   | |      |   _ (  |  __)   |     __)
| (      | (   ) |      ) |      ) |  | |      | (   ) || (      | |      |  ( \ \ | (      | (\ (   
| )      | )   ( |/\____) |/\____) |  | (____/\| )   ( || (____/\| (____/\|  /  \ \| (____/\| ) \ \__
|/       |/     \|\_______)\_______)  (_______/|/     \|(_______/(_______/|_/    \/(_______/|/   \__/
                                                                                                     
\033[0m
Created by Muhammed Shadul
"""

def password_complexity_checker(password):
    length_criteria = len(password) >= 8
    upper_criteria = re.search(r'[A-Z]', password) is not None
    lower_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'[0-9]', password) is not None
    special_criteria = re.search(r'[\W_]', password) is not None

    # Assign points for each criterion met
    score = sum([length_criteria, upper_criteria, lower_criteria, digit_criteria, special_criteria])
    
    # Determine strength
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    # Provide detailed feedback
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not upper_criteria:
        feedback.append("Include at least one uppercase letter.")
    if not lower_criteria:
        feedback.append("Include at least one lowercase letter.")
    if not digit_criteria:
        feedback.append("Include at least one digit.")
    if not special_criteria:
        feedback.append("Include at least one special character.")

    return {
        "strength": strength,
        "feedback": feedback
    }

# Display the banner
print(banner)

# Prompt for password input in default color
password = input("Please enter your password: ")

# Call the function with the password
result = password_complexity_checker(password)

# Print the results
print(f"\nPassword Strength: {result['strength']}")
if result['feedback']:
    print("Feedback:")
    for comment in result['feedback']:
        print(f"- {comment}")
