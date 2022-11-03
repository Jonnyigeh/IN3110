## Repository for assignment 4

All tasks are finished except the time_planner merge. 
Had to make some minor modifications in the test functions:
- Had to write the full os.abspath for the png directory in test_find_best_players in order for the script to localize the files. No idea what might cause this to be an issue since the file/directory structure is correct.
- Had to change list(events["something"]) to events["something"].tolist() when testing the directories. These two _should_ be the same, however the program crashes trying to evaluate the list function. (works in the interactive python environment, but not when running the actual scripts)
