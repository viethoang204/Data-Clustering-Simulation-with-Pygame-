DATA CLUSTERING SIMULATION WITH PYGAME


- I coded this simulation by Python on Jupyter Notebook. There are 02 main pieces of knowledge I have to grasp to complete this program, which are K-means clustering and how to use Pygame. In general, this program helps you to group all the dots you input on the screen by the number of groups(K) that are already set. 

- There are 04 steps to use this one:
  + Step 01: click on the panel of all the dots that you want to group.
  + Step 02: adjust "K" by using "+" and "-" buttons, this is the number of groups that you want the computer to group your dots.
  + Step 03: press the "random" button to generate randomly the number of K groups.
  + Step 04: press the "run" until the error index is the lowest.
  Note: error index is the sum of all the distances between the dots and the clusters that you set.
  
- Mechanism: righ after clicking "run" button, the computer will calculate the distances of each dot to clusters, then find the shortest distance and label the dot with the corresponding color. After that, the computer will locate the average coordinate of the dots having the same label and moving the corresponding cluster to that one. These steps would repeat until the error index is the lowest.

- Limitation: Because of the mechanism, the limitation of this program is that user have to press the "run" and the "random" buttons multiple time to have the best answer.

![nlknklnlknl](https://user-images.githubusercontent.com/119811139/207110060-c8f04e49-89bc-4837-9762-3b6b738c35e3.png)

- Instead of Step 04, you can use the "algorithm" button to have the best result. This is mainly because the function of that one is KMeans from sklearn.cluster so that all the mentioned limits will be solved perfectly.
