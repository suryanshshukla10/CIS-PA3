from pathlib import Path
import logging

log = logging.getLogger(__name__)


class Writer:
    """Abstract output formatter class."""

    def __init__(self, fname: str):
        self.fname = fname

    def save(self, output_dir: str = "."):
        output_dir = Path(output_dir)
        if not output_dir.exists():
            output_dir.mkdir()
        with open(output_dir / self.fname, "w") as file:
            file.write(str(self))

        log.info(f"Saved output to {output_dir / self.fname}")


class PA3(Writer):
    """Output formatter class for programming assignment 3."""

    def __init__(self, name: str, N_samples, d, c, d_norm):
        super().__init__(f"{name}-pa3-X-Output.txt")
        self.name = name
        self.N_samples = N_samples
        self.d = d
        self.c = c
        self.d_norm = d_norm

    def __str__(self):
        outputs = []
        outputs.append(f"{self.N_samples}, {self.name}")
        outputs.append(
            ", ".join(map(lambda x: f"  {x:.02f}", self.d, self.c, self.d_norm)))

        return "\n".join(outputs)
