# codeChallenges
## 1. Array Challenge
Have the function ArrayChallenge(strArr) read the array of strings stored in strArr, which will contain 2 elements: the first element will be a sequence of characters, and the second element will be a long string of comma-separated words, in alphabetical order, that represents a dictionary of some arbitrary length. For example: strArr can be: ["hellocat", "apple,bat,cat,goodbye,hello,yellow,why"]. Your goal is to determine if the first element in the input can be split into two words, where both words exist in the dictionary that is provided in the second input. In this example, the first element can be split into two words: hello and cat because both of those words are in the dictionary.

Your program should return the two words that exist in the dictionary separated by a comma. So for the example above, your program should return hello,cat. There will only be one correct way to split the first element of characters into two words. If there is no way to split string into two words that exist in the dictionary, return the string not possible. The first element itself will never exist in the dictionary as a real word.
Once your function is working, take the final output string and concatenate it with your ChallengeToken, and then replace every third character with an X.

Your ChallengeToken: 48lhv97c5d
Examples
Input: ["baseball", "a,all,b,ball,bas,base,cat,code,d,e,quit,z"]
Output: base,ball
Final Output: baXe,XalX48XhvX7cXd
Input: ["abcgefd", "a,ab,abc,abcg,b,c,dog,e,efd,zzzz"]
Output: abcg,efd
Final Output: abXg,XfdX8lXv9Xc5X
Browse Resources
Search for any help or documentation you might need for this problem. For example: array indexing, Ruby hash tables, etc.


## 2. String Challenge
Have the function StringChallenge(strArr) take the array of strings stored in strArr, which will contain only two strings, the first parameter being the string N and the second parameter being a string K of some characters, and your goal is to determine the smallest substring of N that contains all the characters in K. For example: if strArr is ["aaabaaddae", "aed"] then the smallest substring of N that contains the characters a, e, and d is "dae" located at the end of the string. So for this example your program should return the string dae.

Another example: if strArr is ["aabdccdbcacd", "aad"] then the smallest substring of N that contains all of the characters in K is "aabd" which is located at the beginning of the string. Both parameters will be strings ranging in length from 1 to 50 characters and all of K's characters will exist somewhere in the string N. Both strings will only contains lowercase alphabetic characters.
Once your function is working, take the final output string and concatenate it with your ChallengeToken, and then replace every third character with an X.

Your ChallengeToken: 48lhv97c5d
Examples
Input: ["ahffaksfajeeubsne", "jefaa"]
Output: aksfaje
Final Output: akXfaXe4XlhX97X5d
Input: ["aaffhkksemckelloe", "fhea"]
Output: affhkkse
Final Output: afXhkXseX8lXv9Xc5X
Browse Resources
Search for any help or documentation you might need for this problem. For example: array indexing, Ruby hash tables, etc.


## 3. You are shopping on Amazon.com for some bags of rice. Each listing displays the number of grains of rice that the bag contains. You want to buy a perfect set of rice bags from the entire search results list, riceBags. A perfect set of rice bags, perfect, is defined as:

• The set contains at least two bags of rice.

• When the rice bags in the set perfect are sorted in increasing order by grain count, it satisfies the condition perfect[] perfect[i]= perfect[i+1] for all 1 si<n. Here n is the size of the set and perfect[i] is the number of rice grains in bag /

Find the largest possible set perfect and return an integer, the size of that set. If no such set is possible, then return -1. It is guaranteed that all elements in riceBags are distinct.

Example

Let the bags of rice available on Amazon have grain counts [3, 9, 4, 2, 16]. The following are the perfect sets.

• Set perfect = [3, 9]. The size of this set is 2.

• Set perfect=[4,2]. The size of this set is 2. ⚫ Set perfect = [4, 16]. The size of this set is 2.

• Set perfect = [4, 2, 16]. The size of this set is 3.

The size of the largest set is 3. The image below illustrates the correct ordering of the purchased rice bags by grains of rice.

Function Description

Complete the function maxSetSize in the editor below.

maxSetSize has the following parameter: int riceBags[n]: the list of bags of rice by rice grain count

Returns

int: the size of the largest set possible or -1 if

there is none

Constraints

• 1≤n≤2-105

• 2≤ riceBags[i]≤106


## 4. Amzon Fresh is a new grocery store designed from the ground up to offer a seamless grocery shopping experience to consumers. As part of a stock clearance exercise at the store, given many piles of fresh products, follow the rules given below to stack the products in an orderly manner.

• There are a total of n piles of products.
• The number of products in each pile is represented by the array numProcuts.
• Select any sbuarray from such that the number of products you pick from ith pile is strictly less than the number of products you pick from the (i+1)th pile for all indices i of the subarray.

Find the maxium number of products that can be picked.

Example
The numbers of products in each pile are numProducts = [7,4,5,2,6,5].