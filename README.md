# worst_f1_stats
Data Science to calculate the worst F1 Drivers

## Structure
Simple csv reader, which converts the data into objects of 3 classes. 

### Season
Per year we have a object to store all the seasons results.
We store a dict of race objects. 
 
### Race
Race objects store the results of a race in a particular year.
The Race object stores a 
* list of DNF, DNS, DSQs.
* count of cars started (finished + DSQ + DNF)
* count of cars finished
* a list of reverse finish, normalized over 0 to 1 (1.0 == driver finished last)
* who did the fastest lap.

### Driver
The driver has a list of the years he/she competed, the name, a list of the reverse normalized finishes and the average reverse normalized finish


## Formular

reverse_normalized_finish = finish postion / cars finished the race; # normalized over 0 to 1 (1.0 == driver finished last)
average_reverse_normalized_finish = SUM(all_reverse_normalized_finishes)/ races_competed
worst driver score = ( average_reverse_normalized_finish ** 2) #power of 2 gives being consitently bad more weight)
