class Solution {
public:
vector<int> numMovesStonesII(vector<int>& A) {
    sort(A.begin(), A.end());       // Step 1: sort positions
    int i = 0, n = A.size(), low = n;

    // Step 2: compute maximum moves
    int high = max(A[n - 1] - n + 2 - A[1], 
                   A[n - 2] - A[0] - n + 2);

    // Step 3: compute minimum moves (sliding window)
    for (int j = 0; j < n; ++j) {
        // keep window length < n
        while (A[j] - A[i] >= n) ++i;

        // special tricky case:
        // n-1 stones in a block of length n-1 → needs 2 moves
        if (j - i + 1 == n - 1 && A[j] - A[i] == n - 2)
            low = min(low, 2);
        else
            // otherwise, we need to move stones outside into the window
            low = min(low, n - (j - i + 1));
    }

    return {low, high};
}
};