class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::set<int> noDupe(nums.begin(), nums.end());
        return nums.size() != noDupe.size();
    }
};