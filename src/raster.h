#ifndef DXBALL_RASTER_H
#define DXBALL_RASTER_H
#include "state_types.h"

#if defined(_WIN32)
#define DXBALL_RASTER_CALL __stdcall
#else
#define DXBALL_RASTER_CALL
#endif

typedef struct DxBallRasterPoint { DxBallInt x, y; } DxBallRasterPoint;
#ifdef __cplusplus
extern "C" {
#endif
DxBallInt dxball_fixed_divide(DxBallInt number, DxBallInt denominator);

/* Coordinates, differences, fixed-point products, edge carries and pointer
   arithmetic must be representable. The negative-edge comparison negates its
   error as a wrapping 32-bit word. Backing must cover the visited spans.
   Polygons require a positive count and a closed contour with nonhorizontal
   edges. Unclipped polygons require in-bounds coordinates; clipped routines
   use the original fixed 640-by-480 bounds, independent of supplied pitch. */
void dxball_fill_horizontal_span(DxBallByte *row, DxBallInt left,
                                DxBallInt right, DxBallByte color);
void DXBALL_RASTER_CALL dxball_fill_polygon(DxBallByte *pixels, DxBallInt pitch,
    const DxBallRasterPoint *points, DxBallInt count, DxBallByte color);
void DXBALL_RASTER_CALL dxball_fill_polygon_clipped(DxBallByte *pixels, DxBallInt pitch,
    const DxBallRasterPoint *points, DxBallInt count, DxBallByte color);
/* This entry is cdecl, confirmed through its separate shared SEH epilogue. */
void dxball_fill_triangle(DxBallByte *pixels, DxBallInt pitch,
    DxBallInt x1, DxBallInt y1, DxBallInt x2, DxBallInt y2,
    DxBallInt x3, DxBallInt y3, DxBallByte color);
#ifdef __cplusplus
}

/* A four-byte, nonvirtual signed 16.16 value. Default construction preserves
   the scalar; the nontrivial destructor gives temporaries their real lifetime.
   Coordinate products and divisions must be representable. Addition wraps
   as a 32-bit word, using the supported targets' two's-complement storage. */
class DxBallFixedPoint {
public:
    DxBallInt value;
    DxBallFixedPoint();
    ~DxBallFixedPoint();
    DxBallFixedPoint(DxBallInt integer);
    operator DxBallInt();
    DxBallFixedPoint operator/(DxBallFixedPoint denominator);
    DxBallInt operator<(DxBallFixedPoint other);
    DxBallFixedPoint &operator+=(DxBallFixedPoint increment);
};
#endif
#endif
