class Solution {
public:
    bool check(string str) {
        map<char,int> mp; 
        for(auto x: str) {
            mp[x]++;
        }
        if(mp.find('a')==mp.end()) return false;
        if(mp.find('e')==mp.end()) return false;
        if(mp.find('i')==mp.end()) return false;
        if(mp.find('o')==mp.end()) return false;
        if(mp.find('u')==mp.end()) return false;
        if(mp.size()>5) {return false;}
        return true;
    }
    int countVowelSubstrings(string word) {
        int ans=0; 
        for(int i=0; i<word.size(); i++) {
            string str = "";
            str+=word[i];
            for(int j=i+1; j<word.size(); j++) {
                str+=word[j];
                if(check(str)) {
                    ans++;
                }
            }
        }
        return ans;
    }
};
