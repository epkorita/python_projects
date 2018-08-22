
# coding: utf-8

import os
import csv
filepath = "/Users/parkerkorita/UTAUS201807DATA2/homework-instructions/03-Python-Instructions/Instructions/PyBank/Resources/budget_data.csv"



# read the raw CSV
with open(filepath,"r") as breader:
    lines = []
    data = csv.reader(breader, delimiter = ",")
    for line in data:
        lines.append(line)

# columns = ['Date', 'Profit/Losses']
lines = lines[1:]


# In[3]:


# num datapoints
len(lines)


# In[4]:


# sum the dang thing
sum_tot = sum([int(x[1]) for x in lines])


# In[5]:


delta_list = []
mon_list = []
for idx in range(len(lines) - 1):
    # convert to int, grab relevant stuff
    profit_past = int(lines[idx][1])
    profit_curr = int(lines[idx + 1][1])
    # grab month we care about
    month_curr = lines[idx + 1][0]
    # calc delta
    delta = profit_curr - profit_past
    # store stuff we care about
    delta_list.append(delta)
    mon_list.append(month_curr)

# now, let's do math!
tot_pr_los = sum(delta_list) / len(delta_list)
tot_final = format(tot_pr_los,".2f")


# In[6]:


# whats the max value ?
max_val = max(delta_list)
# where does that sit in delta list ?
max_mon_idx = delta_list.index(max_val)
# whats the corresponding value in the parallel, mon_list ?
max_mon = mon_list[max_mon_idx]
print("{} == {}".format(max_mon, max_val))

# whats the max value ?
min_val = min(delta_list)
# where does that sit in delta list ?
min_mon_idx = delta_list.index(min_val)
# whats the corresponding value in the parallel, mon_list ?
min_mon = mon_list[min_mon_idx]
print("{} == {}".format(min_mon, min_val))


# In[7]:


output = (
f"Financial Analysis\n"
f'-----------------\n'
f"Total: ${str(sum_tot)}\n"
f"Average Change: {str(tot_final)}\n"
f"Greatest Increase in Profits:  {max_mon} (${max_val})\n"
f"Greatest Decrease in Profits: {min_mon} (${min_val})\n"
)


# In[8]:


print(output)


# In[10]:


text_file = open("Output PyBank.txt", "w")
text_file.write(output)
text_file.close()

