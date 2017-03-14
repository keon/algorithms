Consider that the driver with one trip want to pick up some peoples in different locations like this:
String[] locations ={
"person1, person2, person3, person4, person5",
" person6, person7, person8, person9",
"person10, person11, person12",
"person13, person14, person15",}
in each location there are different choice, so write a code present all possible way to pick up people in the different locations.
you can use every data structure needs.


This could be solved using minimum spanning tree concept

***assume taxi is large enough for all passengers****

Arrange all the pickup locations as vertices of a graph along with the present location of the taxi as

one of the vertex

now start with the present location and add that edge with has lowest weight ,this means we have

visited to the location which is nearby and pic all the passangers, then search for the next nearby location

locations and so on until all the locations are visited once
