# Administration

## Problem Statement


1. The following is a beautiful problem again from last year (probably the best one). Doing this is a great learning and satisfying experience, so please attempt to do this question.

Censorship on the internet is a pain which we all go through. While we here are thinking what we should do about censorship in our institute, another group of people was writing code to make this happen, and hence made [`streisand`](https://github.com/StreisandEffect/streisand): <https://github.com/StreisandEffect/streisand>. This group of people made this awesome open source software which can be used to break through all the restrictions. The software they made can be installed on any set of remote server, for instance on the [AWS(Amazon web services)](https://aws.amazon.com/) server, or [digitalocean droplets](https://www.digitalocean.com/) server. These are nothing but remote computers which you can buy and use for yourself. You even get free to try, for instance you get [750 hours of Amazon EC2(EC2 is the amazon name a server or computer) for free](https://aws.amazon.com/free/) which is approximately 30 days. Digitalocean charges $5 (Rs. 320) for 1 month for 1 virtual PC with 1 GB ram.

Your task is very simple. You need to signup on AWS / Digitalocean / some other virtual server providing company and install `streisand`. Then you need to ***SETUP YOUR OWN VIRTUAL PRIVATE NETWORK(VPN)*** according to the instructions given on the streisand github page. All the supported virtual server providers are given on the [streisand github page](https://github.com/StreisandEffect/streisand). Choose whatever you like.

**NOTE:** If you go with any of the virtual machine providers, remember to switch off the servers when not in use, else you may face additional charges.

***UPDATE***: Here is the link to a $10 free Digitalocean referral, so you get $10 is you sign up on DigitalOcean with this link, equivalent of 2 months of CPU storage. It's upto you which one to choose now, DigitalOcean or AWS, you have both of them free.

Creating a virtual server on Digital Ocean is easy, and now you have 2 free months, so you can go with that. If you want to go for AWS, no issues, your decision totally. :-)

***Link: <https://m.do.co/c/fc3343ab2be0>***

2. A hacker has gained access to a user named `user69` on one of your servers and wishes to cause damage to it. You have two services 'A' and 'B' running on your server. 'A' is an application that is used by a million users and downtime for this will have a great negative impact on your company. Meanwhile 'B' was a test project you were working on but forgot to close. 'A' was updated last Saturday and no new vulnerabilities have yet been reported. But it has been 2 years since 'B' was last updated and several vulnerabilities have been reported, and you ignored them. It is very likely that the hacker exploited service 'B' and has setup a back-door in your server. Fortunately for you, `user69` does not have superuser access on your server (YET!). Your task is to come up with a way to prevent this hacker from gaining superuser access, causing harm to users of 'A' and prevent such future attacks.



## Weightage

1. 170 points (If you have done it last year and don't want to do it again, please mention it and link to your solution in last year year's submission).
2. 30 points

## Deliverables

In your git repository whose link you will be submitting, make a folder `Administration` with 2 file in it:

1. `Administration.md`: Here you need to report your findings, how you did this, what all resources you took help from, and what you learnt.
2. `VPNSetup.md`: This should contain the steps required for anyone to use your VPN. For instance, we use `SurfEasy` or `Psiphon` as a VPN in our smartphones. We need to be able to connect **ANY ONE DEVICE**, either a smartphone or a PC, with your custom VPN (though if you setup coorectly, it should work for both without any issues).

Remember, do not worry if you are unable to complete it, just document whatever you were able to do. :)
