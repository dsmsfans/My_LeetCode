/**
 * @param {string[]} word1
 * @param {string[]} word2
 * @return {boolean}
 */
var arrayStringsAreEqual = function(word1, word2) {
    return toString(word1) === toString(word2)
};

function toString(value){
    var output = ""
    for(i in value){
        output = output + value[i]
    }
    return output
}