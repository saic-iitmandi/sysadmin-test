# Networking

## Problem Statement

1. We need maximum information of all the PCs in the `iitmandi.ac.in` network, i.e. `14.139.34.0/24` which are exposed to the internet. For instance, port 443 is for HTTPS, and `students.iitmandi.ac.in` has port 443 open, that is why we see `https://students.iitmandi.ac.in`(notice the `https` before`). You can confirm that by running the following command:

```bash
telnet 14.139.34.3 443
```

and this is the output I get:

```txt
Trying 14.139.34.3...
Connected to 14.139.34.3.
Escape character is '^]'.
```

which implies port 443 is open on `14.139.34.3`. You need to find out all the PCs which are public facing and all their ports open and what kind of operating system they are running on. Any other information would be a bonus.

2. For `students.iitmandi.ac.in`, you need to find out from what company the domain has been bought. For instance, I bought `sahilarora535.me` domain name from [Namecheap.me](https://nc.me/). You need to find out from where did the institute buy the domain `students.iitmandi.ac.in`.

3. Most of the search engines have their own data-centres, for instance Google's data centres can be found [here](https://www.google.com/about/datacenters/inside/locations/index.html). You need to find out how many data centres does [DuckDuckGo](http://duckduckgo.com/) OWN, and what are their locations.

## Weightage

1. 100 points
2. 50 points
3. 50 points

## Deliverables

In your git repository whose link you will be submitting, make a file `Network.md` where you need to report your findings, how you did this, what all resources you took help from, and what you learnt.

Remember, do not worry if you are unable to complete it, just document whatever you were able to do. :) 
