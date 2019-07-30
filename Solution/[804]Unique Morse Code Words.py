class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        letters = []
        output = []
        temp = ""
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for word in words:
            for letter in word:
                temp = temp + morse[ord(letter.lower())-97]
            letters.append(temp)
            temp = ""
        for m in letters:
            if m not in output:
                output.append(m)
        
        return(len(output))
        
                
            
                
                
        
        