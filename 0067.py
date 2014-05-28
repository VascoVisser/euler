
# coding: utf-8

# This is the same solution as for problem 18

# In[13]:

def compute_max_path(raw_triangle):
    triangle = [[int(i) for i in l.split(' ')] for l in raw_triangle.split('\n') if l.strip() != '']
    line_bottom = triangle[-1]
    for line_top in triangle[-2::-1]:
        c1 = (x[0] + x[1] for x in zip(line_bottom, line_top))
        c2 = (x[0] + x[1] for x in zip(line_bottom[1:], line_top))
        line_bottom = [max(x[0], x[1]) for x in zip(c1, c2)]

    print line_bottom
    
with open("triangle.txt") as f:
    data = f.read()
    compute_max_path(data)


# In[ ]:



