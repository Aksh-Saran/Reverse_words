#include <string>
#include <cassert>

std::string reverse_words(const std::string &str) {
    std::string result;
    std::string word;
    
    // Iterate through each character in a string
    for (char ch : str)
    {
        if (isalnum(ch)) 
        {
            // If the character is an alphanumeric then add it to the current word
            word += ch;
        } 
        else 
        {
            // Else if the character is not an alphanumeric then reverse the current word
            if (!word.empty()) // This checks if the word is not empty
            {
                std::string reversedWord = word;
                int i = 0, j = word.length() - 1;
                while (i < j) 
                {
                    std::swap(reversedWord[i++], reversedWord[j--]); // Swap is used to exchange the values between i & j
                }
                result += reversedWord;
                word.clear();
            }
            // Appends the non-alphanumeric character to the result
            result += ch;
        }
    }

    // To reverse the last word if it exists
    if (!word.empty()) 
    {
        std::string reversedWord = word;
        int i = 0, j = word.length() - 1;
        while (i < j) 
        {
            std::swap(reversedWord[i++], reversedWord[j--]);
        }
        result += reversedWord;
    }

    return result;
}

int main() 
{
    std::string test_str = "String; 2be reversed..."; // Here, test_str is a variable assigned to a string
    assert(reverse_words(test_str) == "gnirtS; eb2 desrever..."); // This calls reverse_words function and compares if the string is reversed
    return 0; //If the assertion passes, then 0 is returned and it indicates that test is passed successfuly
}

