//Given a value N, if we want to make change for N Cents, and we have infinite supply of each of S(coins) = { S1, S2, .. , Sm}, 
//how many ways can we make the change? 

//For example, for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}. So output should be 4.
//For N = 10 and S = {2, 5, 3, 6}, there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class CoinChange {

   static long[][] store;
    static long getWays(int[] c, int m,int n){
        // Logic

        if(n==0)
        {
          //if n=0, then there is 1 solution (do not include any coin)
            return 1;       
        }
        
        if(n<0)
        {
          //we are expecting that n is positive integer
            return 0;     
        }
        if(m<=0 && n>=1)
        {
          //if there is no coin
            return 0;      
        }
        if(store[n-1][m-1]==0)
          store[n-1][m-1]=getWays(c,m-1,n)+getWays(c,m,n-c[m-1]);       
        //storing values in matrix  
        
        
        
        
        return store[n-1][m-1];

    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();
        int[] c = new int[m];
        for(int c_i=0; c_i < m; c_i++){
            c[c_i] = in.nextInt();
        }
        store=new long[n][m];
        
        // Print the number of ways of making change for 'n' units using coins having the values given by 'c'
        long ways = getWays(c,m,n);
        System.out.println(ways);
    }
}
