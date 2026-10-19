#ifndef DXBALL_CLOCK_IMPORTS_H
#define DXBALL_CLOCK_IMPORTS_H

#include "clock_api.h"

#if defined(_WIN32)
#ifndef WIN32_LEAN_AND_MEAN
#define WIN32_LEAN_AND_MEAN
#endif
#include <windows.h>
typedef LARGE_INTEGER DxBallClockSample;
#define DXBALL_CLOCK_LOW_PART(sample) ((sample).u.LowPart)
#else
/* Keep the callback's actual object and lifetime on the native host. */
typedef DxBallCounter DxBallClockSample;
#define DXBALL_CLOCK_LOW_PART(sample) ((sample).low)
#ifdef __cplusplus
extern "C" {
#endif
DxBallInt DXBALL_DDCALL QueryPerformanceFrequency(DxBallClockSample *sample);
DxBallInt DXBALL_DDCALL QueryPerformanceCounter(DxBallClockSample *sample);
#ifdef __cplusplus
}
#endif
#endif

typedef char DxBallClockSampleLayout[(sizeof(DxBallClockSample) == 8) ? 1 : -1];

#endif
