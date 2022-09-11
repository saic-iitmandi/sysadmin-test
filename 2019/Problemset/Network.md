# Networking

## Problem Statement

1. For every project on Github, many people have local clones on their laptops. Imagine you are working on a project with a team of 4 (all with write access to the repository). Assume that your laptop is switched on 24x7 hours and has a cloned folder of the repository. Now you want that everytime one of your team members pushes to the repository, the folder on your computer is automatically update with latest changes. (Assume that no merge conflict occurs and every update can be fetched and 'fast-forward' merged). 

To do this, create a test repository (or use an existing one). Make two clones of it in your computer in different folder. Push from one folder to Github, should result in the other folder also getting updated with the latest commit. To be able to achieve this you'd need to make use of Github Webhooks, that are triggered on an event.  You'd also need to do this on your mobile network, so that Github is able to access your computer server with your public IP.


2. For `students.iitmandi.ac.in`, you need to find out from what company the domain has been bought. For instance, I bought `abhigyan.xyz` domain name from [Namecheap.me](https://nc.me/). You need to find out from where did the institute buy the domain `students.iitmandi.ac.in`.


## Weightage

1. 125 points
2. 30 points

## Deliverables

In your git repository whose link you will be submitting, make a file `Network.md` where you need to mention your approach for the first part and report your findings, how you did this, what all resources you took help from, and what you learnt.

If you are creating any script or code, make a folder named `Github Update` and put it in the folder with a README. It would also be good, if you can link to a short video demoing the work.

Remember, do not worry if you are unable to complete it, just document whatever you were able to do. :) 
