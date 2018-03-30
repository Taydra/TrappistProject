import glob

import PSG

gcmfiles = glob.glob('*terminator.txt')
# print (gcmfiles)
filecount = 1
for i, fil in enumerate(gcmfiles):
    print ("")
    print ("File {}: {}".format(i + 1, fil))
    x = PSG.PSG("TRAPPIST-1 e", fil, scope='MIRI-MRS', exoearth=False, atmoceiling=1e-6, uplayers=7, exptime=30,
                expcount=114, skprow=11)
    x.calculate()
    x.send(run=True)
    x.plot_setup()
    x.depthPlot()
    x.depthHeight()
    x.emission()
    x.raw()
    x.star()
    x.signalNoise()
    x.signalNoiseRatio()
    x.absorption()
    print ("    Radiance Plots Complete")
    x.trnTotal()
    x.trnCO2()
    x.trnN2()
    x.trnH2O()
    x.trnIce()
    x.trnCloud()
    x.trnCIA()
    x.trnSpecies()
    x.trnAero()
    x.trnAll()
    x.noiseBreakdown()
    x.noisePPM()
print ("PSG: Operation complete")
