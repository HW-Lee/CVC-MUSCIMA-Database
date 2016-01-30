#
# README
#
# @authors: Anjan Dutta, Alicia Fornes
# contact:  adutta@cvc.uab.es, afornes@cvc.uab.es
# 
----------------------------------------------------------------
This folder contains two scripts (staffdeformation.py, do_deformation.py) 
and one music score image and its corresponding ground-truth
----------------------------------------------------------------

******* REQUIREMENTS

Install the "MusicStaves Toolkit for Gamera": 

http://lionel.kr.hs-niederrhein.de/~dalitz/data/projekte/stafflines/

******* staffdeformation.py:

Place this file in the ../gamera/toolkits/musicstaves/plugins/ folder. If it is 
needed replace the older version that is already in the folder.

******* do_deformation.py:

This is a python script which will create the following deformations:

	(1) Curvature

	(2) Interruption

	(3) Whitespeckles

	(4) Rotation

	(5) Thickness variation

	(6) Typeset emulation

	(7) y variation

	(8) Kanungo

	(9) Thickness ratio

Usage: python do_deformation.py <input_file> <ground_truth_file>

	eg: python do_deformation.py p001.png p001-gt.png


*******************************************************************************
IMPORTANT: 
*******************************************************************************

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY.

The code has been designed and tested in Ubuntu Linux version 10.04.
The behaviour of this code in other systems or platforms is unknown.
*******************************************************************************
