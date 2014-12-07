Voicemail
=========
My first python script :D
#General description
This program mocks a voicemail program which asks the user to select from a range of avaliable clips of mp3 files. The options consists of male/female, reason(s), phone number, and ending(s). After these choices are confirmed and an output file name is provided, a "output.txt" is created containing a record of user input. The selected mp3 files would be then downloaded from a folder hosted by USC. After combining the mp3 files using native commands, the mp3 clips are deleted.
#Command line mode
This program also provides a command line method where flags and arguments are passed from command line instead of prompting for user input. Flags are:
Gender: -g (m/f)
Reason: -r (integer)
Number: -n (string including 10 digits)
Ending: -e (integer)
Output file: -o (string)
