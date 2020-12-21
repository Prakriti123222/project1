import pandas as pandas           #the name written after "as" is the name of library that we will use in the code
import numpy as np
import matplotlib.pyplot as plt


#This graph shows the stats of social media worldwide based on over 10 billion monthly page views.
socialmedia = pandas.read_csv("socialmedia.csv")     #reading the social_media.csv file with help of pandas library


# Making line graph 
plt.title(''' Worldwide Visitors on various social media platforms
            over the last 12 months(in %)(November 2019 - November 2020)''')
plt.plot(socialmedia.Date,socialmedia.Facebook,label="Facebook",marker=".")           
plt.plot(socialmedia.Date,socialmedia.YouTube,label="You Tube",marker=".")
plt.plot(socialmedia.Date,socialmedia.Instagram,label="Instagram",marker=".")          # labels are given to display text to user. it is also used to distinguish various line graphs.
plt.plot(socialmedia.Date,socialmedia.Pinterest,label="Pinterest",marker=".")           
plt.plot(socialmedia.Date,socialmedia.Twitter,label="Twitter",marker=".")
plt.plot(socialmedia.Date,socialmedia.VKontakte,label="VKontakte",marker=".")
plt.plot(socialmedia.Date,socialmedia.LinkedIn,label="LinkedIn",marker=".")
plt.plot(socialmedia.Date,socialmedia.reddit,label="Reddit",marker=".")
plt.plot(socialmedia.Date,socialmedia.Tumblr,label="Tumblr",marker=".")
plt.plot(socialmedia.Date,socialmedia.Other,label="Other",marker=".")
plt.xticks(socialmedia.Date[::2])          #.xticks() is used to add xtick_labels on x axis with a step value of 2
plt.xlabel("Months")                                                       # .xlabel() is used to give label(name) to x-axis 
plt.ylabel("Visitors(worldwide) per month (in%)")                # .ylabel() is used to give label(name) to y-axis 
plt.legend()                                                              # .legend() is used to place legend on axis.its default location is upper left.
plt.show()                                                                # .show() is used to show the plotted graph



# making pie chart
mean_visitors=[]                                                                 
l=[]
for values in socialmedia.Facebook:
    l.append(values)
r=(sum(l)/13)                                                             # finding mean % of users visiting facebook in last 12 months
mean_visitors.append(r)
l=[]
for values in socialmedia.YouTube:
    l.append(values)
r=(sum(l)/13)                                                             # finding mean % of users visiting Youtube in last 12 months
mean_visitors.append(r)
l=[]
for values in socialmedia.Instagram:
    l.append(values)
r=(sum(l)/13)
mean_visitors.append(r)                                                            # finding mean % of users visiting instagram in last 12 months
l=[]
for values in socialmedia.Pinterest:
    l.append(values)
r=(sum(l)/13)                                                             # finding mean % of users visiting pinterest in last 12 months
mean_visitors.append(r)
l=[]
for values in socialmedia.Twitter:
    l.append(values)
r=(sum(l)/13)
mean_visitors.append(r)                                                            # finding mean % of users visiting twitter in last 12 months
mean1=[]                                                                      
l=[]
for values in socialmedia.VKontakte:
    l.append(values)
r=(sum(l)/13)                                                             # finding mean % of users visiting VKontakte in last 12 months
mean1.append(r)                                                                
for values in socialmedia.LinkedIn:
    l.append(values)
r=(sum(l)/13)                                                             # finding mean % of users visiting linkedin in last 12 months                                                                 
mean1.append(r)
l=[]
for values in socialmedia.reddit:
    l.append(values)
r=(sum(l)/13)                                                             # finding mean % of users visiting reddit in last 12 months
mean1.append(r)
l=[]
for values in socialmedia.Tumblr:
    l.append(values)
r=(sum(l)/13)                                                             # finding mean % of users visiting tumblr in last 12 months
mean1.append(r)
l=[]
for values in socialmedia.Other:
    l.append(values)
r=(sum(l)/13)                                                             # finding mean % of users visiting other platforms in last 12 months
mean1.append(r)
mean_visitors=mean_visitors+[sum(mean1)]                                                    # mean_visitors is a list containing mean % of users on all social media platforms.                                                         
name_of_platform=["Facebook","Youtube","Instagram","Pinterest","Twitter","Others"]    # labels
exp=[0,0.2,0.2,0.2,0.2,0.2]          # exp here is user defined list to store explode values. it is used to define that which part should explode. values given are distances of exploded parts from centre.                     
plt.title(" Mean Percentage of worldwide visitors on various social media platforms ")
plt.pie(mean_visitors,labels=name_of_platform, explode=exp, autopct="%2.2f%%")                 # autopct agrument takes the format in which we want to see the %age.it contains a special string which starts and ends with % sign
plt.show()


# making a bar graph with mean %age of visitors on various sites.
plt.bar(name_of_platform,mean_visitors)
plt.xlabel("Social Media Platform")
plt.ylabel("Mean Visitors Worldwide")
plt.title("Mean %age of visitors(worldwide) on various platforms ")
plt.show()


#making bar graph with initial and final %age of visitors on a specific site.
list=[[84.68,4.06,4.84,3.85,2.30,0.27],[74.18,10.41,4.30,6.98,3.45,0.67]]    # list of initial and final % of visitors on various sites.
label1=["Facebook","Youtube","Instagram","Pinterest","Twitter","Others"]
label1=np.arange(6)                                                          # used to arrange 6 bars on x axis with equal space between them.
plt.bar(label1+0.00,list[0],width=0.40,label="Nov'19")                       
plt.bar(label1+0.40,list[1],width=0.40,label="Nov'20")
plt.xticks(label1,["Facebook","Youtube","Instagram","Pinterest","Twitter","Others"])
plt.title(""" %age of visitors(worldwide) on different social media platforms 
                 in nov'19 and nov'20 (blue for nov'19 and orange for nov'20)""")
plt.show()




