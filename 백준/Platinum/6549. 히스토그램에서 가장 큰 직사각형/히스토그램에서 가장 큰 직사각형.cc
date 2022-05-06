#include<stdio.h>

int n;


long long max(long long a,long long b)
{
    return a>b?a:b;
}

int main()
{
    while(1) {
        scanf("%d", &n);
        //printf("length : %d\n",n);
        long long arr[100005] = {0},st[100005] = {0};
        if(n==0) break;
        int i;
        long long ans = 0, cnt = 0;
        for (i = 1; i <= n; i++)scanf("%lld", &arr[i]);
        for (i = 1; i <= n + 1; i++) {
            ans = max(ans, arr[i]);
            while (cnt > 0 && arr[st[cnt]] > arr[i]) {
                ans = max(ans, (i - st[cnt - 1] - 1) * arr[st[cnt]]);
                cnt--;
            }
            st[++cnt] = i;
        }
        printf("%lld\n", ans);
    }
    return 0;
}