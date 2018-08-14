
# coding: utf-8

# In[3]:


import os
import csv
file = "/Users/parkerkorita/UTAUS201807DATA2/homework-instructions/03-Python-Instructions/Instructions/PyPoll/Resources/election_data.csv"


# In[4]:


with open (file, "r") as preader:
    lines = []
    data = csv.reader(preader, delimiter = ",")
    for line in data:
        lines.append(line)
    lines = lines[1:]


# In[5]:


total_votes = len(lines)


# In[6]:


total_votes


# In[7]:


cand_list = []
for idx in lines:
# List of candidates 
     cand_list.append(idx[2])

# Khan count and percentage 
khan_count = cand_list.count("Khan")
khan_percentage = (khan_count/len(lines))*100
khan_form_per = format(khan_percentage,".3f") + "%"
khan_final = "Khan: {} ({})".format(khan_form_per, khan_count)
# Correy count and percentage 
correy_count = cand_list.count("Correy")
correy_percentage = (correy_count/len(lines))*100
corr_form_per = format(correy_percentage,".3f") + "%"
corr_final = "Correy: {} ({})".format(corr_form_per, correy_count)
# Li count and percentage 
li_count = cand_list.count("Li")
li_percentage = (li_count/len(lines))*100
li_form_per = format(li_percentage,".3f") + "%"
li_final = "Li: {} ({})".format(li_form_per, li_count)
# O'Tooley count and percentage 
otooley_count = cand_list.count("O'Tooley")
otooley_percentage = (otooley_count/len(lines))*100
otool_form_per = format(otooley_percentage,".3f") + "%"
otool_final = "O'Tooley: {} ({})".format(otool_form_per, otooley_count)


# In[8]:


winner_dict = {"Khan": int(khan_count),"Correy": int(correy_count),"Li": int(li_count),"O'Tooley": int(otooley_count)}


# In[9]:


winner_cand = max(winner_dict, key=winner_dict.get)


# In[10]:


output = (
f"Election Results \n"
f'----------------- \n'
f"Total Votes: {str(total_votes)} \n"
f'----------------- \n'
f"{khan_final} \n"
f"{li_final} \n"
f"{corr_final} \n"
f"{otool_final} \n"
f'----------------- \n'
f"Winner: {winner_cand} \n"
f'----------------- \n'
)


# In[11]:


print(output)


# In[12]:


text_file = open("Output PyPoll.txt", "w")
text_file.write(output)
text_file.close()

