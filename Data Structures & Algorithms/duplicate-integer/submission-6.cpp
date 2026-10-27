class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> s;
        for (int i : nums) {
            if (s.find(i)) {
                return true;
            }
            else {
                s.add(i);
            }
        }
        return false;
        
    }
};