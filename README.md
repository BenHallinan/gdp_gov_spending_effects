# The Effects of US National Defense Spending on Individual Economic Well-Being 

# Background
The US Economy is a complex system with numerous interrelated factors, including consumer behavior, business decisions, government policies, and global economic conditions. These factors can interact in unpredictable ways, making it difficult to accurately predict economic outcomes. Even more difficult is understanding how these conditions impact individual economic well-being for the citizens of our nation. 

![](/images/gdp-formula.jpg)
*The GDP equation is economists' most generalized and comprehensive measure in the attempt to understand the aggregate health of a nations economy as it encompasses the total value of goods and services produced within a nation's borders during a specific time period.*

Despite this complexity, there are several macroeconomic tools that we can use to establish a fundamental baseline for determining the economic well-being of the nations population. By taking the Gross Domestic Product (GDP) of a nation and dividing it by its population, we get the variable GDP per capita (GDPpc). 

GDP per capita is a rough estimate of the average income available to each citizen. A higher GDP per capita typically means that, on average, people in that country have more income at their disposal for their needs and wants. A rising GDP per capita generally indicates economic growth and development. It suggests that the overall economic conditions are improving, which can positively affect the well-being of citizens. This includes access to better education, healthcare, infrastructure, and a higher quality of life. 

When looking at the GDP formula, no variable is as contested and debated over as the "G". With the numerous ways the Government both directly and indirectly affects the economy, it is no surprise. Now, while the many indirect ways the Government affects the economy are significant in their own right (monetary policy, taxation, regulation, etc), Government spending stands at the top in its ability to influence every aspect of our Nation. And of course, the elephant in the room on every conversation about government spending, our continued deficit spending and the National Debt.  

![](/images/debt_clock.png)
# Purpose
The purpose of this research is to develop a model on the relationship between various components of government expenditure and the overall economic well-being of our population. With this, the intent is to determine if there is a significant positive or negative relationship between the spending categories and U.S. GDP per Capita. The results I am most interested in is the effects of National Defense Spending on our economic well-being. This is due to our National Defense Spending being one of the most debated and it being the largest part of our discretionary budget.

This model could be a useful insight for U.S. policymakers in the long-term planning and evaluation of policy and aid in the optimal allocation of government resources and could also serve as a valuable tool in the argument for why National Defense Spending is so critical to our nation. 

## Proposed Question(s)
What is the effect of National Defense Spending on our nations GDP Per Capita? How does the other spending category independently effect the economy for U.S. Citizens as well?

# Data
All data used in this research was compiled from the Federal Reserve Economic Data(FRED), which was created and maintained by the Research Department at the Federal Reserve Bank of St. Louis. The following is a table of the time-series data taken from 1960 - 2023:

| Economic Data                | Definition|
| ---------------------------- | --------- |
| GDP Per Capita               | Measure used to assess the economic well-being and standard of living of a country's residents. |  
| Total Government Spending    | All U.S. spending to include all consumption expenditures and gross investments |  
| Defense Spending             | Portion of federal government consumption expenditures and gross investment that covers the military activities of the U.S. Department of Defense |  
| Nondefense Federal Spending  | Total government expenditures by the federal government of the United States on all programs and activities at the national level except those related to national defense |  
| State & Local Spending       | Total government expenditures made by state and local governments in the United States.  |  
| Government Transfer Payments | Cash or in-kind payments made by the government to individuals, households, or other entities that do not result in the government receiving goods, services, or assets in return. These payments are typically intended to provide financial assistance or support to individuals or groups within the economy. |

*Note: All data aggregated was done so in both the form of relative dollar amounts (USD & Billions of USD) and percent change by quarter. This allowed for various ways to visualize and model the data appropriately.*

The construction of these datasets intentionally leaves out all data on the payment of interest and the total government spending reflects that as well. Interest payments on the national debt are a financial obligation of the U.S. government and are a result of borrowing to cover budget deficits and finance government operations. 

# Data Visualization
![](/images/spending_vs_gdppc_graph.png)
Looking first at the government spending breakdown, we can see the change overtime of the overall allocation of the US Federal Budget. Comparing that to GDP per Capita, we can see that while they are both relatively increasing each year, government spending has expanded at a significantly more rapid pace. The general causes of which show themselves to be in state & local spending and Federal Transfer Payments while both Defense and Nondefense Federal spending appear to have increased at a more gradual and consistent basis. So, the question then arises, how might these two plots interact? 
![](/images/pct_spending_gdppc_graph.png)
By switching our unit of measure to percent change from the previous fiscal quarter, we can inspect the relationship between our data with a much more relative comparison. Now, at first glace, the relative comparison between percent change in total government spending and percent change in GDP per Capita, does not appear to be insightful. However, in analyzing the trends that appear in the plot, it looks as if there is a lead-lag relationship between government spending and GDP per Capita. To elaborate, it appears that any time GDP per Capita trends down in a quarter, we see a response from the Government in the form of increased spending the following quarter. So, at a surface level, visualizing this data together tells us that there appears to be a positive corelation between government spending and GDP per Capita. Which, while may seem obvious, is serves as basic validation that our GDP equation makes sense when beginning to talk about the effects of government spending on GDP.
   
# Implementation of Regression Model
In order to analyze the effects of the different types of spending on GDPpc, I created several inferential linear regression models. In total, I created 4 primary models; two simple and two complex. The two simple models were a univariate analysis of the effects of total government spending on GDPpc, with the second having GDPpc log transformed to see whether it better represented the relationship. As I expected, the simple models show a significant but not very useful output in which it suggests a positive but marginal relationship between the two variables. The point of conducting the simple regressions were to show that knowing the overall relationship (which again we already new from the GDP equation), does not allow us to provide meaningful insight or give fiscal policy recommendations. 

