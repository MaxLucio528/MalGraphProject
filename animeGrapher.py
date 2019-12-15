'''
Here we import the following libraries:

1 - time: To have a delay after 2 animes are obtained due to API limitations;
2 - graphGenerator: Function that generates the graph;
3 - getAnimeData: Function that gets the anime data.
'''

import time
from graphFunctions.graphGenerator import graphGenerator
from graphFunctions.getAnimeData import getAnimeData
from generalFunctions.clearScreen import clear


# The main function that controls everything.
def main():
    # Trying to run the program normally.
    try:
        '''
        This is the option variable that determines what the program gonna do
        or if the program will continue running or not. 
        '''
        op = -1

        # Loop that runs the program while the user wants.
        while(op != 0):
            clear()
            print("----------------------------------------------")
            print("          Anime Graph Generator v2.0          ")
            print("----------------------------------------------\n")
            print("1 - Add one anime to the graph")
            print("2 - Add multiple animes to the graph")
            print("0 - Exit")
            op = int(input("\nPlease select a option: "))
            clear()

            # One anime will be added to the graph.
            if(op == 1):
                # Repeats till a valid ID is obtained.
                while(True):
                    # Asking the user to type the ID of the anime to be added.
                    animeID = input("Please type the ID of the anime you want to add to the graph: ")
                    print()

                    # Invalid ID chosen.
                    if(int(animeID) < 1):
                        print("Invalid number!\n")
                        clear()
                    else:
                        break

                clear()
                # Calling the function that will get the anime data.
                print("We're collecting the data, please wait...\n")
                getAnimeData(animeID)
                input("Press ENTER to continue...")

            # Multiple animes will be added to the graph.
            elif(op == 2):
                # Repeats till a valid ID is obtained.
                while(True):
                    # Asking the user from where to start.
                    firstAnimeID = input("Please type the ID from where you want to start adding to the graph: ")
                    print()

                    # Invalid ID chosen.
                    if(int(firstAnimeID) < 1):
                        print("Invalid number!\n")
                        clear()
                        continue
                    else:
                        break
                
                # Repeats till a valid ID is obtained.
                while(True):
                    # Asking the user from where to stop.
                    secondAnimeID = input("Please type the ID from where you want to stop adding to the graph: ")
                    print()

                    # Invalid ID chosen.
                    if(int(secondAnimeID) < int(firstAnimeID) or int(secondAnimeID) == int(firstAnimeID)):
                        print("The second number must be bigger than the first one!\n")
                        clear()
                        continue
                    else:
                        break
                
                clear()
                # Calling the function that will get the anime data.
                print("We're collecting the data, please wait...\n")

                # Counter to know when to sleep, preventing problemas with the API.
                i = 0

                # Repeats till all animes were obtained.
                for x in range(int(firstAnimeID), int(secondAnimeID)+1):
                    # Sleeps for a second, preventing the error 429.
                    if(i % 3 == 0):
                        time.sleep(1)

                    # Calling the function that will get the anime data.
                    getAnimeData(x)

                    i += 1

                input("Press ENTER to continue...")

            # Exiting the program.
            elif(op == 0):
                print("Program terminated...\n")
                exit()

            # Invalid number.
            else:
               print("Invalid number! Please try again...\n") 
    # If anything goes wrong with thoses processes the program is redirected here.
    except Exception as e:
        print(e)

# Starting the program.
main()