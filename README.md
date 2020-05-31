# Welcome to the Online appendix of  
## Crème de la crème. Investigating Metadata and Survivability of Top Android Apps 

Mobile apps are distributed via online markets that allow developers to reach a large set of users in different geographic locations. With this online-market-based distribution model, developers have access to a high volume  of crowd-sourced requirements, comments, and ratings. In addition to crowd-sourced reviews, app markets contain valuable apps' metadata that have motivated a plethora of previous works  aimed at mining that information with different purposes. The online markets also operate as a board in which top apps are recognized in lists grouped by category and price, but also in curated lists as the editor choice list of Google Play. Despite the prolific amount of work on app store mining, to the best of our knowledge, the characteristics of the apps on those lists and other aspects such as the survivability in those top-notch lists have not been investigated. Thus in this paper we investigate metadata and survivability of apps in the tops lists of Google Play, from four different countries, and collected during 30 weeks. 


## Reasearch questions and main highlights 
Here you can find the main highlights of each RQs, including some results for not imputed and imputed data.

### RQ1  
_What are the prevalent characteristics of top apps?_

**Main highlights:** for categorical and some numerical variables, there are no differences across countries. Despite this, regarding rating, amount of stars, number of installs and price, differences are relevant. Predominant characteristics of categorical variables remain the same even if we analyze at top-list or country level, with the exception of _Android version_ for Editor Choice. However, predominant variables of numeric variables change mostly across top lists, in particular when dealing with editor choice, despite this, they also change across countries but at a minor rate. Besides, we can conclude that numerical variables related to _length_ do not show relevant differences, but variables related to _rating_ and _amount of stars_ showed large differences in all the cases, no matter the level (top,-list country or top-list-and-country level). In addition, _price_, _number of installs_ and _days since last update_ vary when different combinations across tops and countries are made. Then, when grouping tops and countries, prevailing characteristics differ.

### RQ2  
_Do top apps' predominant characteristics change over time?_

**Main highlights:** after analyzing the data at different time intervals, we conclude that _content rating_, _Android version_, _name length_, _description length_ and _days since last update_ remain consistent among time. However,  _what's new_, _summary length_ and _price_ tend to evolve mostly at the final weeks of the analysis period. _Number of install_ stabilizes at the end and, lastly, _rating_ changes values constantly.

### RQ3  
_What are the top-list survivability patterns exhibited by the analyzed apps?_

To answer this question for each app we analyzed some survivability events to understand survivability behavior patterns in the analyzed apps for some granularities (Country, top, category). 

#### TLO 
A TLO indicates the number of survivability events for an app.
#### Country 



#### Top


#### EST
A EST is the duration of each TLO event.
#### Country 

#### Top

#### TBSE
A TBSE is the time between two consecutive TLO events .
#### Country 

#### Top

**Main highlights:**  taking into account different survivability events can help us to understand some behaviors of the apps in the studied time. For instance, (i) Editor’s choice is the most stable and less diverse top list: it has the lowest number of apps being at the list and the highest survival times;  (ii) between the countries, the events’ distributions can differ but the effect size, in most cases, is trivial (delta<0.2); (iii) if an app returns after leaving a top list, it has a smaller time window for Editor’s choice than for the other tops to do it; (iv) analyzing these events by category show that the differences in the distribution events are, in majority, negligible
