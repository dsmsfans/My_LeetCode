class Solution {
public:
    string convert(string s, int numRows) {
        if(s.size() == 0 || numRows < 1)
        {
            return "";
        }
        if(numRows == 1)
        {
            return s;
        }
        string output = "";
        int size = 2 * numRows - 2;
        for(int i = 0; i< numRows; i++)
        {
            for(int j = i; j < s.size(); j += size)
            {
                output += s[j];
                if(i != 0 && i != numRows - 1)
                {
                    int temp  = j + size - 2 * i;
                    if(temp < s.size())
                    {
                        output += s[temp];
                    }
                    
                }
            }
        }
        return output;
    }
};