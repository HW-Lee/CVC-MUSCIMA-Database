#
# @authors: Anjan Dutta, Alicia Fornes
# contact:  adutta@cvc.uab.es, afornes@cvc.uab.es
# 
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
#----------------------------------------------------------------


#!/usr/bin/python
# Testscript image deformation with ground truth

import sys
from gamera.core import *
from gamera.toolkits.musicstaves import plugins

# Input file name
infile=sys.argv[1]
# Ground Truth file name
gtfile=sys.argv[2]

# show the input file name
print "-------------------------------------------------"
print infile
print "-------------------------------------------------"

init_gamera()

# Load the input image
im_musc = load_image(infile)
im_musc = im_musc.to_onebit()
im_musc.invert()

# Load the ground truth image
im_gt=load_image(gtfile)
im_gt = im_gt.to_onebit()
im_gt.invert()

infile_tokens = infile.split(".")

only_image_name = infile_tokens[0]

# detect the skew angle of the document
[skew_angle,accuracy]=im_gt.rotation_angle_projections(-5.5,5.5,0)
# rotate both the images simultaneously
[im_musc,im_gt,skellist] = im_musc.rotation(im_gt,-skew_angle)
#-------------------------------------------------------------------------------
# Note: In general, the deformed images will be saved to hard disk.
#
# All deformations must be done simultaneously on the ground truth as well.
#
# Remove ".png" or ".tif" extension for generation of output file names.
#
# Check the parameters for all the deformation cases.
#-------------------------------------------------------------------------------
##1-----White Speckles
[fulldef, staffdef, skellist] = im_musc.white_speckles_parallel(im_gt,0.025,10,2)
fulldef.invert()
staffdef.invert()
fulldef.save_PNG('./'+only_image_name+'-whitespeckles')
staffdef.save_PNG('./'+only_image_name+'-whitespeckles-gt')
##2-----Kanungo Noise
[fulldef, staffdef, skellist] = im_musc.degrade_kanungo_parallel(im_gt,0,1,1,1,1,2)
fulldef.invert()
staffdef.invert()
fulldef.save_PNG('./'+only_image_name+'-kanungo')
staffdef.save_PNG('./'+only_image_name+'-kanungo-gt')
##3-----Rotation
[fulldef, staffdef, skellist] = im_musc.rotation(im_gt,12.5)
fulldef.invert()
staffdef.invert()
fulldef.save_PNG('./'+only_image_name+'-rotated')
staffdef.save_PNG('./'+only_image_name+'-rotated-gt')
##4-----Staffline Interruption
[fulldef, staffdef, skellist] = im_musc.staffline_interruptions(im_gt,0.5,3)
fulldef.invert()
staffdef.invert()
fulldef.save_PNG('./'+only_image_name+'-interrupted')
staffdef.save_PNG('./'+only_image_name+'-interrupted-gt')
##5-----Staffline Thickness Ratio
[fulldef, staffdef, skellist] = im_musc.staffline_thickness_ratio(im_gt,1.0)
fulldef.invert()
staffdef.invert()
fulldef.save_PNG('./'+only_image_name+'-thickness-ratio')
staffdef.save_PNG('./'+only_image_name+'-thickness-ratio-gt')
##6-----Staffline Y Variation version-1
[fulldef, staffdef, skellist] = im_musc.staffline_y_variation(im_gt,5,0.6)
fulldef.invert()
staffdef.invert()
fulldef.save_PNG('./'+only_image_name+'-staffline-y-variation-v1')
staffdef.save_PNG('./'+only_image_name+'-staffline-y-variation-v1-gt')
##7-----Staffline Y Variation version-2
[fulldef, staffdef, skellist] = im_musc.staffline_y_variation(im_gt,5,0.93)
fulldef.invert()
staffdef.invert()
fulldef.save_PNG('./'+only_image_name+'-staffline-y-variation-v2')
staffdef.save_PNG('./'+only_image_name+'-staffline-y-variation-v2-gt')
##8-----Staffline Thickness Variation version 1
[fulldef, staffdef, skellist] = im_musc.staffline_thickness_variation(im_gt,1,6,0.5,0)
fulldef.invert()
staffdef.invert()
fulldef.save_PNG('./'+only_image_name+'staffline-thickness-variation-v1')
staffdef.save_PNG('./'+only_image_name+'-staffline-thickness-variation-v1-gt')
##9-----Staffline Thickness Variation version 2
[fulldef, staffdef, skellist] = im_musc.staffline_thickness_variation(im_gt,1,6,0.93,0)
fulldef.invert()
staffdef.invert()
fulldef.save_PNG('./'+only_image_name+'-staffline-thickness-variation-v2')
staffdef.save_PNG('./'+only_image_name+'-staffline-thickness-variation-v2-gt')
##10----Curvature
[fulldef, staffdef, skellist] = im_musc.curvature(im_gt,0.1,2)
fulldef.invert()
staffdef.invert()
fulldef.save_PNG('./'+only_image_name+'-curvature')
staffdef.save_PNG('./'+only_image_name+'-curvature-gt')
##11----Typeset Emulation
[fulldef, staffdef, skellist] = im_musc.typeset_emulation(im_gt,1,0.5,10,1,False)
fulldef.invert()
staffdef.invert()
fulldef.save_PNG('./'+only_image_name+'-typeset-emulation')
staffdef.save_PNG('./'+only_image_name+'-typeset-emulation-gt')
