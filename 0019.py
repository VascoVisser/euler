
# coding: utf-8

# In[1]:

year_spec = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap_spec = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
norm_year = [j for i in year_spec for j in range(i)]
leap_year = [j for i in leap_spec for j in range(i)]
years = [(i, norm_year if i % 4 != 0 else leap_year) for i in range(1901, 2001)]
dom_in_years = [j for y in years for j in y[1]]
dow_in_years = [i % 7 for i in range(len(dom_in_years) + 365)][365:]
len([X for X in zip(dom_in_years, dow_in_years) if X[0] == 0 and X[1] == 6])


# In[ ]:



