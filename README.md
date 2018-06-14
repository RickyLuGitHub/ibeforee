Reddit Daily Programmer Challenge 2018-06-11
(source: https://www.reddit.com/r/dailyprogrammer/comments/8q96da/20180611_challenge_363_easy_i_before_e_except/)

My attempt at coding the English i-before-e-except-after-c rule using Python 3. Also attempt the optional Bonus 1

**How to use:**
in terminal, run "python ibeforee.py" and follow on screen prompts
To run the challenge on a list of words and see how many words meet the rule, download "list.txt" and place in the same directory (or use your own list, name the list of words as list.txt) and upon the prompt, type in "check list" instead of a word.

Challenge Prompt (taken from Reddit):
>"I before E except after C" is perhaps the most famous English spelling rule. For the purpose of this challenge, the rule says:

>if "ei" appears in a word, it must immediately follow "c".

>If "ie" appears in a word, it must not immediately follow "c".

>A word also follows the rule if neither "ei" nor "ie" appears anywhere in the word. Examples of words that follow this rule are:

>fiery hierarchy hieroglyphic
>ceiling inconceivable receipt
>daily programmer one two three
>There are many exceptions that don't follow this rule, such as:

>sleigh stein fahrenheit
>deifies either nuclei reimburse
>ancient juicier societies
>Challenge
>Write a function that tells you whether or not a given word follows the "I before E except after C" rule.

>check("a") => true
>check("zombie") => true
>check("transceiver") => true
>check("veil") => false
>check("icier") => false
>Optional Bonus 1
>How many words in the enable1 word list are exceptions to the rule? (The answer is 4 digits long and the digits add up to 18.)
