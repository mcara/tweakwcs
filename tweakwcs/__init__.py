"""
This package provides support for image alignment.

"""

__docformat__ = "restructuredtext"

__taskname__ = "tweakwcs"
__author__ = "Mihai Cara"


from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version(__name__)
except PackageNotFoundError:
    __version__ = ""


# import deprecated classes:
from .correctors import (  # noqa: F401
    FITSWCS,
    TPWCS,
    FITSWCSCorrector,
    JWSTgWCS,
    JWSTWCSCorrector,
    RomanWCSCorrector,
    ST_V2V3_WCSCorrector,
    WCSCorrector,
)
from .imalign import align_wcs, fit_wcs
from .linalg import inv
from .linearfit import build_fit_matrix, iter_linear_fit
from .matchutils import (  # noqa: RUF100, F401
    MatchCatalogs,
    MatchSourceConfusionError,
    TPMatch,
    XYXYMatch,
)
from .wcsimage import (
    RefCatalog,
    WCSGroupCatalog,
    WCSImageCatalog,
    convex_hull,
)

__all__ = [
    "FITSWCSCorrector",
    "JWSTWCSCorrector",
    "MatchCatalogs",
    "MatchSourceConfusionError",
    "RefCatalog",
    "RomanWCSCorrector",
    "ST_V2V3_WCSCorrector",
    "WCSCorrector",
    "WCSGroupCatalog",
    "WCSImageCatalog",
    "XYXYMatch",
    "align_wcs",
    "build_fit_matrix",
    "convex_hull",
    "fit_wcs",
    "inv",
    "iter_linear_fit",
]
