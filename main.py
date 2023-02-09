from src.controller import Controller


if __name__ == '__main__':
    music_player = Controller()
    music_player.ini_file_exists()
    music_player.main(music_player.save_theme)

