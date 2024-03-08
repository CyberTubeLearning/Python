                                                                ##### IPL_2022 #####
## ipl_2022 data show.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
ipl = pd.read_csv(r'E:\Croma campus traning $developer (p) ltd\Python\ipl_2022.csv')
ipl_top = ipl.head()
ipl_tail = ipl.tail(7)
# display
print(ipl_top)
print(ipl_tail)

#### top 10 top_scorer
import pandas as pd
# making data frame
ipl = pd.read_csv(r'E:\Croma campus traning $developer (p) ltd\Python\ipl_2022.csv')
# number of rows to return
n = 11
# creating series
series = ipl["top_scorer"]
# returning top n rows
top = series.head(n)
# display
print(top)
## venue match_winner###
import pandas as pd
import matplotlib.pyplot as plt
ipl = pd.read_csv(r'E:\Croma campus traning $developer (p) ltd\Python\ipl_2022.csv')
venue = ipl['venue'].head(10)
match_winner = ipl['match_winner'].head(10)

plt.bar(venue,match_winner)
plt.show()
## top 5 player with man_of_the_match
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
ipl = pd.read_csv(r'E:\Croma campus traning $developer (p) ltd\Python\ipl_2022.csv')
list(ipl['player_of_the_match'].value_counts()[0:5].keys())
# Bar plot for the top 5 player with most man of the match
plt.figure(figsize=(8,5))
plt.bar(list(ipl['player_of_the_match'].value_counts()[0:5].keys()),list(ipl['player_of_the_match'].value_counts()[0:5]),color="pink")
plt.show()
## Toss Decision vs Toss Winner #####
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
ipl = pd.read_csv(r'E:\Croma campus traning $developer (p) ltd\Python\ipl_2022.csv')
ipl.head(2)
print(ipl.head())
ipl.groupby(['toss_decision'])['toss_winner'].value_counts().sort_values(ascending=True).plot(kind='barh', color="red", figsize=(10,5), title = "Toss Decision vs Toss Winner")
plt.show()
#### number of toss won by team ###
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
ipl = pd.read_csv(r'E:\Croma campus traning $developer (p) ltd\Python\ipl_2022.csv')
ipl.head(2)
print(ipl.head())
sns.countplot(x = 'toss_winner', data = ipl, palette ='coolwarm')
plt.title("Toss Wins by Team")
plt.ylabel('Number of Tosses Won by team')
plt.xlabel('Teams')
plt.xticks(rotation= 'vertical',size=10)
plt.show()
## toss decision bat or field ####
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
ipl = pd.read_csv(r'E:\Croma campus traning $developer (p) ltd\Python\ipl_2022.csv')
sns.countplot(x = 'toss_decision', data=ipl, palette="cool")
plt.show()
#### Number of IPL matches won by each team.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
ipl = pd.read_csv(r'E:\Croma campus traning $developer (p) ltd\Python\ipl_2022.csv')
plt.figure(figsize = (10,6))
sns.countplot(y = 'match_winner',data = ipl,order= ipl['match_winner'].value_counts().index)
plt.xlabel('Wins')
plt.ylabel('Team')
plt.title('Number of  IPL  matches won by each team')
plt.show()
##Total Number of matches played in different stadium
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
ipl = pd.read_csv(r'E:\Croma campus traning $developer (p) ltd\Python\ipl_2022.csv')
plt.figure(figsize = (10,6))
sns.countplot(y = 'venue',data = ipl,order = ipl['venue'].value_counts().iloc[:10].index)
plt.xlabel('No of matches',fontsize=12)
plt.ylabel('Venue',fontsize=12)
plt.title('Total Number of matches played in different stadium')
plt.show()
##check the unique values presented in each feature.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
ipl = pd.read_csv(r'E:\Croma campus traning $developer (p) ltd\Python\ipl_2022.csv')
x = ["venue", "toss_decision", "stage"]
for i in x:
  print("------------")
  print(ipl[i].unique())
  print(ipl[i].value_counts())
