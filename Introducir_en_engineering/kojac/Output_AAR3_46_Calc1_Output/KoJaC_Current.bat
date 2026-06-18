rem Installation directory
set MSC_VCJOINT_SRC=\\Viper041a\GKN_ViPeR_code\Production\MultirunBatch\General\KoJaC_v7r2\Kojac

rem Adams version
set ver=2024_1

rem Working directory
set MSC_VCJOINT_WORK=%CD%

rem Private data base
set MSC_VCJOINT_PDB=%CD%

del  %CD%\aview*.cmd

rem Copy aviewAS.cmd and dll to working directory
copy %MSC_VCJOINT_SRC%\qs_aviewAS.cmd %MSC_VCJOINT_WORK%\aviewBS.cmd

copy %MSC_VCJOINT_SRC%\bin\ball_joint\win64\%ver%\cvj_vlpt.dll %MSC_VCJOINT_WORK%
copy %MSC_VCJOINT_SRC%\bin\tripode_joint\win64\%ver%\*.dll %MSC_VCJOINT_WORK%

rem copy %MSC_VCJOINT_SRC%\Vtk\post\*.py %MSC_VCJOINT_WORK%

adams%ver%  aview ru-s b multi_run.cmd e


