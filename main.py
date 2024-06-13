##Given an array of integers nums and an integer target, return
# indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.

#You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# {2: 0}
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]


def twoSum(nums, target_num):
    hash = {}
    for i in range(len(nums)):
        value = hash.get(target_num-nums[i])
        if value != None:
            return [i, value]
        else:
            hash[nums[i]] = i

# print(twoSum([1, 2, 3, 5], 7))

def twoSum2(nums, target_num):
    hash = {}
    for i, n in enumerate(nums):
        diff = target_num - n
        if diff in hash:
            return [hash[diff], i]
        else:
            hash[diff] = i



# You are given an array prices where prices[i] is the price of
# a given stock on the ith day.
# You want to maximize your profit by choosing a single day to
# buy one stock and choosing a different day in the future to sell that stock.
#Return the maximum profit you can achieve from this transaction.
# If you cannot achieve any profit, return 0.

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

# input: list of nums
# output: num => max profit
# want to buy low and sell high - make the most profit
#   [7, 1, 5, 3, 6, 4] =>  5 < 6
#       b           s
# max_profit = 5
# buy:  1 ele 1
# sell: 5 ele 4
#

def maxProfit(prices):
    buy = 1
    sell = 1
    max_profit = 0
    while sell < len(prices):
        if prices[buy] < prices[sell]:
            diff = prices[sell] - prices[buy]
            if diff > max_profit:
                max_profit = diff
        else:
            buy = sell
        sell += 1

    return max_profit


# Given a string s containing just the characters
# '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Example 1:
    # Input: s = "()"
    # Output: true

# Example 2:
    # Input: s = "()[]{}"
    # Output: true

# Example 3:
    # Input: s = "(]"
    # Output: false
# Example 4:
    # Input: s = '(())((()())())'
    # Output: true
# stack = [(]
# hash {'(': ')', '{': '}', '[': ']'}
#iterate through the string "()[]{}"
#                             i
# if the next char is not the value of the key in hash return false

def validParens(str):
    hashMap = {"(": ")", "[": "]", "{": "}"}
    stack = []
    for bracket in str:
        if bracket in hashMap:
            stack.append(bracket)
        else:
            if not stack or hashMap[stack.pop()] != bracket:
                return False
    return True



# print(validParens("()[]{}"))

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing
#  together the nodes of the first two lists.

# Return the head of the merged linked list.

# Example 1
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:
# Input: list1 = [], list2 = []
# Output: []

# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]


# A phrase is a palindrome if, after converting all uppercase letters into
# lowercase letters and removing all non-alphanumeric characters, it reads
# the same forward and backward. Alphanumeric characters include letters
# and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

# input string
# output boolean
# convert str to lowercase and get rid of all alphanumeric chars
# reverse method
# iterate backwards and put all eles in a new str
# compare input string with new str
# s = "A man, a plan, a canal: Panama"
# "amanaplanacanalpanama"
import re

def isPalindrome1(s):
    if len(s) <= 1:
        return True

    pattern = r'[^a-zA-Z0-9]'
    cleaned_str = re.sub(pattern, '', s).lower()

    return cleaned_str == cleaned_str[::-1]

def isPalindrome2(s):
    if len(s) <= 1:
        return True

    cleaned = ''.join(e for e in s if e.isalnum()).lower()
    return cleaned == cleaned[::-1]

## tACo Cam!
#     33
# start: 0
# end: 8


def isPalindrome(s):
    start = 0
    end = len(s)-1
    while start < end:
        if not s[start].isalnum():
            start += 1
        elif not s[end].isalnum():
            end -= 1
        elif s[start].lower() == s[end].lower():
            start += 1
            end -= 1
        else:
            return False
    return True




# print(isPalindrome("A man, a plan, a canal: Panama"))

# Given an array of integers nums which is sorted in ascending order,
# and an integer target, write a function to search target in nums.
# If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1

#input lst of nums and a target num
#ouput num either idx of target num in lst or -1(not found)
# [-1,0,3,5,9,12] target 9
#       m l m   h
# low = 3
# high = 5
#

def search(nums, target):
    low = 0
    high = len(nums)-1

    while low <= high:
        mid = (low + high) // 2

        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            low = mid + 1
        else:
            high = mid -1

    return -1

# print(search([-1,0,3,5,9,12], 9))



# Given two strings s and t, return true if t is an anagram of s, and
# false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly once.

# Example 1:
# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

#Input: strs s & t
#OUtput: boolean
# is s an anagram of t (has the same letters and same frequency of letters)
# case sensitive
# create a hash of s and t
# iterate through s
    #if a key does not match
    # false
    # if the value does not match
    #false
#true
# s: {a: 3, n: 1, g: 1, r: 1, m: 1 }
# t: {a: 3, n: 1, g: 1, r: 1, m: 1 }

def validAnagram1(s, t):
    if len(s) != len(t):
        return False

    hash_s = makeHash(s.lower())
    hash_t = makeHash(t.lower())

    for key in hash_s:
        if key not in hash_t.keys():
            return False
        elif hash_s[key] != hash_t[key]:
            return False

    return True



def makeHash(s):
    hash = {}
    for ele in s:
        if ele in hash:
            hash[ele] += 1
        else:
            hash[ele] = 1
    return hash

def isAnagram(s, t):
    if len(s) != len(t):
        return False

    hash_s = {}
    hash_t = {}

    for ele in s:
        hash_s[ele] = hash_s.get(ele, 0) + 1

    for ele in t:
        hash_t[ele] = hash_t.get(ele, 0) + 1

    for key in hash_s:
        if key not in hash_t.keys():
            return False
        elif hash_s[key] != hash_t[key]:
            return False
    return True

print(isAnagram("rat", "car"))

