!
!-- Build the interface
!
def com echo=off
file comm read &
        file=(getenv("MSC_VCJOINT_SRC")//"/installation/load_header.cmd")

def com echo=on
!-- private data base
!
variable set var=.universal_joint.cv_private_db &
        string=(getenv("MSC_VCJOINT_PDB"))
!
!-- change to working directory
!
variable set var=.universal_joint.cv_working_dir &
        string=(getenv("MSC_VCJOINT_WORK"))

if cond=(!str_is_space(.universal_joint.cv_working_dir))
   var set var=.universal_joint.tmp int=(CHDIR(.universal_joint.cv_working_dir))
   var del var=.universal_joint.tmp
end

color mod color=.colors.background red_component=   0.72 green_component=0.72 blue_component=  0.72 
view man mod view=all back=.colors.background
!
!2016-07-14 AG time stamp out, font size to 6
defaults plt_attributes legend_font_size=6
defaults plt_attributes subtitle_font_size=6
defaults plt_attributes title_font_size = 6
defaults plt_attributes date_note_font_size = 6
defaults plt_attributes table_font_size = 6
defaults plotting axis_numbers_font_size = 6
defaults plotting axis_label_font_size = 6
defaults report   base_font_size = 6
defaults plt_attributes plot_auto_date = off
defaults plt_attributes plot_auto_title = off
defaults plt_attributes plot_auto_subtitle = off
defaults plt_attributes plot_table = no
!
! AL, 2017-02, changed default density for steel to match Creo densitiy
material modify material=.materials.steel density=(7800.0(kg/meter**3))

default force force_scale=0.005 torque_scale=0.1 display_text=no decimal_places=4 display_wireframe=yes always_in_front=yes
