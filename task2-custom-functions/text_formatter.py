def format_text(word:str, prefix:str="", suffix:str="", capitalise:bool=False, max_length:int=None) -> str:
    """
    This function will format the text by adding prefix and suffix to the word
    Parameters:
    word:str 
      word to be formatted with string datatype

    prefix:str, optional
      text to be added at the beginning  with string datatype(default is empty string)
    suffix:str,optional
      text to be added at the end with string datatype(default is empty string)
    capitalise:bool, optional
      if True, capitalise the first letter of the word with boolean datatype(default is False)
    max_length:int, optional
      if provided, the word will be truncated to this length with int datatype(default is None)
      

    Example:
    format_text("I", prefix="_like", suffix= "_python", capitalise=True) returns "I_Like_Python"
    format_text("I", prefix="_like", suffix= "_python", capitalise=True, max_length=5) returns "I_Li"

    """
    result = prefix + word + suffix
    if capitalise == True:
        result = result.capitalize()
    if max_length != None:
        result = result[:max_length]
        
    return result
def main():
    try:
        word = input("Enter the word to be formatted: ")
        prefix = input("Enter the prefix to be added: ")
        suffix = input("Enter the suffix to be added: ")
        capital = input("Do you want to capitalise the first letter of the word? (True/False): ").lower()
        if capital == "True":
            capital = True
        else:
            capital = False
        max_length = input("Enter the maximum length of the word (or press Enter to skip): ")
        if max_length == "":
            max_length = None
        else:
            max_length = int(max_length)

        formatted_word = format_text(word, prefix, suffix, capital, max_length)
        print("Formatted word is: ", formatted_word)
    except ValueError:
        print("ValueError: Parameters are in incorrect format. Please provide valid inputs.")
    
main()