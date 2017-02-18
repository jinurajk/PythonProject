from collections import deque


def palindrome(word):
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            print ("Pop Left and Pop", dq.popleft(), dq.pop())
            return False
    return True


def another_palindrome(word):
    return word == word[::-1]


print(palindrome("malayalam"))
print(palindrome("malaym"))
print(palindrome("leftn"))
print(another_palindrome("malayalam"))
print(another_palindrome("mlayalam"))
print(another_palindrome("abcddcba"))
