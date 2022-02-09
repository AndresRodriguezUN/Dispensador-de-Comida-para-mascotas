EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 3 4
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
Wire Wire Line
	4700 3550 5000 3550
Wire Wire Line
	5550 3850 5550 4000
$Comp
L Device:C C?
U 1 1 61978843
P 5000 3850
AR Path="/61978843" Ref="C?"  Part="1" 
AR Path="/6195CD58/61978843" Ref="C?"  Part="1" 
AR Path="/6195DD78/61978843" Ref="C1"  Part="1" 
AR Path="/6196A118/61978843" Ref="C6"  Part="1" 
F 0 "C6" H 5115 3896 50  0000 L CNN
F 1 "10uF/16V" H 5115 3805 50  0000 L CNN
F 2 "Capacitor_SMD:C_0805_2012Metric" H 5038 3700 50  0001 C CNN
F 3 "~" H 5000 3850 50  0001 C CNN
	1    5000 3850
	1    0    0    -1  
$EndComp
Wire Wire Line
	5000 3700 5000 3550
Connection ~ 5000 3550
Wire Wire Line
	5000 3550 5250 3550
Wire Wire Line
	5000 4000 5550 4000
Connection ~ 5550 4000
Wire Wire Line
	5550 4000 5550 4100
$Comp
L Device:C C?
U 1 1 6197884F
P 6100 3850
AR Path="/6197884F" Ref="C?"  Part="1" 
AR Path="/6195CD58/6197884F" Ref="C?"  Part="1" 
AR Path="/6195DD78/6197884F" Ref="C2"  Part="1" 
AR Path="/6196A118/6197884F" Ref="C7"  Part="1" 
F 0 "C7" H 6215 3896 50  0000 L CNN
F 1 "47uF/16V" H 6215 3805 50  0000 L CNN
F 2 "Capacitor_SMD:CP_Elec_6.3x5.4" H 6138 3700 50  0001 C CNN
F 3 "~" H 6100 3850 50  0001 C CNN
	1    6100 3850
	1    0    0    -1  
$EndComp
Wire Wire Line
	6100 4000 5550 4000
Wire Wire Line
	6100 3700 6100 3550
Wire Wire Line
	6100 3550 5850 3550
Connection ~ 6100 3550
Wire Wire Line
	6100 3550 6350 3550
Text HLabel 6350 3550 0    50   Input ~ 0
out
Text HLabel 4700 3550 0    50   Input ~ 0
in
$Comp
L Regulator_Linear:NCP1117-3.3_SOT223 U1
U 1 1 61978DF0
P 5550 3550
F 0 "U1" H 5550 3792 50  0000 C CNN
F 1 "NCP1117-3.3_SOT223" H 5550 3701 50  0000 C CNN
F 2 "Package_TO_SOT_SMD:SOT-223-3_TabPin2" H 5550 3750 50  0001 C CNN
F 3 "http://www.onsemi.com/pub_link/Collateral/NCP1117-D.PDF" H 5650 3300 50  0001 C CNN
	1    5550 3550
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0129
U 1 1 61AFBE1E
P 5550 4100
F 0 "#PWR0129" H 5550 3850 50  0001 C CNN
F 1 "GND" H 5555 3927 50  0000 C CNN
F 2 "" H 5550 4100 50  0001 C CNN
F 3 "" H 5550 4100 50  0001 C CNN
	1    5550 4100
	1    0    0    -1  
$EndComp
$EndSCHEMATC
