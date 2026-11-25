class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;

        int count[26] = {0};    // 26 letters
        
        for (size_t i = 0; i < s.size(); i++){
            count[s[i] - 'a']++;    // at letter index how much frequency of one
            count[t[i] - 'a']--;    // how much frequency for other string (reverse)
        }

        for (int c: count){
            if (c != 0) return false;   // all should cancel out
        }
        return true;
    }
};
