import pycolmap
from pathlib import Path
from ..structs.sparse_eval import SparseEvalResult


def write_aligned_reconstruction(
    reconstruction: pycolmap.Reconstruction,
    result: SparseEvalResult,
    output_path: Path,
) -> None:
    
    output_path.mkdir(parents=True, exist_ok=True)
    sim3d = result.alignment
    reconstruction.transform(sim3d)
    reconstruction.write(output_path)
    