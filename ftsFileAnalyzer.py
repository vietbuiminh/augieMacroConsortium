from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from astropy.io import fits


def main():
    filenames = select_files()
    size = len(filenames)
    for filename in filenames:
         hdulist = fits.open(filename)
         filterName = hdulist[0].header['FILTER']
         expTime = hdulist[0].header['EXPTIME']

         print(filename[filename.rfind('/')+1:] + " \t FILTER NAME = " + filterName + " \t EXPOSURE TIME = " + str(expTime) + " [sec]")
         hdulist.close()
            
#         hdr = pyfits.getheader(filename)
#         file = open(filename, "r")
#         for line in file:
#             print(line)
#         file.close()
        


        
        
def select_files():
    filetypes = (
        ('fts files', '*.fts'),
        ('All files', '*.*')
    )

    filenames = fd.askopenfilenames(
        title='Open files',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected Files',
        message='You chose ' + str(len(filenames)) +' files of fts'
    )
    return filenames



main()