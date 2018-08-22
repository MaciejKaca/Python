import os
path = 'C:\Movies'

list_for_erase = ['5.1', '7.1', '5 1', '7 1', 'DUAL AUDIO', 'DUAL-AUDIO', 'MULTI-CHANNEL', 'Ita-Eng',
'2160p', '4K', '1080p', '720p', '480p', '360p', 'HD', 'FULL HD', 'FULLHD',
'x264', 'CH', 'X264', 'HEVC'
'WEB-DL', 'BrRip', 'Rip', 'DVDRip', 'XviD', 'BLURAY',
'EXTENDED', 'REMASTERED', 'DIRECTORS', 'UNRATED', 'AlTERNATE', 'DVD']

files = []
clear_files = []
for file in os.listdir(path):
    files.append(file)

for title in files:
    for word in list_for_erase:
        title = title.replace(word, "")
    title = os.path.splitext(title)[0]
    clear_files.append(title.strip())

for title in clear_files:
    print(title)