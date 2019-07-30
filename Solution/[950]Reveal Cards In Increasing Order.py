class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        if not deck:
            return None
        deck.sort(reverse = True)
        new_deck = list()
        for i in deck:
            if len(new_deck) > 1:
                new_deck = [new_deck[-1]] + new_deck[:-1]
            new_deck.insert(0,i)
        return new_deck
        