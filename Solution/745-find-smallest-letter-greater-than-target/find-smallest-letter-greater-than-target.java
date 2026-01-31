class Solution {
    public char nextGreatestLetter(char[] l, char target) {
        int s = 0;
        int e = l.length - 1;

        while(s<=e){
            int mid = s + (e-s)/2;
            if (l[mid]>target){
                e = mid - 1;
            }else{
                s=mid+1;
            }
        }
        return l[s%l.length];
    }
}