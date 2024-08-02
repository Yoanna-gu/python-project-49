from ..games.prime import is_prime_game
from ..engine import start_game


def main():
    start_game(is_prime_game)


if __name__ == '__main__':
    main()