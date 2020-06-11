

with open('text.txt','r') as rf:
      with open('text_copy','w') as wf:
        for line in rf:
            wf.write(line)

with open('Atom.png','rb') as rp:#rb=read binary.image cant load direct through read
     with open('Atom_copy.png','wb') as wp:#write binary .image is process by binary fomat
         for lines in rp:
            wp.write(lines)
