# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %%
import argparse

parser = argparse.ArgumentParser(description='This script is designed to take a file name and a character, and fix the LaTeX rendering in the file itself')

parser.add_argument('file_name', help='The name of the markdown file to edit')
parser.add_argument('character', help='the LaTeX identifier character')

args = parser.parse_args()

file = args.file_name
sep = args.character
f = open(file, 'r')
data = f.read()
f.close()


# %%
sep_clean = sep + " "
data = data.replace(sep_clean, sep)
data_split = data.split(sep)
for i in range(len(data_split)):
    if i %2 !=0:
        data_split[i] = data_split[i].replace(' \\','\\')
        data_split[i] = data_split[i].replace('\backslash',' \backslash')
        data_split[i] = data_split[i].replace('\subset ',' \subset ')
        data_split[i] = data_split[i].replace('\subseteq ',' \subseteq ')
        data_split[i] = data_split[i].replace('\cap',' \cap')
        data_split[i] = data_split[i].replace('\cup',' \cup')
        if "prod" in data_split[i]:
            data_split[i] = data_split[i].replace('prod', 'displaystyle\prod')
        
        if "sum" in data_split[i]:
            data_split[i] = data_split[i].replace('prod', 'displaystyle\sum')
        
        if "+" in data_split[i]:
            data_split[i] = data_split[i].replace('+', '%2b')
            
        data_split[i] = '<img src="https://render.githubusercontent.com/render/math?math='+data_split[i]+'">'


# %%
final = ''.join(data_split)


# %%
f = open(file, 'w')
f.write(final)
f.close()


# %%



# %%


