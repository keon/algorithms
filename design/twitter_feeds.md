Design a Twitter feeds API.
How would you actually connect it from a mobile?
What happens behind the Twitter network?
how do the Trends get published?
From where does Twitter get the information for a particular trend(Eg: #Obama, #nfl)
and publish it out?
What protocol does it use?
How do you connect to Twitter API?
How does Twitter handle multiple connections?



Twitter feeds API for 1 user:
The user has M friends and each friend has K new updates.
One possible way is to iterate over all friends and get all the new updates
and display that in feed. O(MK).
But iterating over all the friends is a costly operation,
so i should be getting the feeds from those people whose pics and feeds
i like or comment on or share. We have reduced the iteration on number of people.
We can also use collaborative filtering to decide - what kind of feeds i
would be interested in. Instead of doing all the computations on the fly,
some things can be done offline - for example,
store latest feeds from my friends after I was last active and when i come online,
show those in chronological order.

Connect to Twitter API: Whenever a person gives her credentials
that means one connection is awarded to her.
Now if multiple connections are opened for the same user then according to
'last used' parameter certain connections can be closed.
Also if the user exceeds the limit of number of connections allowed then old connections should be closed.

Twitter uses streaming API. I am not sure about twitter trends though. Can someone elaborate on that?
