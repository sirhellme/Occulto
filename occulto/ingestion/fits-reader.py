from pathlib import Path

import numpy as np
import pandas as pd
from astropy.io import fits

def read_fits(filepath: str | Path, flux_column: str = "PDCSAP_FLLUX",) -> pd.DataFrame:

    filepath = Path(filepath)

    if not filepath.exists():
        raise FileNotFoundError(filepath)
        