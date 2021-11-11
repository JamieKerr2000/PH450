import numpy as np
import matplotlib.pyplot


def gaussp(ti, tfwhm, amp):
    pulse = np.zeros((1, len(ti)), dtype=np.complex64)
    to = tfwhm/1.665
    pu = amp*np.exp(-0.5*(ti/to)**2)
    pulse.real = pu
    return pulse

def gausspc(ti, tfwhm, amp, cp):
    pulse = np.zeros((1, len(ti)), dtype=np.complex64)
    to = tfwhm/1.665
    tp = amp*np.exp(-0.5*(ti/to)**2)
    cp = amp*np.exp(-0.5*cp*(ti/to)**2)
    pulse.real = tp
    pulse.imag = cp
    return pulse

tp = 1.0
taxis = np.linspace(-10*tp, 10*tp, 1024)
gp = gaussp(taxis, tp, 1.)

gpc = gausspc(taxis, tp, 1., 3.0)

