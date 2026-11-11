
-------------------------------------------------------------------------------
|                                                                             |
|                  ,                                                          |
|               ***,                    Hexagon                               |
|          ((((((,,,                    -------                               |
|      (((((((((,,,,            *                                             |
|      *((((((,,,,,,          **(                                             |
|      **((((,,,,,,,     ******((       A d a m s   C++   S o l v e r         |
|      ****,,,,,,,,, ********((((       Build:   2024.1.0-003613-9acb412d     |
|      ***  ,,,,,(((********(((((       Version: Adams 2024.1                 |
|      *.   **((((((******(((((((                                             |
|      ********(((((*****((((((((                                             |
|               ,,,,   .,,,,,,,                                               |
|                 ,,  ,,,,              http://www.hexagon.com                |
|                  , ,                                                        |
|                   ,                                                         |
|                                                                             |
|    *********************************************************************    |
|    *                                                                   *    |
|    *              Hexagon Manufacturing Intelligence, Inc.             *    |
|    *                                                                   *    |
|    *                             A d a m s                             *    |
|    *                                                                   *    |
|    *          Automatic Dynamic Analysis of Mechanical Systems         *    |
|    *                                                                   *    |
|    *********************************************************************    |
|    *                                                                   *    |
|    *                         LEGAL INFORMATION                         *    |
|    *                                                                   *    |
|    *  Warning:  This computer  program is protected  by copyright law  *    |
|    *  and  international  treaties.    Unauthorized  reproduction  or  *    |
|    *  distribution  of this  computer program, or any  portion of it,  *    |
|    *  may result in severe civil and criminal penalties.               *    |
|    *                                                                   *    |
|    *  Copyright (C) 2024 Hexagon AB and/or its subsidiaries.           *    |
|    *                        All rights reserved.                       *    |
|    *                                                                   *    |
|    *********************************************************************    |
|                                                                             |
|-----------------------------------------------------------------------------|
|                                                                             |
|    *********************************************************************    |
|    *                                                                   *    |
|    *   Local Time: 2026-01-12 06:32:44                                 *    |
|    *    Host Name: viper144                                            *    |
|    *        Uname: MS Windows NT                                       *    |
|    *      OS Info: 6.2                                                 *    |
|    *         User: vtkprod.viper                                       *    |
|    *  Customer ID: 5694C154-A915CE72                                   *    |
|    *  Current dir: (See below)                                         *    |
|    *   Process ID: 10364                                               *    |
|    *                                                                   *    |
|    *********************************************************************    |
|                                                                             |
-------------------------------------------------------------------------------

 Current dir:
    D:\HPCscratch\jesus.abenojar\MRB_016cccc_12063151jesusabenojar__AVZwFQ_HPC8714


---- START: WARNING ----
  OS-environment variable
  MDI_ADAMS_CONTACT_OUT=OFF
  Enforces Adams Solver (C++) to controls the export of intermediate contact events in data for a contact model.
  Options are ON, OFF.
---- END: WARNING ----


 command: FILE/MODEL=CV_Joint.adm, OUTPUT_PREFIX=a016cccc_t2600a200d 
The number of parallel threads has been set to 8.


  The model has CONTACT elements, switching to the MODIFIED corrector.


---- START: WARNING ----
Zero area triangle(s) found.
Shell has 438933 total triangles.
Zero area triangle(s) follow.

     FILE = CV_Joint.x_t
     PART = aar.oroller_1
  ELEMENT = SOLID1

---- END: WARNING ----


---- START: WARNING ----
  Triangle(15667): 
    Vertex(5522):           -5.2416           18.5962            5.9017
    Vertex(5521):           -5.2516           18.5934            5.9017
    Vertex(5520):           -5.2566            18.592            5.9017
---- END: WARNING ----


---- START: WARNING ----
----
Warning!  Some triangles have zero area!
----

---- END: WARNING ----


---- START: WARNING ----
Zero area triangle(s) found.
Shell has 438933 total triangles.
Zero area triangle(s) follow.

     FILE = CV_Joint.x_t
     PART = aar.oroller_2
  ELEMENT = SOLID2

---- END: WARNING ----


---- START: WARNING ----
  Triangle(15667): 
    Vertex(5522):           -5.2416           18.5962            5.9017
    Vertex(5521):           -5.2516           18.5934            5.9017
    Vertex(5520):           -5.2566            18.592            5.9017
---- END: WARNING ----


---- START: WARNING ----
----
Warning!  Some triangles have zero area!
----

---- END: WARNING ----


---- START: WARNING ----
Zero area triangle(s) found.
Shell has 438933 total triangles.
Zero area triangle(s) follow.

     FILE = CV_Joint.x_t
     PART = aar.oroller_3
  ELEMENT = SOLID3

---- END: WARNING ----


---- START: WARNING ----
  Triangle(15667): 
    Vertex(5522):           -5.2416           18.5962            5.9017
    Vertex(5521):           -5.2516           18.5934            5.9017
    Vertex(5520):           -5.2566            18.592            5.9017
---- END: WARNING ----


---- START: WARNING ----
----
Warning!  Some triangles have zero area!
----

---- END: WARNING ----


-------------------------------------------------------------------------------
|                                 Model Title                                 |
|=============================================================================|
|                                                                             |
|                       Adams View model name: CV_Joint                       |
|                                                                             |
-------------------------------------------------------------------------------

 command: integrator/hht,err=1e-7,corr=modified,hinit=1e-5,hmax=3e-5,patt=t
 command: output/nosep
 command: equi/alim=0.5d,tlim=0.5,maxit=500,stability=1e-1,err=1e-2
 command: accgrav/igrav=0,jgrav=0,kgrav=0
 command: sim/sta


  Begin Static Solution


 STATICS: Original static solver will be used with the Sparse linear solver.

  Static Solution converged in 58 iterations
  Residual imbalance is less than 3.74907E-06

  End Static Solution
 command: ACCGRAV/IGRAV=0.0,JGRAV= -9806.65,KGRAV=0.0
 command: sim/ini,disp


  Begin Displacement Initial Conditions


  End Displacement Initial Conditions
 command: SIMULATE/ DYNAMIC,END=2.4,STEPS=2880


  Begin Simulation

  ****** Performing Dynamic Simulation using HHT I3 Integrator ******
   The system is modelled with INDEX-3 DAEs.
   The integrator is HHT, CORRECTOR = modified
   Integration error =    1.000000E-07

   Simulation   Step          Function     Cumulative    Integration   Elapsed 
   Time         Size          Evaluations  Steps Taken   Order         Time    
   ___________  ___________   ___________  ___________   ___________   ________
   0.00000E+00  1.00000E-05            0            0             1      42.81 
   2.40000E-01  3.00000E-05        19372         8934             2       6:14 
   4.80000E-01  2.37952E-05        52626        21778             2      20:35 
   7.20000E-01  1.60530E-05        98582        39400             2      35:28 
   9.60000E-01  1.47624E-05       139051        55225             2      47:45 
   1.20000E+00  2.19022E-05       179070        70633             2      59:25 
   1.44000E+00  1.70835E-05       218228        85746             2    1:10:41 
   1.68000E+00  2.76425E-05       257798       101082             2    1:22:07 
   1.92000E+00  2.24010E-05       297986       116567             2    1:33:19 
   2.16000E+00  1.68983E-05       337080       131658             2    1:44:29 
   2.40000E+00  1.44689E-05       375991       146624             2    1:55:42 

  End Simulation
 command: STOP


Finished -----
Elapsed time = 6943.13s,  CPU time = 17767.16s,  Average CPU load = 255.90%

