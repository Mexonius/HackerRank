int diagonalDifference(vector<vector<int>> arr) {
    int d1=0, d2=0;
    for(int i=0; i<arr.size(); i++) d1+=arr[i][i];
    for(int i=arr.size()-1; i>=0; i--) d2+=arr[i][arr.size()-i-1];
    return abs(d1-d2);
}