![](/images/simple_models.png)
*On the left is our simple monetary model and on the right is our simple log transformed model.*

As I develop the complex models, we begin to see the main point of the analysis take shape. Both the complex models were developed in the same manner as the simple, with the first having all variables remaining without transformation and the second GDPpc log transformed once more. With these models, we go beyond the inferential analysis of total government spending and expand the independent variables into the various categories of spending: National Defense, Non-Defense Federal, State & Local, and Transfer Payments. 

![](/images/complex_models.png)
*On the left is our complex monetary model and on the right is our complex log transformed model.*

Now, the results start to tell us a lot more; and they are quite interesting at that. While each model is interpreted differently (see table in Results section), they each tell the same story: increases in National Defense and State/Local spending both have a positive relationship with an increase in GDPpc while Non-defense Federal and Transfer Payment Spending have a negative relationship.

I will get into the analysis of the results and the 'So What' in the next section, but it important to note why I chose to only transform the dependent variable in the second model(s). It is the attempt to best capture the relative effects of each spending category despite the vast differences and complexities that are buried in each of those numbers. Additionally, even when breaking down total government spending into each of these major categories, they remain highly correlated with each other. After all, if we think of each of them as a slice of a pie, a relative increase in one category has the potential to mean a relative decrease in another. So, when dealing with independent variables such as U.S. spending categories, solely transforming the dependent variable gives us the best chance as seeing a relatively True results in a model as oversimplified as this. 
![](/images/spending_pie.png)

# Results
In the conduct of this research and the design of these regression models, I sought to answer the following question: What is the effect of each major U.S. Government Spending Category on GDP per Capita and, if any, are the results significant? The table below takes the coefficients of our independent variables and states their full interpretation. 

![](/images/Results_table.png)

Now, with the results of the analysis in hand, very insightful and interesting conclusions can start to be drawn. Lets start the analysis of each variable beginning with Nondefense Federal spending; as I think the results of the National Defense coefficient deserves the most attention. 

Nondefense federal spending not only was significant but was also the largest impact on GDPpc in absolute terms. The clear take away here is that, at the Federal level, the Government is being significantly inefficient, wasting, and/or misallocating funds. Simply put - The Federal government is either spending too much money or is grossly misallocating them. It does not take any time in a quick search to have this easily backed up; and countless times at that. This model now gives us the means to discuss this in terms of the impact on the individual American. Let's take the spending from the 2nd QTR of 2023 as our empirical example. In this QTR the Federal Government spent $765 billion dollars. So, using that with our model, on average holding all else constant, the inefficiencies in Federal spending would cost each American $42,000 dollars. 

The most unsurprising result was the effect of state & local spending. Having the overall largest positive effect on GDPpc, this result is a great representation on the effectiveness of localizing efforts and is a tremendous argument towards a greater emphasis on state governments. The inferences from these results is that there is much greater information and knowledge on the distribution and allocation of government expenditures and investments when local governments are allowed to allocate funds as needed by their communities.

Government Transfer Payments, and the results they produced, highlight just how complex these relationships are and why no solution is ever going to be absolute. The results of the transfer payments coefficient may be significant, and negative at that, but the effect is so small that any real insight is hard to be drawn. However, in staying in line with the model, there are some significant logical explanations as to why the relationship may in fact be negative and may be something the U.S. government may want to examine in greater detail:
* Crowding out private investment: When the government increases transfer payments, it often needs to finance these expenditures through taxation or borrowing. Higher taxes can reduce disposable income for individuals and businesses, potentially leading to reduced private consumption and investment.
* Disincentives for work and productivity: If transfer payments are too generous or not designed well, they can create disincentives for individuals to work or seek employment, as the benefits they receive from the government might outweigh the financial gains from working.
* inefficiencies in resource allocation: Transfer payments may not always be targeted efficiently, leading to misallocation of resources. If these payments are not reaching those who need them most or if they are encouraging unproductive behavior, it can result in a less efficient allocation of resources in the economy.

Finally, onto the discussion of the impact of National Defense spending. Without a closer look, the initial thought would be that while necessary, National Defense spending negatively impacts GDPpc as it is funds that otherwise could be invested in other aspects of the country. However, in analyzing the data and the historical context of the relationship of our military with the rest of the nation, we can see that the funding of our military has indirectly been a significant contributing factor to the country's economic growth and development. The positive coefficient of our model captures numerous avenues of impact and here are some examples of this impact:
* Stimulating Technological Innovation: Defense spending has historically driven technological advancements. Research and development in areas such as aerospace, electronics, and materials science have been spurred by defense needs. These innovations often spill over into the civilian sector, leading to the development of new consumer products and industries.
* Education and Training: The military provides extensive education and training for its personnel. This includes technical and vocational training, as well as funding for higher education through programs like the GI Bill. This investment in human capital increases the skills and productivity of the workforce, contributing to higher incomes and economic growth for individuals and the country as a whole.
* Infrastructure Development: Defense-related projects often require substantial infrastructure investments, such as military bases, research facilities, and transportation networks. These projects create jobs during construction and contribute to the long-term economic development of the regions in which they are located.

While these models remain vastly oversimplified in the sense of macroeconomic data analysis, they provide a data driven insight into the ways that leaders and lawmakers around the nation can better our economy and the economic well-being of each and every one of us. 

# Inspiration
I took a lot of inspiration from all the great work that the Office of Economic and Manpower Analysis (OEMA) is doing and thought to look at the material and financial side of things. And while there is not of easily parsable data to closely look at the efficiency and effects of Defense spending, I wanted to as least show as a starting point that there is a positive relationship between defense spending and the well-being of the US Population; as indirect as those effects may be they are important.


