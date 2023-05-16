import colorama
from colorama import Fore,Back,Style
colorama.init()

mensaje = """
 _______  __         .______   .______        ______    _______  _______    .______       __   _______      ___
|   ____||  |        |   _  \  |   _  \      /  __  \  |   ____||   ____|   |   _  \     |  | |   ____|    /   \\
|  |__   |  |        |  |_)  | |  |_)  |    |  |  |  | |  |__   |  |__      |  |_)  |    |  | |  |__      /  ^  \\
|   __|  |  |        |   ___/  |      /     |  |  |  | |   __|  |   __|     |      /     |  | |   __|    /  /_\  \\
|  |____ |  `----.   |  |      |  |\  \----.|  `--'  | |  |     |  |____    |  |\  \----.|  | |  |      /  _____  \\
|_______||_______|   | _|      | _| `._____| \______/  |__|     |_______|   | _| `._____||__| |__|     /__/     \__\
"""

anime = """⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⣿⣿⣿⣿⣿⣿⡿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⡷⣿⣼⣿⣻⣿⣿⣧⢿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣏⢿⣯⣷⣿⣾
⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⢹⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⠿⣟⢟⡻⣿⣻⣿⣿⣿⣿⣿⣾⣿⣿⢿⣿⣻⣿⣧⢿⣿⣿⣿⣿⣿⣿⣿⣷⣻⣿⣿⣎⢿⣿⣿⣾
⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣼⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣎⣷⣿⡿⣿⣿⢻⣿⣿⣿⣿⣿⣿⣎⢿⣿⣿
⣿⣿⣿⡿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⢻⣿⣿⣿⣿⣿⣿⣿⣇⣿⣿⣻⣿⣿⣿⣿⣿⣯⣷⣿⣿⣿⣿⣿⣿⣿⣾⣿⣽⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣻⣿⣯⢿⣿⣿⣿⣿⣿⣿⣎⢿⣷
⣿⣿⣿⣹⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡾⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⣿⣿⣿⣟⣻⣿⣟⣿⣿⣿⣿⣿⣿⣷⢻⣭⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢿⣿⣏⣿⣿⣿⣿⣿⣿⣿⡎⢿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣧⣿⣿⣿⣿⣿⣿⣿⢿⣿⣌⣿⣿⣿⣿⣿⣿⣿⣿
⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣿⣿⣿⣿⣿⣿⣿⣿⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣷⣻⣿⣿⣿⣿⣿⣿⡼⣿⣿⣿⣿⣿⣿⣾⣿⣿⡹⣿⣿⣿⣿⣿⣿⣻
⣿⢣⣿⣿⣿⣿⣿⣿⣿⣿⢻⣿⣿⣼⣿⣿⣿⣿⡿⣾⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣧⣿⣽⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣸⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣏⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⢻⣿⢿⡿⣿⣿⢿⣷⣿⣷⣻⣿⣿⣿⣿⣿⣿
⡟⣾⣿⣿⣿⣿⣿⣿⣿⡏⣿⣿⡯⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⡿⣿⣿⣿⣿⣼⣿⣿⣮⣿⣿⣿⡇⣿⣿⣾⣿⣏⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣹⣿⣿⣿⣿⣿⢿⣿⣿⡿⢿⣿⣏⢿⣿⣿⢻⣯⣿⢻⣿⣿⣯⢿⣿⣿⣿⣿⣽
⢳⣿⣿⣷⣿⣿⣿⣿⣿⢹⡿⣿⣷⣿⣿⣿⣿⣿⣷⣿⣿⡿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⢿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢺⣿⣿⣿⣯⣿⣷⣿⣟⣿⣿⣯⢿⣿⣻⣿⣿⢿⣿⣿⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣷⣿⣿⣇⣿⢿⣿⣿⣿⡎⣿⣿⣿⣿⣿⣿⡞⡿⣿⣷⢿⣛⣱⣿⣾⣿⡞⣿⣿⣾⣿⣿
⣾⣿⣿⣿⢹⣿⣿⣿⣿⣿⣿⢻⣿⣯⣿⣼⣿⣿⢺⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⡟⣿⣿⣿⣿⣿⣼⣿⣿⣿⡟⣿⣿⣯⣿⣿⣿⣿⠘⡇⣿⣿⣿⣾⣿⣿⣿⣷⣿⣿⢸⣿⣯⣿⣿⣿⣿⢻⢸⢳⡟⣿⢸⣿⣿⣿⢸⣾⣯⣧⣿⣿⢸⣿⣿⡏⣿⣿⣷⢹⣯⣿⣿⢻⣧⢻⣿⣿⢻⣾⣿⣿⣿⣿
⣿⣿⣿⠏⣿⣷⡿⣿⢿⣹⢻⡞⡾⡏⡟⣿⣿⢿⣸⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣸⣿⡋⣿⣿⢸⡞⣷⣧⢿⢓⢼⣻⣿⣿⣿⢱⢿⣸⣿⢷⢾⣿⡹⠼⡎⢏⣏⠶⠘⣇⣶⢿⣯⣇⣿⣻⡟⣾⢻⡮⣾⡿⡞⡹⣿⡻⡞⣟⣿⢿⢯⣿⡜⣿⣿⣾⣷⣿⣽⡿⣿
⢿⠳⡙⡜⣧⣟⡝⡏⡞⡟⣿⠏⣹⢱⢠⡏⣭⡿⣾⣻⢿⡿⣿⣾⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⡿⡧⢿⣿⣿⡛⣿⡿⣿⣷⣷⢿⡷⠸⠘⠃⠘⠘⠈⠛⡌⡇⡻⣾⠛⣾⢿⡼⣮⡞⣏⢷⢃⠘⣞⣲⡐⢿⣰⢟⣾⢱⢾⢋⢷⠹⢣⣝⢳⢳⠿⢷⢿⠓⣿⡸⣿⣿⣟⢿⣷⣻⣿⢿⣿⣿⡽⣿⠿
⡇⠀⠁⢀⡻⠘⠃⠂⠡⡶⢿⡼⡽⣆⠻⡏⠝⡇⢾⣯⣾⣧⣿⣷⢻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣼⡟⡗⡷⢼⢿⡿⣟⢿⡷⢿⠚⣿⠘⠋⠀⠀⠀⠀⠀⢀⠀⠁⠀⠈⠁⠀⢻⢪⢏⢯⠣⠂⡸⡜⡁⢈⣧⡆⠜⠆⠛⢢⡆⡜⡇⠀⠈⠃⢜⡞⣏⢏⡜⡞⣷⡘⡧⢻⡛⠞⠾⣿⣷⣻⢞⡏⣿⡟⢻⡼
⢀⣀⣀⣀⣁⣀⣀⠀⠀⠀⠁⠀⠀⠁⠈⠁⠀⠀⢺⡳⢿⠳⣿⣛⣾⢺⣿⣷⣿⣻⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣿⣿⡇⡿⣗⡿⢬⠇⡯⠇⡓⡏⣇⠂⠀⠀⠀⠀⢀⠊⠀⠀⠁⢄⠀⠀⠀⠀⠀⠃⠀⠀⠀⠀⠁⠁⠛⠄⠁⠲⠌⣄⣀⠠⡀⠀⠃⣀⡴⠒⠈⠀⠀⠛⡹⣹⢥⢣⢿⡀⡿⡞⡜⡿⠿⣝⠟⣍⠯⣿⠡⢥
⠀⠀⠀⠀⠀⠀⠈⠉⠉⠙⠓⠒⠤⠤⣀⠀⠀⠀⠈⠀⠋⠀⠁⠛⡇⢺⡹⣿⣿⣼⣿⠿⢿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⡿⢟⣿⢹⣾⢾⢋⠋⠅⠈⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡈⠀⠀⠀⠀⠀⠁⠠⠄⠀⠀⠀⠀⠀⠀⠀⠀⣠⡴⠶⠶⣆⣀⠌⢳⣗⢌⣦⣾⡯⠄⠤⣄⣠⠶⠀⠈⠑⠊⠞⡆⣧⠹⡐⡴⠱⠹⡼⡛⡼⢲⢯⢣⠖
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠈⠑⡐⠠⢀⠀⠀⠀⠀⠓⠸⢷⡧⣿⣇⣿⣿⢿⣿⣿⣾⣿⣿⡏⣿⣿⣿⣿⡿⣿⣗⣾⣿⠘⠃⢹⠀⠀⠀⠆⠀⠀⠀⠀⠀⠀⢀⠄⠄⠀⠠⠁⡆⠀⠀⠀⠀⠀⠀⠀⠈⠐⠂⠤⠤⣤⣶⣯⣓⡤⢶⠷⠶⢭⣷⢮⠻⣟⣞⡝⣩⣴⡿⡋⠀⠀⢀⠀⠀⠀⠀⠹⠁⠁⢩⠧⢁⢧⡙⡃⢦⠉⠎⠀⠘
⠀⠀⠀⠀⠈⠰⡀⠀⠀⠀⠀⠀⠀⠂⡀⠀⠀⠀⠀⠀⠈⠒⠄⡀⠀⠀⠀⠘⠉⣦⣟⠇⡏⡏⣿⣿⣿⣿⡏⣿⣿⣿⣿⣿⣿⢫⢾⡘⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠤⢀⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⣨⡊⠉⠙⢯⡝⢿⡆⠉⠛⠛⠻⠿⣿⣛⢽⣴⣿⠟⣡⡴⢶⠞⣛⡓⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠁⠀⠀⠈⠀⠸
⠀⠀⠀⠀⠀⠀⠈⠐⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠒⠄⡀⠀⠀⠀⠈⠀⠀⢧⡇⡏⣞⣻⡏⡿⣿⣿⡷⠿⡟⣻⢸⠁⠀⢀⠔⠈⠁⠀⠀⠐⠒⠉⠆⠀⢡⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢰⡂⠻⢯⠩⠀⠀⠙⣅⢺⣦⣠⣤⢶⣾⣭⣥⣕⡿⣿⣿⣿⣶⡶⢟⣛⣶⣬⣶⣄⡀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣤⣀⠀⠀
⢀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠒⠂⡀⠐⠊⠰⢄⠀⠀⠀⠀⠹⠇⢗⡛⣼⡇⣷⢻⡟⡇⠋⡟⠩⠀⠀⢰⠃⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠈⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⡈⢧⢁⠀⠀⠀⢻⣻⡥⠈⢣⣤⣶⣶⣿⣕⣻⣿⣛⡁⠚⢋⣩⣭⣷⣌⡉⠙⠂⠀⠀⢀⡼⠛⠋⠉⠁⠉⠓⡌⠑
⠀⠀⠀⠀⡀⠀⢀⠀⠀⠀⠈⠃⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⠀⠀⠳⣀⠀⠀⠀⠂⠨⠇⡏⡇⢡⢸⠃⠀⠹⠀⠠⠀⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠻⠄⠀⠀⠀⢸⡻⣧⠞⠋⠉⣩⣽⣿⣯⣍⣴⣿⣿⣯⣕⣂⣍⠛⢿⡿⢶⣄⠀⡴⠋⢀⠤⠤⢀⠀⠀⢀⣈⢆
⡀⠔⠈⣁⣤⣶⣿⣶⣷⣤⣄⠀⠀⢕⡂⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠘⠢⡀⠈⠑⢄⠀⠀⠀⠀⠀⠃⠀⠘⠂⠀⠀⠀⠀⠀⠀⠀⢿⠠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠻⠀⠀⢀⡼⠛⠉⠉⣉⣹⣿⣿⣝⠻⢯⡻⠟⢉⣥⣶⣍⡈⢀⣶⣿⣿⠿⠶⠢⡉⠲⣷⡦⠀
⢀⡤⠞⠋⢁⠀⠉⠛⠿⣿⣿⣷⡀⠈⠷⠒⠓⠒⠒⠀⠀⠀⠀⠤⠄⡀⠀⠀⠀⠘⢗⡀⠀⢣⡀⠀⠀⠀⠀⠀⢐⠀⠀⠀⠀⠀⠀⠀⠀⠈⢎⠰⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠌⠀⢀⣴⠟⠋⡉⠉⢿⣿⡿⠋⢀⣴⣿⣭⣶⣶⣾⣿⡿⢍⠀⠀⢀⣼⣿⣄⠘⢄⣘
⡫⡡⢀⠂⢎⢊⠀⢀⠀⠈⢻⣿⣿⣦⠈⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠂⢀⠀⠀⠑⠢⠄⠙⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡆⠡⡧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢲⣷⣼⣧⣆⠕⣿⣦⣿⠋⠀⣠⣿⣿⣿⣿⣟⣿⡟⠁⠑⡄⠁⣀⣾⣿⡟⢁⣦⠈⢿
⢊⢄⡝⠔⡀⡂⣌⢀⢒⡡⣁⡘⢿⣿⣇⣀⣁⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠈⠤⠀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣥⢢⡑⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠱⠾⢿⠹⣯⢿⣇⠸⡿⠁⢀⣾⣭⣿⣷⣶⠌⠉⢉⣉⣢⡀⠈⢦⠈⢿⢏⣰⣿⣿⢧⠈
⡧⠠⢉⠊⢗⠔⠀⡄⠿⡠⠁⠀⣨⠟⠁⠀⠀⠀⣀⣆⠀⠀⠀⠀⠀⠀⠀⠀⡀⠤⠤⣀⠀⠀⠀⠔⠈⠉⠑⠒⢤⣀⠀⣀⠤⠞⠋⠉⠉⠉⠉⠁⠀⠃⡕⠼⢊⢄⡀⠀⠀⠀⠀⠀⣀⠠⠤⠤⠤⠀⠀⠀⠀⠀⠀⠀⠤⠄⠀⠀⠀⠀⠀⠀⠀⢀⠌⢁⣴⣾⣿⣿⣿⣆⣝⡴⠧⠠⠛⣧⣌⣻⠟⠁⡠⣾⣿⣿⣿⣿⣄⣿⣇⠈⠻⣿⡿⠁⠀⣇
⣧⣇⣇⣯⢪⢈⢐⣾⠮⠒⠈⢡⠋⠀⠀⠀⢀⣴⣿⢿⣆⠀⠀⠀⢀⡴⠈⠁⠀⠀⠀⠀⠑⢈⡀⣀⣀⣀⣀⠀⠀⠈⠛⢅⣐⣀⡀⠀⠀⠀⠰⠀⠀⠀⠈⠀⢌⢄⡙⣢⣤⠖⠛⠈⠉⠉⠀⠒⠠⢀⡀⠁⠛⢦⣄⣀⣀⣀⠀⠁⠒⢄⠀⣀⠔⢁⣴⢹⢹⡏⢿⠻⣿⣿⣿⣶⣶⣄⡀⠙⡿⠃⢠⣾⡦⣙⡻⡿⢿⣿⣿⣿⢛⡆⠀⠹⡅⣰⣿⣿
⠯⣿⣿⣿⣿⠟⠉⠀⠀⠀⢠⠃⠀⠀⠀⣰⣾⣿⣿⣿⣿⣦⠀⣴⡷⢶⣦⣤⣀⠀⠀⠀⠀⠀⠻⣅⡀⠈⣿⡍⠒⢄⠀⠀⠑⢀⠀⠀⠀⠁⡀⠀⠀⠀⠐⢐⠐⢉⡛⠯⣦⡑⢆⠀⡀⠀⠀⠀⢀⣴⣽⠷⣄⠀⠈⠋⣀⠀⠈⠐⢄⡀⡽⠁⢠⣾⣿⣾⢪⣽⣼⣾⣿⣿⣿⣿⣿⣷⢼⠎⠀⣠⠻⡿⣿⣿⣿⠿⢿⣿⣿⣿⣾⣿⡄⠀⢹⣿⣿⠟
⡠⢀⠜⠋⠀⠈⠉⠔⠂⡔⠃⠀⠀⢀⡰⠛⣿⠻⣿⣿⣿⣿⣿⣾⣿⣿⠟⠀⠈⣷⣦⡀⠀⠀⠀⠑⡉⠲⡝⢿⡉⠒⠹⠦⣄⠀⠑⢤⣀⣠⣥⡀⠀⠀⠂⠠⠄⡀⠀⠈⠩⠉⠉⠘⠒⠒⢰⣴⠿⠯⠅⠀⣈⠳⢤⡀⠀⠠⡀⠀⢠⠟⠀⡴⠻⣿⣿⣾⣿⣿⣿⣿⣿⡏⠀⠙⣿⣿⠊⠀⣰⣷⠀⠱⣼⡻⢿⣷⣿⣿⣿⣿⣿⣿⣻⡄⠘⣿⠋⠀
⠞⠁⠦⣀⠀⠀⠀⠀⠨⠃⠀⠀⢀⡼⠁⠀⠸⠀⠹⣿⣿⣯⣿⣿⣿⠏⠀⠀⣼⣿⣿⠋⠶⡄⠀⠀⠰⣔⠚⠒⠓⠒⠂⠠⠼⢷⡀⠀⠳⣐⣠⡈⠩⡀⠒⡠⣀⠈⣐⡤⢩⠔⠉⠉⠉⠁⠻⢁⡀⢀⠤⠄⡀⡆⠀⠙⣆⠀⠘⣶⠃⢀⣼⢧⣀⣀⡌⠿⠿⠿⣿⠟⣿⠁⠀⢀⣬⡏⠀⢠⣿⢿⣦⠀⢹⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠸⣶⣦
⠐⠂⠠⢄⡀⠀⠀⢠⠁⠀⠀⠀⡴⠀⢀⠀⣠⣀⣄⣺⣿⣷⣿⣿⡏⠀⠀⢠⣿⣿⢇⡐⠮⠛⢷⡄⠀⢹⡉⠁⢩⣹⣷⢦⣀⡀⠘⢦⡀⠑⣦⡀⠉⢐⡒⠔⠈⣀⣀⡴⠋⠀⠀⠀⠀⣠⣾⣿⣿⣦⣄⣤⣬⣾⣦⣀⠘⢦⣰⠃⢀⣞⠁⠊⠉⠀⠀⠀⣀⣠⣤⣥⡚⠄⡀⢸⢿⠁⢀⣿⣯⠙⣿⡆⠀⢻⣶⣿⣿⣿⣿⣿⣿⣿⡿⢹⡆⠀⣿⠻
⡀⠀⠀⠀⠀⠁⢢⠏⠀⠀⢀⡞⠀⢀⣴⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⡖⠠⠽⣿⠉⠀⢀⠀⣀⠨⠷⣄⠀⡗⠓⠦⣧⣿⠀⠀⠙⢿⡚⠿⡄⠈⢏⠙⢷⠶⠛⠛⠉⡽⠁⠀⠀⠀⢠⠾⣀⠊⠘⢿⣿⣿⣿⡟⢿⣿⣿⣿⣦⠇⡠⠚⠀⠀⣀⡤⠶⣾⣿⣿⣿⣿⣿⣿⢷⣾⣿⣟⠀⢸⣿⢛⣯⣿⣿⡄⠈⡿⣿⣿⣿⣿⣿⣿⢿⣿⡌⣷⠀⢸⠀
⠛⠧⠄⣀⡀⠀⡸⠀⠀⠀⣼⣠⢀⣿⣿⣿⠿⠃⢀⣿⣿⣇⣿⣿⣿⣿⣤⡀⠀⠣⢀⣠⣛⣤⣤⡤⢿⡄⢿⣀⠀⠘⠻⣄⠀⠀⠀⠻⣧⣻⡄⠀⠄⠀⠣⡀⠀⢠⠃⠀⠠⠀⢀⡟⢄⠄⢀⣼⠃⠻⣿⣿⣿⣟⣿⣿⣿⣼⠜⠀⠀⣠⠿⡛⠀⠀⢸⣿⣿⣿⢿⣿⣿⣟⣿⣿⣿⣧⣼⡿⡿⣘⣿⣿⡇⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⡄
⠀⢀⡤⠖⠛⣻⠃⠀⢀⡾⠁⠈⠻⢿⠛⠁⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣦⠟⠦⣀⠀⠙⢿⠋⠁⠀⠀⢳⡸⡏⠓⢦⡀⠈⠳⢀⠀⣠⣿⠟⢷⡄⠈⣦⠀⠈⢢⠟⠀⠀⠀⢠⣟⢀⠎⢠⣶⠉⢦⡀⠈⢻⣿⣿⣿⣟⠟⠁⣠⢴⣿⣧⠀⠸⣄⣠⣾⣿⣟⢨⣾⡏⣿⣿⣿⣿⣿⣿⣿⣿⣞⣿⣿⣿⣿⠀⢸⣿⣿⣿⣽⣿⣿⣿⣿⣿⣿⣷⣸⣿
⠶⠋⠀⣠⠞⡹⠀⠀⡼⢧⡀⠀⠀⠀⠡⠄⠀⣾⣿⣿⣿⣿⠈⣿⣿⣿⣿⣠⣾⣿⠗⢄⠀⠐⠀⠀⠀⠀⢷⡇⠀⠀⠍⠳⡄⠈⢾⠟⠁⠀⠀⢻⡆⠘⣷⣲⠋⠀⠀⠀⢠⣿⣺⠎⠀⣼⣧⣀⢾⢷⡄⠀⠹⣿⠟⠃⢠⡞⠁⣸⣿⣿⣇⠀⢻⣽⣿⡿⠿⠼⠿⠧⣾⣿⣿⣿⣟⣿⣿⣷⣟⣿⣿⣾⣯⣷⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⡴⠁⠢⠇⠀⣼⢡⣿⡿⢦⡀⠀⠀⠀⠑⢿⣿⣿⣟⡇⠀⢸⣿⣿⣿⣿⡟⠁⠀⠀⠑⢄⡀⠈⠲⢒⠘⣿⡉⠀⠈⠁⠺⠷⣤⣳⡀⠀⡀⠒⠿⣆⢘⠃⠀⠀⠀⢠⣾⢉⡟⠀⣸⣿⡻⢧⣴⣿⣽⣆⢠⠋⣠⣾⣿⣿⣦⣿⣟⠹⠋⠉⠉⠀⠀⠀⠀⠀⠀⢀⡀⣀⠀⠀⠉⠉⠛⠿⢿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠷⠿⠿⠿⣿⣟⣿
⢠⡞⠃⠃⠁⠃⢠⣏⣿⠟⠀⣠⣿⣶⣄⠀⠀⠀⠻⣿⣿⣄⠀⠀⢿⣿⣿⣿⠀⠀⠀⠀⠀⢀⡽⣦⠀⠀⠱⣾⣿⠶⡿⣷⣶⣶⣬⣟⡧⣖⠀⢀⡶⢻⣿⠀⠀⠀⢠⡾⠁⣿⠀⣠⣿⣿⣿⣿⣿⣿⠟⢻⠃⣴⣿⣿⣿⣿⠟⠉⠀⠀⠀⠀⢀⣀⣤⣴⣶⣿⣿⣿⣿⣿⣿⣿⣷⣿⣷⣦⣦⣤⣌⡻⢿⣿⣿⣿⣿⠟⢉⣀⣀⣀⣀⣀⠀⠀⠀⠉
⡋⡄⢃⡇⡧⡇⣼⣾⠛⢠⣾⣿⣿⣿⣿⣷⣄⠀⠀⠈⢻⣿⣧⡀⠸⣾⣿⣿⣇⠀⠈⢀⠔⠉⢀⡨⠗⢄⠀⠈⢣⡰⢠⢳⠀⠉⠚⣷⣿⣷⠦⠿⠤⣼⠇⠀⠀⢀⡚⢣⣼⣓⣠⣾⠘⣿⣿⡾⠋⠀⣴⠃⣼⣿⣾⣿⠛⠉⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⠿⠟⠛⠛⠛⠻⠿⢽⣷⣿⣿⣿⣻⣿⣶⣿⣷⣮⣻⣩⠾⠿⠿⠛⠛⠛⠛⠿⠿⣿⡷⢦
⠀⠱⣇⠃⢣⣿⣿⢏⣰⣿⣿⣿⣿⣿⡿⠋⣿⣷⡀⠀⠀⠹⣿⣷⡄⣿⣿⣿⣿⡀⠠⠚⠀⣰⠎⠁⢠⠘⠱⣄⣀⣿⣬⠼⠔⠂⠈⠁⠀⣀⢀⣀⢰⡍⠀⠀⠐⢺⣋⠘⠻⣟⣿⣿⣧⡿⠋⠀⢀⣼⢇⣼⣿⣿⡟⠁⠀⠂⢀⣴⣿⣿⣿⠿⠟⠋⠉⠀⣀⣀⣀⣀⣀⣀⠀⠀⠈⠙⠻⢿⣿⣿⡯⠟⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿
⡄⠀⠹⡗⢾⣿⠇⣼⣿⣿⣿⣿⡿⡏⠠⢸⣿⣿⣿⣆⠀⠀⠙⣿⣷⣼⣿⣿⣿⣷⡏⢠⡾⣃⠤⠆⠈⠀⣠⣾⠟⠉⠀⣀⣠⣤⣶⣾⡿⡿⣿⣿⣿⠁⠀⠀⠐⣿⡏⣿⣶⣤⡛⢿⡟⠁⠀⣰⣿⣏⣼⣿⣿⠏⠀⠀⠀⣠⣾⣿⣿⠏⢀⣄⣴⡶⠞⠛⠛⠿⢿⣿⣿⣟⣻⣿⣶⣦⣴⠾⠛⠉⠀⠀⠀⢀⣀⣤⣠⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣶
⢷⡀⠀⢹⣼⣇⣼⣿⣿⣿⣿⡟⡀⢁⠆⢸⣿⣿⣿⡿⢷⡀⠀⠹⣿⣿⣿⣿⣿⣿⣶⣿⠋⢁⣀⣠⡴⠞⡉⡠⠁⣠⡞⠋⠉⠛⠾⢿⡁⡄⠹⣿⣿⠀⠀⠀⠸⣿⣷⣿⣿⣿⣿⠏⠀⠀⣾⣿⣿⣾⣷⡿⠋⠀⠀⢠⡻⣿⣿⣿⣷⣾⣿⡿⠋⠀⠀⢀⣀⣴⣬⣿⢿⣿⣹⡿⠛⠉⠀⠀⣀⣠⠴⠒⣿⣿⣥⡟⠉⠀⠀⠀⠈⠙⢿⣿⣿⣿⣿⣿
⠤⢷⡀⠀⢻⣿⣿⣿⣿⣿⠧⠄⡀⠈⠀⢹⣿⣿⢿⡇⠈⢿⣆⣘⣿⣿⣿⣿⣿⣿⣿⣷⡾⢟⡷⠋⠀⠠⣪⣶⡿⠛⠹⣶⣤⣄⡀⠀⠈⠓⢾⣿⡇⠀⠀⢠⢿⣿⣷⣿⣿⡛⠁⠀⠠⣾⣿⣿⣿⣿⡟⠁⠀⢠⣾⣯⣽⣿⣽⣿⣿⣿⠟⠀⠀⠂⢀⣴⣿⣿⣿⣿⣿⡿⠋⠀⢠⣤⣾⣿⣿⣿⣷⡤⠈⠹⣿⣽⣷⣶⣤⡀⠀⠀⠀⠈⠻⢿⣿⣿
⠤⠼⢷⠀⠈⣿⣿⣿⣿⣧⣤⣤⣀⡁⠢⣼⣿⣿⣿⠃⠀⠈⢿⣶⣻⣯⣿⣿⣿⣿⡿⠋⣠⠞⠀⠀⢨⣾⡿⠫⢣⠀⣴⣿⣿⣿⣙⣷⣦⣄⡀⣿⠃⠀⠀⣸⣻⣿⣿⣿⠏⠀⠀⢀⣼⣿⣿⣿⣿⡟⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⣠⣾⣿⣿⣿⣿⠟⣁⢶⣶⣞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠈⢿⣾⣿⣿⣿⣷⣦⣀⠀⠀⠀⠙⢿"""

print(f"{Fore.CYAN}"+mensaje)
print(f"{Fore.RED}"+anime)
