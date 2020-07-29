class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # UNDERSTAND
        # We are given an array of strings.
        # We need to group anagrams together - words containing
        # the same letters

        # PLAN
        # Create a hashtable to keep track of words and the letters
        # that each word has.

        # The value in our hashtable will be a list of the word's letters
        # sorted alphabetically.

        # Iterate through our hashtable and create a final output list
        # of lists, grouping any words that have the same alphabetically
        # sorted list

        # EXECUTE
        letter_table = {}  # init a hashtable

        # iterate through our input list and sort the strs alphabetically
        sorted_strs = [''.join(sorted(word)) for word in strs]

        # iterate through our list of sorted strings
        for s in range(len(sorted_strs)):
            # if the sorted string is not in our hashtable, add it
            # initialize the value as a new list with the unsorted string
            # in the same position
            if sorted_strs[s] not in letter_table:
                letter_table[sorted_strs[s]] = [strs[s]]
            # if sorted string exists in our hashtable, append the unsorted
            # string to the current list
            else:
                letter_table[sorted_strs[s]].append(strs[s])

        # return the values of our hashtable for our final output
        return letter_table.values()
