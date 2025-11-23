import os
# import pathlib
import re

# --- definisco i path e listo il contenuto ---
path = os.path.dirname(os.path.abspath(__file__))
file_list = sorted(os.listdir(path))

# print(f"{Color.RED}{path}{Color.OFF}")

### parte RENAME ###

# --- definisco il pattern ---
pattern = re.compile(r',\s')
pattern2 = re.compile(r'\s-\s')
pattern3 = re.compile(r'\s')

# --- stampo il contenuto ---
def file_rename():
    for i in file_list:
        if i == ".DS_Store":
            continue
        os.rename(i, pattern.sub('_', i ).lower())
        os.rename(i, pattern2.sub('-', i ))
        os.rename(i, pattern3.sub('-', i ))
        
        print(i)

# file_rename()

### parte YAML ###
def yaml_write():
    with open('../_data/albums.yml', mode='w', encoding='utf8') as file:
        for i in file_list:
            if i == ".DS_Store":
                continue
            
            text = f"""- title:\n  artist:\n  year:\n  file: {i}\n\n"""   
            file.write(text)

yaml_write()


# input('\n\nENTER to clear')
# os.system("clear")