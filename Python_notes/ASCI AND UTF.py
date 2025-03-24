'''
 ASCCII CODE:

 * ASCCII stands for American standard code for Information
   interchange

 * Computers didn't understand english words so it is
   assigns each and every words and as an number
   that number are ASCII code.

 * ASCCII code has 0-127 numbers and Alphabat characters
   that characters and numbers are stored in hexa and
   decimal numbers

 EX: decimal  hexa    Char
      65      41      A

 * Like this ASCCII has 127 numbers

 * If we know how computers converts this char to it's
   Binary code then we have to convert decimal and hexa decimal
   values to Binary code

 * There are also an extended version of this ASCCII
   that has some greek symbols

 * The extended version of ASCCII starts form 128

 UTF:

 * Stands for Unicode Charactertices Transformation 
  format.

 * There are various UTF system are there UTF-8,16,32
   but python uses UTF-8 as default

 * The first 128 ASCCII characters are in UTF-8 system
   That takes 1Byte of memeory space 

 * Unicode has many languages latin,greek,Syriac,Thaana

 * All the languages words are stored as an hexa,decimal 
   format, it takes various storage space according to
   the languages

 * You can view any of the characters UTF value by using
   encode method in python

   text='A'.encode('ASCII')
   print(text.hex())

python 2.x used ASCII as the default encoding.

Python 3.x uses UTF-8 as the default encoding for source files and text file operations.

You can explicitly specify the encoding when opening a file:

'''













