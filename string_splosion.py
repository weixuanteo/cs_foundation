# Given a non-empty string like "Code" return a string like "CCoCodCode".

# Sample input
s = "Code"

def string_splosion(str):
    result = ""
    # On each iteration, add the substring of the chars
    for i in range(len(str)):
        print("str[:i+1]: ", str[:i+1])
        # [Python slicing] Returns from begining of the string to pos i+1 and concatenate to result.
        result = result + str[:i+1]
    return result

# Main
result = string_splosion(s)
print(result)