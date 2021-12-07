#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# Hliang, 2021-Dec-05, code the application per pseudocode
# Hliang, 2021-Dec-06, test/modify the script
# Hliang, 2021-Dec-06, (structured error handling has not added yet)
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """
    # DONE Add Code to the CD class
    #  -- Constructor-- #
    def __init__(self, v1, v2, v3):
        #  -- Attributes -- #
        self.__cd_id = v1
        self.__cd_title = v2
        self.__cd_artist = v3
    #  -- Propertities -- #
    @property
    def cd_id(self):
        return self.__cd_id

    @cd_id.setter # TODO not functional
    def cd_id(self, cdID):
        if str(cdID).isnumeric():
            self.__cd_id = cdID
        else:
            raise Exception("error")
    
    @property
    def cd_title(self):
        return self.__cd_title
    
    @property
    def cd_artist(self):
        return self.__cd_artist

    
    @staticmethod
    def Ojb_data(CD):
       """Fuction to make list of objects

        """
#      tblOjb = {'ID': CD.cd_id, 'Title': CD.cd_title, 'Artist': CD.cd_artist}
       lstOfCDObjects.append(CD)

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """

#  -- Method -- #

    # DONE Add code to process data from a file
    #  -- Constructor-- #
    def __init__(self, name):
        #  -- Attributes -- #
        self.__file_name = name
    
    #  -- Method -- #
    @staticmethod
    def load_inventory(name, table):
        table.clear()  # this clears existing data and allows to load data from file
        objFile = open(name, 'r')
        for line in objFile:
            data = line.strip().split(',')
            ojbRow = CD(int(data[0]),data[1],data[2])
            table.append(ojbRow)
        objFile.close()
        
    # DONE Add code to process data to a file
    @staticmethod
    def save_inventory(name, table):
        objFile = open(name, 'w') 
        for obj in table:
            objStr1 = str(obj.cd_id)
            objStr2 = obj.cd_title
            objStr3 = obj.cd_artist
            objFile.write(objStr1+','+objStr2+','+objStr3+'\n') 
        objFile.close()

# -- PRESENTATION (Input/Output) -- #
class IO:
    # DONE add docstring
    """store user's inputs and to printing feedbacks:

    properties:

    methods:
        menu: show menu
        userinputs: hold user's menu option
        usersdata: hold inputs of CD information
        menu_choice(): -> (str argument)
        show_inventory: -> (str of CD information)

    """

    #  -- Constructor-- #
    def __init__(self, val1):
        #  -- Attributes -- #
        self.__valIO = val1

    @property
    def userinputs(self):
        return self.__valIO    
    
    @userinputs.setter
    def userinputs(self,val0):
        self.__valIO = val0

    #  -- Method -- #
    # DONE add code to show menu to user
    def menu():
        return 'Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory\n\
[s] Save Inventory to file\n[x] exit\n'

    # DONE add code to captures user's choice
    @staticmethod
    def menu_choice():
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    # DONE add code to display the current data on screen
    @staticmethod
    def show_inventory(table):
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for item in table:
            vv1 = item.cd_id
            vv2 = item.cd_title
            vv3 = item.cd_artist
            print(vv1,'\t',vv2,'(by:',vv3, ')')
        print('======================================')

    # DONE add code to get CD data from user
    def usersdata():
        userObj1 = IO(input('Enter ID: '))
        userObj2 = IO(input('Enter Title: '))
        userObj3 = IO(input('Enter Artist: '))
        return userObj1.userinputs, userObj2.userinputs, userObj3.userinputs

# -- Main Body of Script -- #
# DONE Add Code to the main body
# Load data from file into a list of CD objects on script start
FileIO.load_inventory(strFileName, lstOfCDObjects)


while True:
    print(IO.menu())
    strChoice = IO.menu_choice()
    # let user exit program
    if strChoice == 'x':
        break
    
    # let user load inventory from file
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileIO.load_inventory(strFileName, lstOfCDObjects)
            IO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.

    # let user add data to the inventory
    elif strChoice == 'a':
        Vals = IO.usersdata()
        CDOjb = CD(*Vals)
        CD.Ojb_data(CDOjb)
        
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.

    # let user save inventory to file
    elif strChoice == 's':
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            FileIO.save_inventory(strFileName, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.

    # show user current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    
    else:
        print('General Error')


