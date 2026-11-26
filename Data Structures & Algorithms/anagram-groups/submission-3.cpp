class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> groups;
        for (const string& word: strs){ // & makes it so you reference the string using word instead of copying it into word
            int count[26] = {0};
            for (char c: word) count[c - 'a']++;

            string key;
            for (int c: count) key += to_string(c) + "#";   // # serves to separate each character frequency ex. cab -> 1#1#1#0#0...w

            groups[key].push_back(word);    // appends word to key
        }
        vector<vector<string>> result;
        for (auto& [key, wordList]: groups) result.push_back(wordList); 
        return result;
    }
};
