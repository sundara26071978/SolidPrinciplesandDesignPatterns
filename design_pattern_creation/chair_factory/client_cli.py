import click
from chair_factory import ChairFactory

@click.command()
@click.option("--chair-size", "-s", default="medium", help="Chair size to buy")
def main(chair_size):
    CHAIR = ChairFactory.create_chair(chair_size)
    print(CHAIR.get_dimensions())
    
if __name__ == "__main__":
    main()

# To run this file, use the command below in terminal
# uv run .\client.py --chair-size small