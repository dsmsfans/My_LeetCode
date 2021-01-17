/**
 * @param {number} n
 * @return {number}
 */
var numberOfMatches = function(n) {
    var total = n
    var output = 0
    while(n !== 1){
        output = output + parseInt(n / 2)
        n = n - parseInt(n / 2)
    }
    return output
};