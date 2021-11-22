import click
import logging
from rich.logging import RichHandler
from rich.progress import track
import time
from pathlib import Path
import numpy as np


from ciscode import readers

FORMAT = "%(message)s"
logging.basicConfig(
    level="INFO",
    format=FORMAT,
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)],
)

log = logging.getLogger("ciscode")


@click.command()
@click.option("-d", "--data-dir", default="data", help="Where the data is.")
@click.option("-o", "--output_dir", default="outputs", help="Where to store outputs.")
# @click.option("-n", "--name", default="pa3-debug-a", help="Which experiment to run.")
def main(
    data_dir: str = "data", output_dir: str = "outputs", name: str = "Problem3Mesh"
):
    data_dir = Path(data_dir).resolve()
    output_dir = Path(output_dir).resolve()
    if not output_dir.exists():
        output_dir.mkdir()

    # Read inputs
    Vertices = readers.Vertices(data_dir / f"{name}.sur")
    Indices = readers.Indices(data_dir / f"{name}.sur")

    logging.info("Vertices")
    logging.info(Vertices.arrVer)
    logging.info("Indices")
    logging.info(Indices.arrInd)


if __name__ == "__main__":
    main()
