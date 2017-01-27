REM Run this from the buildScripts\keil directory

python uvprojCompareTool.py --input ..\..\01_flightCore\keil\flightCoreMfgTest.out.uvprojx  > uvproj\flightCoreMfgTest_.txt

python uvprojCompareTool.py --input ..\..\03_egb\keil\egb.out.uvprojx         > uvproj\egb_.txt
python uvprojCompareTool.py --input ..\..\03_egb\keil\egbHilsim.out.uvprojx   > uvproj\egb_hilsim.txt
python uvprojCompareTool.py --input ..\..\03_egb\keil\egbFuncTest.out.uvprojx > uvproj\egbFuncTest_.txt
python uvprojCompareTool.py --input ..\..\03_egb\keil\egbMfgTest.out.uvprojx  > uvproj\egbMfgTest_.txt
python uvprojCompareTool.py --input ..\..\03_egb\keil\egbMfgTestHelper.out.uvprojx  > uvproj\egbMfgTestHelper_.txt

python uvprojCompareTool.py --input ..\..\actuator\act04p\keil\act04p.out.uvprojx         > uvproj\act04p_.txt
python uvprojCompareTool.py --input ..\..\actuator\act04p\keil\act04pHilsim.out.uvprojx   > uvproj\act04p_hilsim.txt
python uvprojCompareTool.py --input ..\..\actuator\act04p\keil\act04pFuncTest.out.uvprojx > uvproj\act04pFuncTest_.txt
python uvprojCompareTool.py --input ..\..\actuator\act04p\keil\act04pMfgTest.out.uvprojx  > uvproj\act04pMfgTest_.txt

python uvprojCompareTool.py --input ..\..\actuator\act12p\keil\act12p.out.uvprojx         > uvproj\act12p_.txt
python uvprojCompareTool.py --input ..\..\actuator\act12p\keil\act12pHilsim.out.uvprojx   > uvproj\act12p_hilsim.txt
python uvprojCompareTool.py --input ..\..\actuator\act12p\keil\act12pFuncTest.out.uvprojx > uvproj\act12pFuncTest_.txt
python uvprojCompareTool.py --input ..\..\actuator\act12p\keil\act12pMfgTest.out.uvprojx  > uvproj\act12pMfgTest_.txt

python uvprojCompareTool.py --input ..\..\05_pressure\keil\pressure.out.uvprojx         > uvproj\pressure_.txt
python uvprojCompareTool.py --input ..\..\05_pressure\keil\pressureHilsim.out.uvprojx   > uvproj\pressure_hilsim.txt
python uvprojCompareTool.py --input ..\..\05_pressure\keil\pressureFuncTest.out.uvprojx > uvproj\pressureFuncTest_.txt
python uvprojCompareTool.py --input ..\..\05_pressure\keil\pressureMfgTest.out.uvprojx  > uvproj\pressureMfgTest_.txt

python uvprojCompareTool.py --input ..\..\06_gps\keil\gps.out.uvprojx         > uvproj\gps_.txt
python uvprojCompareTool.py --input ..\..\06_gps\keil\gpsHilsim.out.uvprojx   > uvproj\gps_hilsim.txt
python uvprojCompareTool.py --input ..\..\06_gps\keil\gpsFuncTest.out.uvprojx > uvproj\gpsFuncTest_.txt
python uvprojCompareTool.py --input ..\..\06_gps\keil\gpsMfgTest.out.uvprojx  > uvproj\gpsMfgTest_.txt

python uvprojCompareTool.py --input ..\..\08_radio\keil\mrmb.out.uvprojx         > uvproj\mrmb_.txt
python uvprojCompareTool.py --input ..\..\08_radio\keil\mrmbHilsim.out.uvprojx   > uvproj\mrmb_hilsim.txt
python uvprojCompareTool.py --input ..\..\08_radio\keil\mrmbFuncTest.out.uvprojx > uvproj\mrmbFuncTest_.txt
python uvprojCompareTool.py --input ..\..\08_radio\keil\mrmbMfgTest.out.uvprojx  > uvproj\mrmbMfgTest_.txt

python uvprojCompareTool.py --input ..\..\32_adm\keil\adm.out.uvprojx         > uvproj\adm_.txt
python uvprojCompareTool.py --input ..\..\32_adm\keil\admHilsim.out.uvprojx   > uvproj\adm_hilsim.txt
python uvprojCompareTool.py --input ..\..\32_adm\keil\admFuncTest.out.uvprojx > uvproj\admFuncTest_.txt
python uvprojCompareTool.py --input ..\..\32_adm\keil\admMfgTest.out.uvprojx  > uvproj\admMfgTest_.txt
python uvprojCompareTool.py --input ..\..\32_adm\keil\admMfgTestHelper.out.uvprojx  > uvproj\admMfgTestHelper_.txt