class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # 1. Create an empty dictionary to store our groups
        groups = {}

        for word in strs: 
            # 2. Sort the letters to create a unique "key" 
            # "eat" -> ["a", "e", "t"] -> "aet"
            key = "".join(sorted(word)) 
            
            # 3. Check if we've seen this set of letters before
            if key in groups:
                # If yes, add the word to that group's list
                groups[key].append(word) 
            else:
                # If no, create a new list with this word
                groups[key] = [word] 
                
        # 4. Return just the lists of words from the dictionary
        return list(groups.values())