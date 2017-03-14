Given input which is a vector of (user name, log-in time, log-out time),
output time series which will have number of users logged in at each given
time slot in the input, output should only contain time slots which are given
in input for example if the input is "September", 1.2, 4.5),
("June", 3.1, 6.7), ("August", 8.9, 10.3) output should contain only
1.2, 3.1, 4.5, 3.1, 6.7, 8.9, 10.3
Example: /* [ ("September", 1.2, 4.5), ("June", 3.1, 6.7), ("August", 8.9, 10.3) ] =>
[(1.2, 1), (3.1, 2), (4.5, 1), (6.7, 0), (8.9, 1), (10.3, 0)] */ 


• Sweeping line method
            § record the time instance and it type: log in, log out
            § Sort the time instances. Keep a variable to record the number of logged in users, number
            § For a time instance,
                □ if it is log-in type, number++, print
else number--, print


1. Constant time random access hash implementation

2. Efficient elevator API

3. Ransom note

4. Median of k unsorted arrays

5. Design of a task scheduler

6. Custom comparator  
