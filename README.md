# Compare-Last-Three-Characters

Question Explanation:

This program checks whether the last three characters of two given strings are the same.

Logical Approach:

Read Input:
Read two strings from input.

Find the Length of Each String:
Determine the length of the first string (len_a) and the second string (len_b).

Extract the Last Three Characters:
For the first string, extract the last three characters by slicing it from len_a - 3 to the end.
For the second string, perform a similar slicing from len_b - 3 to the end.

Comparison:
Compare the last three characters of the first string with the last three characters of the second string.

Output:
If the last three characters match, print True.
If they do not match, print False.

Example for Clarity:

Consider the strings apple and pimple as inputs.
The last three characters of apple are ple.
The last three characters of pimple are also ple.
Since both these substrings are the same, the output is True.

The output will be:

True
