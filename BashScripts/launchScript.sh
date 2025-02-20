#!/bin/bash
# This script will launch AutomaticPlot.py with each set of parameters
# The file should be in path MPCD/analysisScripts/AutomaticPlot.py
# The code expect to have input.json in MPCD/sampleInputs/myExp/input.json
# It will copy this input.json into Exp* folder which will create itself for each set of parameters
# Feel free to adjust
rm -rf Baziei* slurm-* MPCD0* MPCD1* MPCD2* MPCD3* MPCD4* MPCD5* MPCD6* MPCD7* MPCD8* MPCD9*
rm -rf MPCD/sampleInputs/myExp/Exp*
index=0
rm -r Res
mkdir Res
for rep in 0 #$(seq 0 1 10)
do
        for grav in 0.0
        do
                for pop in 20
                do
                        for size in 50 100 200
                        do
                                for act in 0.05
                                do
					for bs in 0.0 0.05 0.1 0.15
                                        do
                                                for damp in 0
                                                do
							((index=index+1))
							echo "Write $index"
							mkdir MPCD/sampleInputs/myExp/Exp$index
							cp MPCD/sampleInputs/myExp/input.json MPCD/sampleInputs/myExp/Exp$index/input.json
							path="MPCD/sampleInputs/myExp/Exp$index/"
							echo "#!/bin/bash" > BazieiMPCD$index.sh
							echo "python3 MPCD/analysisScripts/AutomaticPlot.py $path $index $grav $pop $size $act $bs $damp" >> BazieiMPCD$index.sh
							echo "mv MPCD/sampleInputs/myExp/Exp$index/avVel*.dat MPCD/sampleInputs/myExp/Exp$index/avVelgrav-$grav-pop-$pop-act-$act-bs-$bs-rep-$rep-size-$size-damp-$damp.dat" >> BazieiMPCD$index.sh
                                                        echo "mv MPCD/sampleInputs/myExp/Exp$index/avOri*.dat MPCD/sampleInputs/myExp/Exp$index/avOrigrav-$grav-pop-$pop-act-$act-bs-$bs-rep-$rep-size-$size-damp-$damp.dat" >> BazieiMPCD$index.sh
                                                        echo "mv MPCD/sampleInputs/myExp/Exp$index/directorfield*.dat MPCD/sampleInputs/myExp/Exp$index/directorfieldgrav-$grav-pop-$pop-act-$act-bs-$bs-rep-$rep-size-$size-damp-$damp.dat" >> BazieiMPCD$index.sh
                                                        echo "mv MPCD/sampleInputs/myExp/Exp$index/flowfield*.dat MPCD/sampleInputs/myExp/Exp$index/flowfieldgrav-$grav-pop-$pop-act-$act-bs-$bs-rep-$rep-size-$size-damp-$damp.dat" >> BazieiMPCD$index.sh
                                                        echo "mv MPCD/sampleInputs/myExp/Exp$index/coarsegrain*.dat MPCD/sampleInputs/myExp/Exp$index/coarsegrain-$grav-pop-$pop-act-$act-bs-$bs-rep-$rep-size-$size-damp-$damp.dat" >> BazieiMPCD$index.sh
                                                        echo "mv MPCD/sampleInputs/myExp/Exp$index/input*.json MPCD/sampleInputs/myExp/Exp$index/inputgrav-$grav-pop-$pop-act-$act-bs-$bs-rep-$rep-size-$size-damp-$damp.json" >> BazieiMPCD$index.sh
                                                        echo "mv MPCD/sampleInputs/myExp/Exp$index/synopsis*.dat MPCD/sampleInputs/myExp/Exp$index/synopsisgrav-$grav-pop-$pop-act-$act-bs-$bs-rep-$rep-size-$size-damp-$damp.dat" >> BazieiMPCD$index.sh
                                                        echo "mv MPCD/sampleInputs/myExp/Exp$index/corrDensDens*.dat MPCD/sampleInputs/myExp/Exp$index/corrDensDensgrav-$grav-pop-$pop-act-$act-bs-$bs-rep-$rep-size-$size-damp-$damp.dat" >> BazieiMPCD$index.sh
                                                        echo "mv MPCD/sampleInputs/myExp/Exp$index/corrDirDir*.dat MPCD/sampleInputs/myExp/Exp$index/corrDirDirgrav-$grav-pop-$pop-act-$act-bs-$bs-rep-$rep-size-$size-damp-$damp.dat" >> BazieiMPCD$index.sh
                                                        echo "mv MPCD/sampleInputs/myExp/Exp$index/corrVelVel*.dat MPCD/sampleInputs/myExp/Exp$index/corrVelVelgrav-$grav-pop-$pop-act-$act-bs-$bs-rep-$rep-size-$size-damp-$damp.dat" >> BazieiMPCD$index.sh
                                                        echo "mv MPCD/sampleInputs/myExp/Exp$index/velfield*.dat MPCD/sampleInputs/myExp/Exp$index/velfieldgrav-$grav-pop-$pop-act-$act-bs-$bs-rep-$rep-size-$size-damp-$damp.dat" >> BazieiMPCD$index.sh
                                                        echo "mv MPCD/sampleInputs/myExp/Exp$index/distSpeed*.dat MPCD/sampleInputs/myExp/Exp$index/distSpeedgrav-$grav-pop-$pop-act-$act-bs-$bs-rep-$rep-size-$size-damp-$damp.dat" >> BazieiMPCD$index.sh
                                                        echo "mv MPCD/sampleInputs/myExp/Exp$index/polarfield*.dat MPCD/sampleInputs/myExp/Exp$index/polarfieldgrav-$grav-pop-$pop-act-$act-bs-$bs-rep-$rep-size-$size-damp-$damp.dat" >> BazieiMPCD$index.sh
							echo "zip -j Res/Exp$index.zip MPCD/sampleInputs/myExp/Exp$index/*" >> BazieiMPCD$index.sh
							echo "rm -rf MPCD/sampleInputs/myExp/Exp$index" >> BazieiMPCD$index.sh
							chmod +x BazieiMPCD$index.sh
							sbatch -plong BazieiMPCD$index.sh
							#sbatch -plong --time=7-00:00:00 BazieiMPCD$index.sh
							#sbatch BazieiMPCD$index.sh
						done
					done
				done
			done
		done
	done
done
