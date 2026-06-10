import os

base_dir = '.'

mapping = {
    'Day01': 'Day01_Variables_and_Band_Name_Generator',
    'Day02': 'Day02_Data_Types_and_Tip_Calculator',
    'Day03': 'Day03_Control_Flow_and_Treasure_Island',
    'Day04': 'Day04_Randomisation_and_Lists',
    'Day05': 'Day05_For_Loops_and_Password_Generator',
    'Day06': 'Day06_Functions_and_Karel',
    'Day07': 'Day07_Hangman',
    'Day08': 'Day08_Function_Parameters_and_Caesar_Cipher',
    'Day09': 'Day09_Dictionaries_and_Blind_Auction',
    'Day10': 'Day10_Functions_with_Outputs_and_Calculator',
    'Day11': 'Day11_Blackjack',
    'Day12': 'Day12_Scope_and_Number_Guessing_Game',
    'Day13': 'Day13_Debugging',
    'Day14': 'Day14_Higher_Lower_Game',
    'Day15': 'Day15_Local_Development_and_Coffee_Machine',
    'Day16': 'Day16_Object_Oriented_Programming',
    'Day17': 'Day17_Quiz_Project_and_OOP',
    'Day18': 'Day18_Turtle_and_GUI',
    'Day19': 'Day19_Instances_State_and_Higher_Order_Functions',
    'Day20': 'Day20_Snake_Game_Part_1',
    'Day22': 'Day22_Pong_Game',
    'Day23': 'Day23_Turtle_Crossing_Game',
    'Day24': 'Day24_Files_Directories_and_Paths',
    'Day25': 'Day25_CSV_Data_and_Pandas',
    'Day26': 'Day26_List_and_Dict_Comprehension',
    'Day27': 'Day27_Tkinter_and_args_kwargs',
    'Day28': 'Day28_Pomodoro_GUI_App',
    'Day29': 'Day29_Password_Manager_GUI_App',
    'Day30': 'Day30_Errors_Exceptions_and_JSON',
    'Day31': 'Day31_Flash_Card_App',
    'Day32': 'Day32_Email_SMTP_and_datetime',
    'Day33': 'Day33_APIs',
    'Day34': 'Day34_API_Practice_and_GUI_Quizzler',
    'Day35': 'Day35_Keys_Authentication_and_Environment_Variables',
    'Day36': 'Day36_Stock_Trading_News_Alert',
    'Day37': 'Day37_Habit_Tracking_API',
    'Day38': 'Day38_Workout_Tracking_with_Google_Sheets',
    'Day39': 'Day39_Flight_Deal_Finder_Part_1',
    'Day40': 'Day40_Flight_Deal_Finder_Part_2',
    'Day41': 'Day41_HTML_Introduction',
    'Day42': 'Day42_HTML_Intermediate',
    'Day43': 'Day43_CSS_Introduction',
    'Day44': 'Day44_CSS_Intermediate',
    'Day45': 'Day45_Web_Scraping_with_Beautiful_Soup',
    'Day46': 'Day46_Spotify_Playlist_Creator',
    'Day47': 'Day47_Automated_Amazon_Price_Tracker',
    'Day48': 'Day48_Selenium_Webdriver_Browser_Automation',
    'Day49': 'Day49_Automating_Job_Applications_LinkedIn',
    'Day54': 'Day54_Web_Development_with_Flask',
    'Day55': 'Day55_HTML_and_URL_Parsing_in_Flask',
}

for old_name, new_name in mapping.items():
    old_path = os.path.join(base_dir, old_name)
    new_path = os.path.join(base_dir, new_name)
    
    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print(f"Renamed {old_name} to {new_name}")
    elif os.path.exists(new_path):
        print(f"Already renamed: {new_name}")
    else:
        print(f"Warning: {old_path} not found.")

print("\nDone renaming folders!")
