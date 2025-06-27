//taken from gfg practise - Find the highest number
// array is first increasing and decreasing. Find the highest number.

#include<bits/stdc++.h>
using namespace std;

int a[210];
int n;

int fun(int l,int r){
    if(l==r) return a[l];
    if(l==r-1) return max(a[l],a[r]);
    int mid = (l+r)/2;
    if((mid!=r && a[mid]<=a[mid+1]))
        return fun(mid,r);
    if((mid!=l && a[mid]<=a[mid-1]))
        return fun(l,mid);
    if(a[mid]>a[l] && a[mid]>a[r])
        return a[mid];
}

int main()
{
    int t;
    cin>>t;
    while(t--){
        cin>>n;
        for(int i=0;i<n;i++) cin>>a[i];
        cout<<fun(0,n-1)<<endl;
    }
    return 0;
}
