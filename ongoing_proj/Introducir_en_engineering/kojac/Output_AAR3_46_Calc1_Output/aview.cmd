!
!===============================================================================
!
cv_assembly create  &
   testrig_name = singleJoint  &
   joint_file_name = "016cccc.mod"
!
!===============================================================================
!
 variable modify variable_name=.universal_joint.analysis_settings.number_of_rotations integer=5
!
! Friction 
 var modify variable_name=.CV_Joint.aar.fri_TrunnionToRoller_sta   real=0.070
 var modify variable_name=.CV_Joint.aar.fri_IRollerToORoller_tran  real=0.077
 var modify variable_name=.CV_Joint.aar.PreForceIRoller real=100
!
! Definition for 3D contact postprocessing 
  var set var=.CV_Joint.Contact3D_Export1 string="cfo_ro_tu_1", "tulip",     "dummy_tutr1.rofix_ref", "TuF"
  var set var=.CV_Joint.Contact3D_Export2 string="cfo_ro_tu_1", "oroller_1", "dummy_tutr1.rofix_ref", "ORoF"
  var set var=.CV_Joint.Contact3D_Export2 string="cfo_sp_ro_1", "iroller_1", "iroller_1.ro_ref", "IRo"
  var set var=.CV_Joint.Contact3D_Export3 string="cfo_sp_ro_1", "iroller_1", "dummy_tutr1.rofix_ref", "IRoF"
  var set var=.CV_Joint.Contact3D_Export4 string="cfo_sp_ro_1", "spider",    "dummy_tutr1.rofix_ref", "SpF"
  var set var=.CV_Joint.Contact3D_Export5 string="cfo_ro_tu_1", "tulip",     "tulip.tu_ref",          "Tu"
  var set var=.CV_Joint.Contact3D_Export6 string="cfo_ro_tu_1", "oroller_1", "oroller_1.ro_ref",      "ORo"
  var set var=.CV_Joint.Contact3D_Export7 string="cfo_sp_ro_1", "iroller_1", "iroller_1.ro_ref",      "IRo"
  var set var=.CV_Joint.Contact3D_Export8 string="cfo_sp_ro_1", "spider",    "spider.sp_ref",         "Sp"
!
!===============================================================================
!
!--ACFG 
!
cv_analysis acfg submit  &
   torques=2600.0E+003 &
   angles=20.0,16.0,12.0,8.0,4.0,2.0 &
   rpm=200 &
   modes=Drive &
   articulation_mode=pivot &
   analysis_name=a016cccc
!
!
!==================================
! Close ADAMS/View - DO NOT MODIFY or REMOVE THESE COMMANDS
!
interface win disp win=.gui.main
interface plot window close
undo flush
mdi exit_macro
quit conf=no
