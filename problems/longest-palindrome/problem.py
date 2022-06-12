

class NaiveApproach:

    def longestPalindrome(self, s: str) -> str:
        longest = s[0]
        for i in range(len(s)):
            max_length = len(longest)
            if max_length >= len(s) - i:
                return longest
            for j in range(i+max_length+1, len(s)+1):
                current = s[i:j]
                if self.isPalindrome(current) and len(current) > len(longest):
                    longest = current
        return longest

    def isPalindrome(self, s):
        result = True
        for i in range(len(s)//2):
            print(f'{s[i]} == {s[-i-1]}')
            if s[i] != s[-i-1]:
                result = False
        return result

class LongestCommonSubstring:

    def __init__(self):
        pass

    def longestPalindrome(s: str) -> str:
        r = s[::-1]
        longest = s[0]
        for i in range(len(s)):
            # for j in range(i+1, len(s)+2):
            # for j in range(len(s)+2, i+1, -1):
            for j in range(len(s)+2, i+len(longest), -1):
                if len(s[i:j]) > len(longest):
                    if (i > 0 and r[-j:-i] == s[i:j]) or (i == 0 and r[-j:] == s[:j]):
                        longest = s[i:j]
        return longest




# if __name__ == '__main__':
#     s = '1221'
#     print(f'{s} is a palindrome:  {isPalindrome(s)}')

#     s = '1223'
#     print(f'{s} is a palindrome:  {isPalindrome(s)}')
