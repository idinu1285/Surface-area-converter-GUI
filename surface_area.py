# importing the necessary modules for making GUI app
from tkinter import *
import tkinter.ttk as ttk
import sys

# main function of app
def surface_area_converter():

    surface_area = Tk()   # set instance of tkinter
    surface_area.title('Surface area converter')   # set title of window app
    surface_area.geometry('750x600')   # set window dimension
    surface_area.configure(background = '#80C080') #set background of window app


    # function that ensures the conversion
    # function to be called when button Enter will be pressed
    def enter_measurement(event):

        user_input = float(measure_input.get())

        if selection_box.get() == 'Acre':

            measure_output_label.config(text = 'Square meter')
            measure_output.insert(0, round(user_input * 4046.8564224,6))
            measure_output1_label.config(text = 'Are')
            measure_output1.insert(0, round(user_input * 40.468564224,6))
            measure_output2_label.config(text = 'Hectare')
            measure_output2.insert(0, round(user_input * 0.40468564224,6))
            measure_output3_label.config(text = 'Homestead')
            measure_output3.insert(0, round(user_input * 0.00625,4))
            measure_output4_label.config(text = 'Rood')
            measure_output4.insert(0, round(user_input * 4,4))
            measure_output5_label.config(text = 'Square centimeter')
            measure_output5.insert(0, round(user_input * 40468564.224,4))
            measure_output6_label.config(text = 'Square foot')
            measure_output6.insert(0, round(user_input * 43560,4))
            measure_output7_label.config(text = 'Square inch')
            measure_output7.insert(0, round(user_input * 6272640,4))
            measure_output8_label.config(text = 'Square kilometer')
            measure_output8.insert(0, round(user_input * 0.0040468564224,6))
            measure_output9_label.config(text = 'Square mile')
            measure_output9.insert(0, round(user_input * 0.0015625,6))
            measure_output10_label.config(text = 'Square milimeter')
            measure_output10.insert(0,round(user_input * 4046856422.4,4))
            measure_output11_label.config(text = 'Square rod')
            measure_output11.insert(0,round(user_input * 160,4))
            measure_output12_label.config(text ='Square yard')
            measure_output12.insert(0, round(user_input * 4840,4))
            measure_output13_label.config(text = 'Township')
            measure_output13.insert(0, round(user_input * 4.34027778 * pow(10,-5),6))


        elif selection_box.get() == 'Square meter':

            measure_output_label.config(text = 'Acre')
            measure_output.insert(0, round(user_input * 0.0002471053814672,6))
            measure_output1_label.config(text = 'Are')
            measure_output1.insert(0, round(user_input * 0.01,4))
            measure_output2_label.config(text = 'Hectare')
            measure_output2.insert(0, round(user_input * pow(10,-4),6))
            measure_output3_label.config(text = 'Homestead')
            measure_output3.insert(0, round(user_input * 1.54440863417 * pow(10,-6),8))
            measure_output4_label.config(text = 'Rood')
            measure_output4.insert(0, round(user_input * 9.884215258687 * pow(10,-4),6))
            measure_output5_label.config(text = 'Square centimeter')
            measure_output5.insert(0, round(user_input * pow(10,4),4))
            measure_output6_label.config(text = 'Square foot')
            measure_output6.insert(0, round(user_input * 10.76391041671 ,6))
            measure_output7_label.config(text = 'Square inch')
            measure_output7.insert(0, round(user_input * 1550.003100006,6))
            measure_output8_label.config(text = 'Square kilometer')
            measure_output8.insert(0, round(user_input * pow(10,-6),8))
            measure_output9_label.config(text = 'Square mile')
            measure_output9.insert(0, round(user_input * 3.86102159 * pow(10,-7),10))
            measure_output10_label.config(text = 'Square milimeter')
            measure_output10.insert(0,round(user_input * pow(10,6),4))
            measure_output11_label.config(text = 'Square rod')
            measure_output11.insert(0,round(user_input * 0.03953686103475 ,6))
            measure_output12_label.config(text ='Square yard')
            measure_output12.insert(0, round(user_input * 1.195990046301,6))
            measure_output13_label.config(text = 'Township')
            measure_output13.insert(0, round(user_input * 1.072506 * pow(10,-8),10))


        elif selection_box.get() == 'Are': 

            measure_output_label.config(text = 'Square meter')
            measure_output.insert(0, round(user_input * 100,4))
            measure_output1_label.config(text = 'Acre')
            measure_output1.insert(0, round(user_input * 0.02471053814672,6))
            measure_output2_label.config(text = 'Hectare')
            measure_output2.insert(0, round(user_input * 0.01,4))
            measure_output3_label.config(text = 'Homestead')
            measure_output3.insert(0, round(user_input * 1.54440863417 * pow(10,-4),4))
            measure_output4_label.config(text = 'Rood')
            measure_output4.insert(0, round(user_input * 0.09884215258687,6))
            measure_output5_label.config(text = 'Square centimeter')
            measure_output5.insert(0, round(user_input * pow(10,6),4))
            measure_output6_label.config(text = 'Square foot')
            measure_output6.insert(0, round(user_input * 1076.391041671,6))
            measure_output7_label.config(text = 'Square inch')
            measure_output7.insert(0, round(user_input * 155.000310001 * pow(10,3),6))
            measure_output8_label.config(text = 'Square kilometer')
            measure_output8.insert(0, round(user_input * pow(10,-4),6))
            measure_output9_label.config(text = 'Square mile')
            measure_output9.insert(0, round(user_input * 3.86102159 * pow(10,-5),8))
            measure_output10_label.config(text = 'Square milimeter')
            measure_output10.insert(0,round(user_input * pow(10,8),4))
            measure_output11_label.config(text = 'Square rod')
            measure_output11.insert(0,round(user_input * 3.953686103475,6))
            measure_output12_label.config(text ='Square yard')
            measure_output12.insert(0, round(user_input * 119.5990046301,6))
            measure_output13_label.config(text = 'Township')
            measure_output13.insert(0, round(user_input * 1.072506 * pow(10,-6),8))


        elif selection_box.get() == 'Hectare':

            measure_output_label.config(text = 'Square meter')
            measure_output.insert(0, round(user_input * pow(10,4),4))
            measure_output1_label.config(text = 'Are')
            measure_output1.insert(0, round(user_input * 100,4))
            measure_output2_label.config(text = 'Acre')
            measure_output2.insert(0, round(user_input * 2.471053814672,6))
            measure_output3_label.config(text = 'Homestead')
            measure_output3.insert(0, round(user_input * 0.0154440863417,6))
            measure_output4_label.config(text = 'Rood')
            measure_output4.insert(0, round(user_input * 9.884215258687,6))
            measure_output5_label.config(text = 'Square centimeter')
            measure_output5.insert(0, round(user_input * pow(10,8),4))
            measure_output6_label.config(text = 'Square foot')
            measure_output6.insert(0, round(user_input * 107639.1041671,6))
            measure_output7_label.config(text = 'Square inch')
            measure_output7.insert(0, round(user_input * 155.000310001 * pow(10,5),6))
            measure_output8_label.config(text = 'Square kilometer')
            measure_output8.insert(0, round(user_input * 0.01,4))
            measure_output9_label.config(text = 'Square mile')
            measure_output9.insert(0, round(user_input * 3.861021585424 * pow(10,-3),8))
            measure_output10_label.config(text = 'Square milimeter')
            measure_output10.insert(0,round(user_input * pow(10,10),4))
            measure_output11_label.config(text = 'Square rod')
            measure_output11.insert(0,round(user_input * 395.3686103475,6))
            measure_output12_label.config(text ='Square yard')
            measure_output12.insert(0, round(user_input * 11959.90046301,6))
            measure_output13_label.config(text = 'Township')
            measure_output13.insert(0, round(user_input * 1.072506 * pow(10,-4),8))


        elif selection_box.get() == 'Homestead':

            measure_output_label.config(text = 'Square meter')
            measure_output.insert(0, round(user_input * 647497.027584,6))
            measure_output1_label.config(text = 'Are')
            measure_output1.insert(0, round(user_input * 6474.97027584,6))
            measure_output2_label.config(text = 'Acre')
            measure_output2.insert(0, round(user_input * 160,4))
            measure_output3_label.config(text = 'Hectare')
            measure_output3.insert(0, round(user_input * 64.7497027584,6))
            measure_output4_label.config(text = 'Rood')
            measure_output4.insert(0, round(user_input * 640,4))
            measure_output5_label.config(text = 'Square centimeter')
            measure_output5.insert(0, round(user_input * 6474970275.84,4))
            measure_output6_label.config(text = 'Square foot')
            measure_output6.insert(0, round(user_input * 6969600,4))
            measure_output7_label.config(text = 'Square inch')
            measure_output7.insert(0, round(user_input * 1003622400,4))
            measure_output8_label.config(text = 'Square kilometer')
            measure_output8.insert(0, round(user_input * 0.647497027584,6))
            measure_output9_label.config(text = 'Square mile')
            measure_output9.insert(0, round(user_input * 0.25 ,4))
            measure_output10_label.config(text = 'Square milimeter')
            measure_output10.insert(0,round(user_input * 647497027584,4))
            measure_output11_label.config(text = 'Square rod')
            measure_output11.insert(0,round(user_input * 25600,6))
            measure_output12_label.config(text ='Square yard')
            measure_output12.insert(0, round(user_input * 774400,6))
            measure_output13_label.config(text = 'Township')
            measure_output13.insert(0, round(user_input * 6.944444444444 * pow(10,-3),6))


        elif selection_box.get() == 'Rood':

            measure_output_label.config(text = 'Square meter')
            measure_output.insert(0, round(user_input * 1011.7141056,6))
            measure_output1_label.config(text = 'Are')
            measure_output1.insert(0, round(user_input * 10.117141056,6))
            measure_output2_label.config(text = 'Acre')
            measure_output2.insert(0, round(user_input * 0.25,4))
            measure_output3_label.config(text = 'Hectare')
            measure_output3.insert(0, round(user_input * 0.10117141056,6))
            measure_output4_label.config(text = 'Homestead')
            measure_output4.insert(0, round(user_input * 1.5625 * pow(10,-3),6))
            measure_output5_label.config(text = 'Square centimeter')
            measure_output5.insert(0, round(user_input * 10117141.056,6))
            measure_output6_label.config(text = 'Square foot')
            measure_output6.insert(0, round(user_input * 10890,4))
            measure_output7_label.config(text = 'Square inch')
            measure_output7.insert(0, round(user_input * 1568160,4))
            measure_output8_label.config(text = 'Square kilometer')
            measure_output8.insert(0, round(user_input * 1.0117141056 * pow(10,-3),6))
            measure_output9_label.config(text = 'Square mile')
            measure_output9.insert(0, round(user_input * 3.90625 * pow(10,-4),6))
            measure_output10_label.config(text = 'Square milimeter')
            measure_output10.insert(0,round(user_input * 1011714105.6,4))
            measure_output11_label.config(text = 'Square rod')
            measure_output11.insert(0,round(user_input * 40,4))
            measure_output12_label.config(text ='Square yard')
            measure_output12.insert(0, round(user_input * 1210,4))
            measure_output13_label.config(text = 'Township')
            measure_output13.insert(0, round(user_input * 1.085069444444  * pow(10,-5),6))


        elif selection_box.get() == 'Square centimeter':

            measure_output_label.config(text = 'Square meter')
            measure_output.insert(0, round(user_input * pow(10,-4),4))
            measure_output1_label.config(text = 'Acre')
            measure_output1.insert(0, round(user_input * 2.471053814672 * pow(10,-8),12))
            measure_output2_label.config(text = 'Hectare')
            measure_output2.insert(0, round(user_input * pow(10,-8),10))
            measure_output3_label.config(text = 'Homestead')
            measure_output3.insert(0, round(user_input * 1.54440863417 * pow(10,-10),12))
            measure_output4_label.config(text = 'Rood')
            measure_output4.insert(0, round(user_input * 9.884215258687 * pow(10,-8),12))
            measure_output5_label.config(text = 'Are')
            measure_output5.insert(0, round(user_input * pow(10,-6),10))
            measure_output6_label.config(text = 'Square foot')
            measure_output6.insert(0, round(user_input * 1.076391041671 * pow(10,-3),6))
            measure_output7_label.config(text = 'Square inch')
            measure_output7.insert(0, round(user_input * 0.1550003100006,10))
            measure_output8_label.config(text = 'Square kilometer')
            measure_output8.insert(0, round(user_input * pow(10,-10),12))
            measure_output9_label.config(text = 'Square mile')
            measure_output9.insert(0, round(user_input * 3.86102159 * pow(10,-11),14))
            measure_output10_label.config(text = 'Square milimeter')
            measure_output10.insert(0,round(user_input * pow(10,2),4))
            measure_output11_label.config(text = 'Square rod')
            measure_output11.insert(0,round(user_input * 3.953686103475 * pow(10,-6),8))
            measure_output12_label.config(text ='Square yard')
            measure_output12.insert(0, round(user_input * 1.195990046301 * pow(10,-4),6))
            measure_output13_label.config(text = 'Township')
            measure_output13.insert(0, round(user_input * 1.072506  * pow(10,-12),14))


        elif selection_box.get() == 'Square foot':

            measure_output_label.config(text = 'Square meter')
            measure_output.insert(0, round(user_input * 0.09290304,6))
            measure_output1_label.config(text = 'Acre')
            measure_output1.insert(0, round(user_input * 2.295684113866 * pow(10,-5),7))
            measure_output2_label.config(text = 'Hectare')
            measure_output2.insert(0, round(user_input * 9.290304 * pow(10,-6),8))
            measure_output3_label.config(text = 'Homestead')
            measure_output3.insert(0, round(user_input * 1.434802571166 * pow(10,-7),8))
            measure_output4_label.config(text = 'Rood')
            measure_output4.insert(0, round(user_input * 9.182736455463 * pow(10,-5),6))
            measure_output5_label.config(text = 'Are')
            measure_output5.insert(0, round(user_input * 9.290304 * pow(10,-4),6))
            measure_output6_label.config(text = 'Square centimeter')
            measure_output6.insert(0, round(user_input * 929.0304,6))
            measure_output7_label.config(text = 'Square inch')
            measure_output7.insert(0, round(user_input * 144,4))
            measure_output8_label.config(text = 'Square kilometer')
            measure_output8.insert(0, round(user_input * 9.290304 * pow(10,-8),10))
            measure_output9_label.config(text = 'Square mile')
            measure_output9.insert(0, round(user_input * 3.86102159 * pow(10,-8),10))
            measure_output10_label.config(text = 'Square milimeter')
            measure_output10.insert(0,round(user_input * 92903.04,4))
            measure_output11_label.config(text = 'Square rod')
            measure_output11.insert(0,round(user_input * 3.673094582185  * pow(10,-3),6))
            measure_output12_label.config(text ='Square yard')
            measure_output12.insert(0, round(user_input * 0.1111111111111,6))
            measure_output13_label.config(text = 'Township')
            measure_output13.insert(0, round(user_input * 9.963906744209 * pow(10,-10),12))


        elif selection_box.get() == 'Square inch':

            measure_output_label.config(text = 'Square meter')
            measure_output.insert(0, round(user_input * 6.4516 * pow(10,-3),6))
            measure_output1_label.config(text = 'Acre')
            measure_output1.insert(0, round(user_input * 1.594225079074 * pow(10,-7),10))
            measure_output2_label.config(text = 'Hectare')
            measure_output2.insert(0, round(user_input * 6.4516 * pow(10,-8),10))
            measure_output3_label.config(text = 'Homestead')
            measure_output3.insert(0, round(user_input * 9.96390674421 * pow(10,-10),12))
            measure_output4_label.config(text = 'Rood')
            measure_output4.insert(0, round(user_input * 6.376900316294 * pow(10,-7),10))
            measure_output5_label.config(text = 'Are')
            measure_output5.insert(0, round(user_input * 6.4516 * pow(10,-6),8))
            measure_output6_label.config(text = 'Square centimeter')
            measure_output6.insert(0, round(user_input * 6.4516,6))
            measure_output7_label.config(text = 'Square foot')
            measure_output7.insert(0, round(user_input * 6.944444444445 * pow(10,-3),6))
            measure_output8_label.config(text = 'Square kilometer')
            measure_output8.insert(0, round(user_input * 6.4516 * pow(10,-10),12))
            measure_output9_label.config(text = 'Square mile')
            measure_output9.insert(0, round(user_input * 2.490976686052 * pow(10,-10),12))
            measure_output10_label.config(text = 'Square milimeter')
            measure_output10.insert(0,round(user_input * 645.16,6))
            measure_output11_label.config(text = 'Square rod')
            measure_output11.insert(0,round(user_input * 2.550760126518 * pow(10,-5),8))
            measure_output12_label.config(text ='Square yard')
            measure_output12.insert(0, round(user_input * 7.716049382716 * pow(10,-4),6))
            measure_output13_label.config(text = 'Township')
            measure_output13.insert(0, round(user_input * 6.919379683479 * pow(10,-12),14))

                
        elif selection_box.get() == 'Square kilometer':

            measure_output_label.config(text = 'Square meter')
            measure_output.insert(0, round(user_input * pow(10,6),4))
            measure_output1_label.config(text = 'Acre')
            measure_output1.insert(0, round(user_input * 247.1053814672,6))
            measure_output2_label.config(text = 'Hectare')
            measure_output2.insert(0, round(user_input * 100,4))
            measure_output3_label.config(text = 'Homestead')
            measure_output3.insert(0, round(user_input * 1.54440863417,6))
            measure_output4_label.config(text = 'Rood')
            measure_output4.insert(0, round(user_input * 988.4215258687,6))
            measure_output5_label.config(text = 'Are')
            measure_output5.insert(0, round(user_input * pow(10,5),4))
            measure_output6_label.config(text = 'Square centimeter')
            measure_output6.insert(0, round(user_input * pow(10,10),4))
            measure_output7_label.config(text = 'Square foot')
            measure_output7.insert(0, round(user_input * 10763910.41671,6))
            measure_output8_label.config(text = 'Square inch')
            measure_output8.insert(0, round(user_input * 155.000310001 * pow(10,7),6))
            measure_output9_label.config(text = 'Square mile')
            measure_output9.insert(0, round(user_input * 0.3861021585425,6))
            measure_output10_label.config(text = 'Square milimeter')
            measure_output10.insert(0,round(user_input * pow(10,12),4))
            measure_output11_label.config(text = 'Square rod')
            measure_output11.insert(0,round(user_input * 39536.86103475,6))
            measure_output12_label.config(text ='Square yard')
            measure_output12.insert(0, round(user_input * 1195990.046301,6))
            measure_output13_label.config(text = 'Township')
            measure_output13.insert(0, round(user_input * 1.072505995951  * pow(10,-2),6))


        elif selection_box.get() == 'Square mile':

            measure_output_label.config(text = 'Square meter')
            measure_output.insert(0, round(user_input * 2589988.110336,4))
            measure_output1_label.config(text = 'Acre')
            measure_output1.insert(0, round(user_input * 640,4))
            measure_output2_label.config(text = 'Hectare')
            measure_output2.insert(0, round(user_input * 258.9988110336,6))
            measure_output3_label.config(text = 'Homestead')
            measure_output3.insert(0, round(user_input * 4,4))
            measure_output4_label.config(text = 'Rood')
            measure_output4.insert(0, round(user_input * 2560,4))
            measure_output5_label.config(text = 'Are')
            measure_output5.insert(0, round(user_input * 25899.88110336,4))
            measure_output6_label.config(text = 'Square centimeter')
            measure_output6.insert(0, round(user_input * 25899881103.36,2))
            measure_output7_label.config(text = 'Square foot')
            measure_output7.insert(0, round(user_input * 27878400,2))
            measure_output8_label.config(text = 'Square inch')
            measure_output8.insert(0, round(user_input * 4014489600,4))
            measure_output9_label.config(text = 'Square kilometer')
            measure_output9.insert(0, round(user_input * 2.589988110336,6))
            measure_output10_label.config(text = 'Square milimeter')
            measure_output10.insert(0,round(user_input * 2589988110336,4))
            measure_output11_label.config(text = 'Square rod')
            measure_output11.insert(0,round(user_input * 102400,4))
            measure_output12_label.config(text ='Square yard')
            measure_output12.insert(0, round(user_input * 3097600,4))
            measure_output13_label.config(text = 'Township')
            measure_output13.insert(0, round(user_input * 2.777777777778 * pow(10,-2),6))


        elif selection_box.get() == 'Square milimeter':

            measure_output_label.config(text = 'Square meter')
            measure_output.insert(0, round(user_input * pow(10,-6),6))
            measure_output1_label.config(text = 'Acre')
            measure_output1.insert(0, round(user_input * 2.471053814672 * pow(10,-10),12))
            measure_output2_label.config(text = 'Hectare')
            measure_output2.insert(0, round(user_input * pow(10,-10),12))
            measure_output3_label.config(text = 'Homestead')
            measure_output3.insert(0, round(user_input * 1.54440863417 * pow(10,-12),12))
            measure_output4_label.config(text = 'Rood')
            measure_output4.insert(0, round(user_input * 9.884215258687 * pow(10,-10),12))
            measure_output5_label.config(text = 'Are')
            measure_output5.insert(0, round(user_input * pow(10,-8),10))
            measure_output6_label.config(text = 'Square centimeter')
            measure_output6.insert(0, round(user_input * 0.01,6))
            measure_output7_label.config(text = 'Square foot')
            measure_output7.insert(0, round(user_input * 1.076391041671 * pow(10,-5),8))
            measure_output8_label.config(text = 'Square inch')
            measure_output8.insert(0, round(user_input * 1.550003100006 * pow(10,-3),6))
            measure_output9_label.config(text = 'Square kilometer')
            measure_output9.insert(0, round(user_input * pow(10,-12),12))
            measure_output10_label.config(text = 'Square mile')
            measure_output10.insert(0,round(user_input * 3.861021585425 * pow(10,-13),16))
            measure_output11_label.config(text = 'Square rod')
            measure_output11.insert(0,round(user_input * 3.953686103475 * pow(10,-8),10))
            measure_output12_label.config(text ='Square yard')
            measure_output12.insert(0, round(user_input * 1.1959900463010 * pow(10,-6),8))
            measure_output13_label.config(text = 'Township')
            measure_output13.insert(0, round(user_input * 1.072505995951  * pow(10,-14),16))


        elif selection_box.get() == 'Square rod':

            measure_output_label.config(text = 'Square meter')
            measure_output.insert(0, round(user_input * 25.29285264,6))
            measure_output1_label.config(text = 'Acre')
            measure_output1.insert(0, round(user_input * 6.25 * pow(10,-3),6))
            measure_output2_label.config(text = 'Hectare')
            measure_output2.insert(0, round(user_input * 2.529285264 * pow(10,-3),6))
            measure_output3_label.config(text = 'Homestead')
            measure_output3.insert(0, round(user_input * 3.90625 * pow(10,-5),6))
            measure_output4_label.config(text = 'Rood')
            measure_output4.insert(0, round(user_input * 0.025,6))
            measure_output5_label.config(text = 'Are')
            measure_output5.insert(0, round(user_input * 0.2529285264,6))
            measure_output6_label.config(text = 'Square centimeter')
            measure_output6.insert(0, round(user_input * 252928.5264,6))
            measure_output7_label.config(text = 'Square foot')
            measure_output7.insert(0, round(user_input * 272.25,6))
            measure_output8_label.config(text = 'Square inch')
            measure_output8.insert(0, round(user_input * 39204,4))
            measure_output9_label.config(text = 'Square kilometer')
            measure_output9.insert(0, round(user_input * 2.529285264 * pow(10,-5),8))
            measure_output10_label.config(text = 'Square mile')
            measure_output10.insert(0,round(user_input * 9.765625 * pow(10,-6),8))
            measure_output11_label.config(text = 'Square milimeter')
            measure_output11.insert(0,round(user_input * 25292852.64,6))
            measure_output12_label.config(text ='Square yard')
            measure_output12.insert(0, round(user_input * 30.25,6))
            measure_output13_label.config(text = 'Township')
            measure_output13.insert(0, round(user_input * 2.712673611111 * pow(10,-7),10))


        elif selection_box.get() == 'Square yard':

            measure_output_label.config(text = 'Square meter')
            measure_output.insert(0, round(user_input * 0.83612736,6))
            measure_output1_label.config(text = 'Acre')
            measure_output1.insert(0, round(user_input * 2.066115702479 * pow(10,-4),6))
            measure_output2_label.config(text = 'Hectare')
            measure_output2.insert(0, round(user_input * 8.3612736 * pow(10,-5),6))
            measure_output3_label.config(text = 'Homestead')
            measure_output3.insert(0, round(user_input * 1.29132231405 * pow(10,-6),6))
            measure_output4_label.config(text = 'Rood')
            measure_output4.insert(0, round(user_input * 8.264462809917 * pow(10,-4),6))
            measure_output5_label.config(text = 'Are')
            measure_output5.insert(0, round(user_input * 8.3612736 * pow(10,-3),6))
            measure_output6_label.config(text = 'Square centimeter')
            measure_output6.insert(0, round(user_input * 8361.2736,6))
            measure_output7_label.config(text = 'Square foot')
            measure_output7.insert(0, round(user_input * 9,4))
            measure_output8_label.config(text = 'Square inch')
            measure_output8.insert(0, round(user_input * 1296,4))
            measure_output9_label.config(text = 'Square kilometer')
            measure_output9.insert(0, round(user_input * 8.3612736 * pow(10,-7),10))
            measure_output10_label.config(text = 'Square mile')
            measure_output10.insert(0,round(user_input * 3.228305785124 * pow(10,-7),10))
            measure_output11_label.config(text = 'Square rod')
            measure_output11.insert(0,round(user_input * 3.305785123967  * pow(10,-2),4))
            measure_output12_label.config(text ='Square milimeter')
            measure_output12.insert(0, round(user_input * 836127.36,4))
            measure_output13_label.config(text = 'Township')
            measure_output13.insert(0, round(user_input * 8.967516069788 * pow(10,-9),10))


        elif selection_box.get() == 'Township':

            measure_output_label.config(text = 'Square meter')
            measure_output.insert(0, user_input * 93239571.9721)
            measure_output1_label.config(text = 'Acre')
            measure_output1.insert(0, round(user_input * 23040,2))
            measure_output2_label.config(text = 'Hectare')
            measure_output2.insert(0, round(user_input * 9323.95719721,2))
            measure_output3_label.config(text = 'Homestead')
            measure_output3.insert(0, round(user_input * 144,2))
            measure_output4_label.config(text = 'Rood')
            measure_output4.insert(0, round(user_input * 92160,2))
            measure_output5_label.config(text = 'Are')
            measure_output5.insert(0, user_input * 932395.719721)
            measure_output6_label.config(text = 'Square centimeter')
            measure_output6.insert(0, user_input * 932395719721)
            measure_output7_label.config(text = 'Square foot')
            measure_output7.insert(0, user_input * 1003622400)
            measure_output8_label.config(text = 'Square inch')
            measure_output8.insert(0, user_input * 144521625600)
            measure_output9_label.config(text = 'Square kilometer')
            measure_output9.insert(0, round(user_input * 93.2395719721,2))
            measure_output10_label.config(text = 'Square mile')
            measure_output10.insert(0,round(user_input * 36,4))
            measure_output11_label.config(text = 'Square rod')
            measure_output11.insert(0,user_input * 3686400)
            measure_output12_label.config(text ='Square yard')
            measure_output12.insert(0, user_input * 111513600)
            measure_output13_label.config(text = 'Square milimeter')
            measure_output13.insert(0, user_input * 93239571972100)

    # function with the role of exiting the application
    def exit_app():
        sys.exit()
    
    # function which clear content of text widgets
    def clear():
        measure_input.delete(0,'end')
        measure_output.delete(0,'end')
        measure_output1.delete(0,'end')
        measure_output2.delete(0,'end')
        measure_output3.delete(0,'end')
        measure_output4.delete(0,'end')
        measure_output5.delete(0,'end')
        measure_output6.delete(0,'end')
        measure_output7.delete(0,'end')
        measure_output8.delete(0,'end')
        measure_output9.delete(0,'end')
        measure_output10.delete(0,'end')
        measure_output11.delete(0,'end')
        measure_output12.delete(0,'end')
        measure_output13.delete(0,'end')

    # function which reset the fields of Combobox
    def reset_unit_box():
        selection_box.set('')

    # set Label widgets with title of name app and select unit
    label1 = Label(surface_area, text = 'Surface area converter', bg = '#80C080', fg = 'black', font = ('Arial', 25))
    label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky=W)
   
    label2 = Label(surface_area, text = 'Select unit of measurement', bg = '#80C080', fg = 'black', font = ('Arial', 13))
    label2.grid(row=1, column=0, columnspan=1, padx=5, pady=5, sticky=W)
    
    # set Combobox widget
    box_val = StringVar()
    selection_box = ttk.Combobox(surface_area, textvariable=box_val, width = 15)
    selection_box['values'] = ('Square meter', 'Acre', 'Are', 'Hectare', 'Homestead', 'Rood', 'Square centimeter', 'Square foot', 'Square inch', 'Square kilometer', 'Square mile',
                               'Square milimeter', 'Square rod', 'Square yard', 'Township')
    selection_box.current(0)
    selection_box.grid(row=1, column=1, padx=5, pady=5, sticky=E)
    
    #set input and output fields
    measure_input = Entry(surface_area)
    measure_input.grid(row=1,column=2, padx=10, pady=5, sticky=W)
    measure_input.bind('<Return>', enter_measurement)
    
    measure_output_label = Label(surface_area, text ='', bg = '#80C080', fg = 'black', font = ('Arial', 13))
    measure_output_label.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    measure_output1_label = Label(surface_area, text ='', bg = '#80C080', fg = 'black', font = ('Arial', 13))
    measure_output1_label.grid(row=3, column=1, padx=5, pady=5, sticky=W)
    
    measure_output2_label = Label(surface_area, text ='', bg = '#80C080', fg = 'black', font = ('Arial', 13))
    measure_output2_label.grid(row=4, column=1, padx=5, pady=5, sticky=W)

    measure_output3_label = Label(surface_area, text ='', bg = '#80C080', fg = 'black', font = ('Arial', 13))
    measure_output3_label.grid(row=5, column=1, padx=5, pady=5, sticky=W)

    measure_output4_label = Label(surface_area, text ='', bg = '#80C080', fg = 'black', font = ('Arial', 13))
    measure_output4_label.grid(row=6, column=1, padx=5, pady=5, sticky=W)

    measure_output5_label = Label(surface_area, text ='', bg = '#80C080', fg = 'black', font = ('Arial', 13))
    measure_output5_label.grid(row=7, column=1, padx=5, pady=5, sticky=W)

    measure_output6_label = Label(surface_area, text ='', bg = '#80C080', fg = 'black', font = ('Arial', 13))
    measure_output6_label.grid(row=8, column=1, padx=5, pady=5, sticky=W)

    measure_output7_label = Label(surface_area, text ='', bg = '#80C080', fg = 'black', font = ('Arial', 13))
    measure_output7_label.grid(row=9, column=1, padx=5, pady=5, sticky=W)

    measure_output8_label = Label(surface_area, text ='', bg = '#80C080', fg = 'black', font = ('Arial', 13))
    measure_output8_label.grid(row=10, column=1, padx=5, pady=5, sticky=W)

    measure_output9_label = Label(surface_area, text ='', bg = '#80C080', fg = 'black', font = ('Arial', 13))
    measure_output9_label.grid(row=11, column=1, padx=5, pady=5, sticky=W)

    measure_output10_label = Label(surface_area, text ='', bg = '#80C080', fg = 'black', font = ('Arial', 13))
    measure_output10_label.grid(row=12, column=1, padx=5, pady=5, sticky=W)

    measure_output11_label = Label(surface_area, text ='', bg = '#80C080', fg = 'black', font = ('Arial', 13))
    measure_output11_label.grid(row=13, column=1, padx=5, pady=5, sticky=W)

    measure_output12_label = Label(surface_area, text ='', bg = '#80C080', fg = 'black', font = ('Arial', 13))
    measure_output12_label.grid(row=14, column=1, padx=5, pady=5, sticky=W)

    measure_output13_label = Label(surface_area, text ='', bg = '#80C080', fg = 'black', font = ('Arial', 13))
    measure_output13_label.grid(row=15, column=1, padx=5, pady=5, sticky=W)
    
    measure_output = Entry(surface_area)
    measure_output.grid(row=2, column=2, padx=10, pady=5, sticky=W)

    measure_output1 = Entry(surface_area)
    measure_output1.grid(row=3, column=2, padx=10, pady=5, sticky=W)

    measure_output2 = Entry(surface_area)
    measure_output2.grid(row=4, column=2, padx=10, pady=5, sticky=W)

    measure_output3 = Entry(surface_area)
    measure_output3.grid(row=5, column=2, padx=10, pady=5, sticky=W)

    measure_output4 = Entry(surface_area)
    measure_output4.grid(row=6, column=2, padx=10, pady=5, sticky=W)

    measure_output5 = Entry(surface_area)
    measure_output5.grid(row=7, column=2, padx=10, pady=5, sticky=W)

    measure_output6 = Entry(surface_area)
    measure_output6.grid(row=8, column=2, padx=10, pady=5, sticky=W)

    measure_output7 = Entry(surface_area)
    measure_output7.grid(row=9, column=2, padx=10, pady=5, sticky=W)
    
    measure_output8 = Entry(surface_area)
    measure_output8.grid(row=10, column=2, padx=10, pady=5, sticky=W)

    measure_output9 = Entry(surface_area)
    measure_output9.grid(row=11, column=2, padx=10, pady=5, sticky=W)

    measure_output10 = Entry(surface_area)
    measure_output10.grid(row=12, column=2, padx=10, pady=5, sticky=W)

    measure_output11 = Entry(surface_area)
    measure_output11.grid(row=13, column=2, padx=10, pady=5, sticky=W)

    measure_output12 = Entry(surface_area)
    measure_output12.grid(row=14, column=2, padx=10, pady=5, sticky=W)

    measure_output13 = Entry(surface_area)
    measure_output13.grid(row=15, column=2, padx=10, pady=5, sticky=W)

    # set Button widgets
    button1 = Button(surface_area,text='Exit', command=exit_app, width = 20, bg = 'red').grid(row=1,column=3, sticky=W, padx=50, pady=5)
    button2 = Button(surface_area, text='Clear', command=clear, width = 20, bg = 'green').grid(row=2,column=3,sticky=W, padx=50, pady=5)
    button3 = Button(surface_area, text='Reset Unit Box', command=reset_unit_box, width = 20, bg = 'blue').grid(row=3,column=3,sticky=W, padx=50, pady=5)
    

    surface_area.mainloop()

# call the main function
surface_area_converter()








