
########################################################
#
# Copyright (c) 2003-2010 by University of Queensland
# Earth Systems Science Computational Center (ESSCC)
# http://www.uq.edu.au/esscc
#
# Primary Business: Queensland, Australia
# Licensed under the Open Software License version 3.0
# http://www.opensource.org/licenses/osl-3.0.php
#
########################################################

__copyright__="""Copyright (c) 2003-2010 by University of Queensland
Earth Systems Science Computational Center (ESSCC)
http://www.uq.edu.au/esscc
Primary Business: Queensland, Australia"""
__license__="""Licensed under the Open Software License version 3.0
http://www.opensource.org/licenses/osl-3.0.php"""
__url__="https://launchpad.net/escript-finley"

"""
test for util operations for reduction operations with tagged data

:remark: use see `test_util`
:var __author__: name of author
:var __copyright__: copyrights
:var __license__: licence agreement
:var __url__: url entry point on documentation
:var __version__: version
:var __date__: date of the version
"""

__author__="Lutz Gross, l.gross@uq.edu.au"

import unittest
import numpy
from esys.escript import *
from test_util_base import Test_util_base

class Test_util_reduction_with_tagged_data(Test_util_base):
   """
   test for reduction operation Lsup,sup,inf with tagged data only
   """
   #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   def test_Lsup_taggedData_rank0(self):
      defval=0.860813503322
      arg=Data(defval,self.functionspace)
      arg.setTaggedValue(1,0.086081350332)
      res=Lsup(arg)
      ref1=0.086081350332
      ref2=0.860813503322
      self.failUnless(isinstance(res,float),"wrong type of result.")
      self.failUnless(abs(res-ref1)<=self.RES_TOL*abs(ref1),"wrong result")
      arg.setTaggedValue(2,defval)
      res=Lsup(arg)
      self.failUnless(abs(res-ref2)<=self.RES_TOL*abs(ref2),"wrong result")
   #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   def test_Lsup_taggedData_rank1(self):
      arg=Data(numpy.array([-0.54932912559284452, 0.29396676960376178]),self.functionspace)
      arg.setTaggedValue(1,[0.98025125990414441, -0.070257235982443378])
      res=Lsup(arg)
      ref=0.980251259904
      self.failUnless(isinstance(res,float),"wrong type of result.")
      self.failUnless(abs(res-ref)<=self.RES_TOL*abs(ref),"wrong result")
   #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   def test_Lsup_taggedData_rank2(self):
      arg=Data(numpy.array([[-0.86895475746708128, 0.45103596542916824, 0.89202718384469271, 0.66165880808530297, 0.71929063210904221], [-0.054750345740449236, -0.26270085023397649, -0.44869339310367407, 0.84127602579890803, 0.4084040169910117], [-0.80258081555352101, 0.71946204694435134, -0.97606916814646971, -0.88087380297928397, 0.91540441306863141], [0.53133024472568935, -0.60623654813712635, 0.82280414663810242, 0.64010933901991374, 0.62566314353300356]]),self.functionspace)
      arg.setTaggedValue(1,[[-0.84852153765445437, 0.13244202632711666, -0.64133508534494599, -0.73706953458433633, 0.55834403408867184], [0.27998214461793847, 0.31446145164831063, -0.63410404784852048, 0.2813747329563423, 0.41221195047082393], [-0.79513090436643696, 0.92563876120768263, 0.80602538500705001, 0.21092919617246042, -0.21449414451693616], [0.50885151366468984, -0.53247783698745965, -0.98502684901017235, 0.36104863911630503, -0.68481313205160554]])
      res=Lsup(arg)
      ref=0.98502684901
      self.failUnless(isinstance(res,float),"wrong type of result.")
      self.failUnless(abs(res-ref)<=self.RES_TOL*abs(ref),"wrong result")
   #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   def test_Lsup_taggedData_rank3(self):
      arg=Data(numpy.array([[[-0.0289179522354861, -0.53873332225554216], [-0.87313007813556509, -0.47147149825784584]], [[0.046403579054177468, -0.66499184318911042], [-0.14945300648197457, 0.33023752485562841]], [[0.73609028529612153, 0.62400582710031194], [0.18047782954118574, 0.98299132707347403]], [[0.97452943106570422, -0.80052218344822124], [0.90989474269184356, 0.74467116925414456]], [[-0.40975095375636039, 0.35721815590834538], [-0.023117827122894896, 0.38726163442133732]], [[0.35214474483480052, 0.79626235681759927], [0.072063982160859297, -0.13255981975702369]]]),self.functionspace)
      arg.setTaggedValue(1,[[[0.35540494212277429, -0.40452986468200347], [0.92646378475498059, -0.60976701230157482]], [[-0.17488076275939557, 0.1383489038535719], [0.87222102776136068, 0.05521388649844039]], [[-0.45846974731683399, 0.84645585780786292], [-0.36620222778926448, 0.8758026265447818]], [[0.55804586547774848, -0.19954715807059986], [0.51849302021923482, 0.29871500421422281]], [[0.98995968883285035, -0.78797081527577162], [0.3108075746688399, 0.5474101080348186]], [[-0.74670637823709085, 0.16925394395842575], [-0.76281911656771095, 0.79574461985041189]]])
      res=Lsup(arg)
      ref=0.989959688833
      self.failUnless(isinstance(res,float),"wrong type of result.")
      self.failUnless(abs(res-ref)<=self.RES_TOL*abs(ref),"wrong result")
   #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   def test_Lsup_taggedData_rank4(self):
      arg=Data(numpy.array([[[[-0.17143955149003642, -0.0089504254973518105, 0.53089483578382191, 0.32381408252152899], [-0.77296292864801019, -0.089110721047862773, 0.46285355679515883, 0.62221785170960708], [-0.67474474335134915, 0.34682047265462157, 0.9384448074012548, 0.5682850087388498]], [[0.52652198841191855, 0.52394055634009762, 0.41923325950497858, -0.48507989905455706], [-0.90073796582592069, -0.40217266425438258, -0.60530063652424215, 0.68062718938448441], [-0.59931923693732347, -0.79549982795384744, -0.70714734772804722, -0.46042778371080284]]], [[[0.58538756755140686, 0.98385384505005846, 0.7777811719634411, -0.64306377174574281], [0.72961354558815694, 0.10696472171933968, -0.11372282342784068, 0.87929133681948879], [-0.67126196529672244, -0.64730190047646907, 0.64547629928395711, 0.50361974274373145]], [[0.96265942240931546, -0.20746026072477042, 0.47323657518133921, -0.78443796621025053], [0.61977887181220659, -0.0192018581010025, -0.0016015804221325425, 0.25446656696052594], [0.19964691572203019, -0.44122579240360293, 0.89836148991232134, -0.97914559157737457]]], [[[-0.32474221003830039, 0.50501185871734799, 0.081832847990893409, 0.49226411509256796], [-0.58561709012191865, -0.97753141368900409, 0.50702769958783778, 0.46965610524959978], [0.19394052487354463, 0.32118138849740641, 0.48348630138165749, -0.61570132061285632]], [[0.78997938799317668, 0.48729593728848108, 0.86690961213187001, -0.55317005853484491], [-0.38985400756166189, -0.79197087340853445, 0.150444446088422, 0.30366473850354492], [0.16673919050825758, -0.28616432413953641, -0.49042930009947883, -0.80964116966434485]]]]),self.functionspace)
      arg.setTaggedValue(1,[[[[-0.72676590268291097, 0.98420782971554899, -0.58004995296952444, 0.37649505647780179], [-0.36963117451708949, -0.38478644500667469, 0.1606599749645139, 0.26146427896482427], [-0.99755391430668583, 0.96243322443760793, -0.34748898506056713, 0.28223401802658166]], [[0.41892282572460227, -0.068327589700850844, -0.92249969532644394, -0.2927104302765704], [0.63237889769391709, -0.61446924102341649, -0.9271255632289408, 0.72693928120951368], [-0.099138333893530106, -0.93278471458000989, 0.16805036953472618, 0.13406769552186848]]], [[[0.1322308020971239, -0.15094779056740282, 0.48419178200868274, -0.90259173990902308], [0.088806733010250438, -0.44134645109664827, 0.50169033175317468, -0.16413576472992863], [0.10447947060273766, 0.59946651445651744, -0.28648625172498821, -0.26114646276357711]], [[-0.17647875332717788, -0.95243401465773969, 0.066994364736289391, 0.76072295812282875], [-0.29974152935779652, -0.87018574916912828, -0.40027227651920905, -0.27566894336852044], [-0.87505794257603342, 0.53786153286888583, -0.23579951775243324, 0.29461110217796826]]], [[[-0.031292782596848978, 0.19001451946176351, 0.51137483078731094, 0.35855090738394124], [-0.62796181019314523, -0.017622867812650655, -0.20994152673731148, 0.21972116995451207], [-0.53419638828850147, 0.61964526276926013, 0.83633801914948402, -0.22627427949817003]], [[-0.25275677187826617, 0.92174213140825789, 0.29387486254521544, 0.2851840648022741], [0.99521823294639589, 0.30976825827796484, 0.39585066725930163, -0.037512976967312373], [-0.0098417329760405181, -0.72834591016301697, -0.2368701950529164, -0.075161686057492183]]]])
      res=Lsup(arg)
      ref=0.997553914307
      self.failUnless(isinstance(res,float),"wrong type of result.")
      self.failUnless(abs(res-ref)<=self.RES_TOL*abs(ref),"wrong result")
   #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   def test_inf_taggedData_rank0(self):
      arg=Data(0.162086575852,self.functionspace)
      arg.setTaggedValue(1,0.162086575852)
      res=inf(arg)
      ref=0.162086575852
      self.failUnless(isinstance(res,float),"wrong type of result.")
      self.failUnless(abs(res-ref)<=self.RES_TOL*abs(ref),"wrong result")
   #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   def test_inf_taggedData_rank1(self):
      arg=Data(numpy.array([0.97502548554439095, 0.14468929449768342]),self.functionspace)
      arg.setTaggedValue(1,[-0.80902425002058509, -0.89805781018804365])
      res=inf(arg)
      ref=-0.898057810188
      self.failUnless(isinstance(res,float),"wrong type of result.")
      self.failUnless(abs(res-ref)<=self.RES_TOL*abs(ref),"wrong result")
   #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   def test_inf_taggedData_rank2(self):
      arg=Data(numpy.array([[-0.5694816711808135, 0.80659676528259427, 0.30198257784452243, -0.056794149786052461, 0.28747138649972137], [-0.55351234371619573, -0.7889070920065997, 0.88098536867480282, 0.18532519445126572, 0.4953885498039805], [0.034981671345569287, 0.32837659010563613, -0.12027778324017335, 0.6186028529626495, 0.94436199061580317], [-0.32534943311134756, 0.54392552535517247, -0.07184818553543626, -0.32050443715783694, -0.85778834873938736]]),self.functionspace)
      arg.setTaggedValue(1,[[-0.39066692582632312, 0.56443807842368665, 0.50983381732205602, 0.8533352755557535, 0.26857966396123456], [-0.43675811505896145, 0.061780174738994775, -0.70572251236028349, 0.58277425693964768, -0.77149002637252218], [0.21410554898576928, 0.63314655619690563, 0.83857171132417307, -0.64841751958506944, 0.49689361559212686], [-0.77395862547728433, -0.49190916492680103, -0.96727611195835639, 0.75749173365014144, 0.31952116010595022]])
      res=inf(arg)
      ref=-0.967276111958
      self.failUnless(isinstance(res,float),"wrong type of result.")
      self.failUnless(abs(res-ref)<=self.RES_TOL*abs(ref),"wrong result")
   #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   def test_inf_taggedData_rank3(self):
      arg=Data(numpy.array([[[-0.42552857556236279, -0.35412978699074116], [0.32347364437155268, -0.06660424254888464]], [[0.69470606979783533, -0.27025063802848237], [0.60488222118615087, 0.75136007820911765]], [[-0.18334541260777715, 0.46826845351595714], [0.50971438744602593, -0.75173109388533477]], [[-0.83925390214063711, 0.10222838155029201], [0.97240290055902889, 0.61070698842426729]], [[-0.096661305892300042, 0.3060232400934193], [0.44355296215710527, -0.42328090263660423]], [[-0.37229736098865907, -0.61446651581066591], [-0.59861049707188863, -0.083231793539160881]]]),self.functionspace)
      arg.setTaggedValue(1,[[[0.098193175227128116, 0.70584535076979682], [0.64798160196689181, -0.4003221305355702]], [[-0.04270365807543719, -0.81717683614201619], [-0.40362171906510702, -0.64589178916948042]], [[-0.34373454409447479, -0.77185875470824516], [-0.0065539211815313081, 0.83912029516917275]], [[0.50979364877951405, 0.43268906334074786], [0.97762994631388556, 0.097902836960438]], [[0.25841131938252593, -0.075670175812033058], [-0.57350008458063262, -0.54227522655426319]], [[0.023586725726449931, 0.51624902917426008], [-0.88765839495000032, 0.61903659822536805]]])
      res=inf(arg)
      ref=-0.88765839495
      self.failUnless(isinstance(res,float),"wrong type of result.")
      self.failUnless(abs(res-ref)<=self.RES_TOL*abs(ref),"wrong result")
   #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   def test_inf_taggedData_rank4(self):
      defval=numpy.array([[[[-0.28454409743308506, -0.5668179780431859, 0.94184808892377703, 0.92323038327044005], [-0.62255144042695854, 0.10076051065495695, -0.75730451262334242, 0.92747176366592243], [-0.27419623999345366, -0.2073834606691658, -0.80951479323876696, 0.7135757150367612]], [[-0.97314628579045248, 0.68637741632500915, 0.53335906255833199, 0.96086938773033026], [-0.94945339539011386, -0.81392220879720334, -0.85288194032365472, -0.16477859877633083], [-0.21874528606061738, 0.02516499720401133, -0.049189220512075194, 0.037621105958556278]]], [[[-0.047849568456701519, 0.17313004158353174, -0.73652898602638794, 0.54596512107217787], [0.53827755889057149, 0.82310276090363499, -0.28442357567638377, -0.27179900237071242], [-0.19399624326093612, -0.12349387443529247, -0.56735519289734504, -0.68464632829023375]], [[0.33637651162122606, 0.22878413048564927, -0.70679532991608829, -0.25607454879877101], [-0.29261869752827607, -0.210849838585774, -0.15002781188439474, -0.40403456108229485], [0.98194953410530106, -0.10120885200799257, -0.73197515875287644, -0.79609802011910569]]], [[[-0.25327135865022421, -0.57325273532977317, 0.81059261361542845, -0.046095046141370499], [0.96531384124283903, -0.61153728454098477, -0.97457818352675707, -0.62195519514120923], [0.69039154876488285, 0.92574092049825851, -0.16814749709359544, -0.10824422727782279]], [[-0.54851863859404215, -0.6147932835008143, -0.12084391085229162, 0.57476183090130717], [0.23951711064034398, -0.54814262685597792, 0.94406155895646182, 0.5501815266421175], [0.21626599181010975, -0.9661525769220054, 0.85862231711120418, 0.97115736784479956]]]])
      arg=Data(defval,self.functionspace)
      arg.setTaggedValue(1,[[[[-0.44268265295180487, -0.94661739524160704, -0.58229956703493468, -0.83249621866194934], [-0.68913939538381319, -0.75804956419646286, 0.64749957799330526, 0.32616508244527531], [-0.14277223200775602, 0.74824266545401041, -0.75701815640062908, 0.27359871030382887]], [[-0.48033424095007193, -0.067929127807738965, 0.45865972622825102, -0.21732884173055611], [-0.84531291000880504, 0.83240578985878577, -0.25004340292634253, 0.21302689907942329], [0.46335645072330633, -0.10408082112144545, 0.96768118368872202, -0.14088569164618203]]], [[[0.28258575728428736, -0.45763983811002018, -0.29020353090870232, -0.35290974430439914], [0.8698073989711228, 0.99501431931359741, 0.36030715281910175, -0.27073779707934853], [-0.86095060819411717, -0.85818974539956372, 0.88449786126964258, -0.4780560878654454]], [[-0.12884556589949114, 0.46614981239408104, -0.82753211385973646, 0.71952728123859067], [-0.43573431868291923, 0.41690370693945611, -0.024901756894041061, 0.14934111352857715], [0.78047901800597619, 0.26373552686712709, -0.95380580583786689, 0.63288455897048768]]], [[[-0.94242811017558603, -0.2101877288188847, 0.91797691709730911, 0.45617540058153594], [-0.93413158750269942, -0.70238302965184563, 0.36501953522261488, -0.43956770565509551], [-0.056597755835613439, 0.41357120112496037, -0.60521324615373961, -0.2181851605833629]], [[-0.21130451442872822, 0.53289932629760295, -0.72866050065430343, -0.90245795340674695], [0.1171412044571345, -0.91170721460310178, 0.58826690518723557, -0.39254304440341792], [-0.60338068872893746, -0.40393966609543219, -0.69793709205007581, -0.50271106301761193]]]])
      res=inf(arg)
      ref1=-0.953805805838	# There is a lower value in default but the tags in use prevent it being processed
      ref2=-0.974578183527
      self.failUnless(isinstance(res,float),"wrong type of result.")
      self.failUnless(abs(res-ref1)<=self.RES_TOL*abs(ref1),"wrong result")
      arg.setTaggedValue(2,defval)
      res=inf(arg)
      self.failUnless(abs(res-ref2)<=self.RES_TOL*abs(ref2),"wrong result")
   #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   def test_sup_taggedData_rank0(self):
      arg=Data(0.649634736435,self.functionspace)
      arg.setTaggedValue(1,0.649634736435)
      res=sup(arg)
      ref=0.649634736435
      self.failUnless(isinstance(res,float),"wrong type of result.")
      self.failUnless(abs(res-ref)<=self.RES_TOL*abs(ref),"wrong result")
   #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   def test_sup_taggedData_rank1(self):
      arg=Data(numpy.array([-0.91775874675364899, -0.44518660348335226]),self.functionspace)
      arg.setTaggedValue(1,[-0.91030878048996744, -0.36380755471992954])
      res=sup(arg)
      ref=-0.36380755472
      self.failUnless(isinstance(res,float),"wrong type of result.")
      self.failUnless(abs(res-ref)<=self.RES_TOL*abs(ref),"wrong result")
   #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   def test_sup_taggedData_rank2(self):
      arg=Data(numpy.array([[-0.086523811957357255, -0.42774060865319008, 0.35170422393945833, -0.24772487756509576, 0.85056214851195744], [-0.31877386278938702, 0.28773006836605641, 0.44932528141129979, -0.56724416115855569, 0.80633095352264816], [-0.53652434245562564, -0.26697043576159984, -0.88767305488188519, -0.029691195696610828, 0.67899103041623876], [0.92484508322389836, 0.18625473102022339, -0.27285903116359256, 0.63921542460538938, -0.9221199231145456]]),self.functionspace)
      arg.setTaggedValue(1,[[0.65738567253805136, -0.6778218395330815, 0.40806699669092361, 0.34540048412849589, -0.11704616494950493], [0.38512651510421825, 0.74221788961938562, 0.95314896284964967, -0.040871082359481337, 0.73045537711619035], [0.10490367249326416, -0.24457205097868751, 0.23569203929084925, -0.4833470179537227, 0.13727107062761412], [-0.34956075762939753, -0.40510846111177878, -0.60113099618774268, -0.8694743269747125, 0.8300938895447072]])
      res=sup(arg)
      ref=0.95314896285
      self.failUnless(isinstance(res,float),"wrong type of result.")
      self.failUnless(abs(res-ref)<=self.RES_TOL*abs(ref),"wrong result")
   #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   def test_sup_taggedData_rank3(self):
      arg=Data(numpy.array([[[0.50181406381755478, 0.12696291412348604], [0.45580252908683372, -0.69381529096260919]], [[-0.44711719663105876, -0.49939480373343814], [0.49163505815095565, 0.70755602744123269]], [[-0.32952519817455106, -0.56163922933132882], [0.020194551395573912, 0.74013090992747421]], [[-0.13639620097611793, -0.5402749306510144], [-0.71348777995694368, -0.07149424731352183]], [[-0.81298057712035066, -0.12510197890662789], [-0.30874509775629533, -0.58120893128076712]], [[0.86654409796596377, -0.50673775089683915], [-0.12239574780538409, 0.81691821472857717]]]),self.functionspace)
      arg.setTaggedValue(1,[[[-0.57151921079320256, 0.95258628100636189], [-0.77681734612402287, 0.95978727375688866]], [[0.76493561669286803, 0.51125225923442486], [-0.24392383855124655, 0.014944647833669666]], [[-0.93836576145690231, -0.044479851632975853], [-0.30511938835638897, 0.0091738439461943599]], [[0.71921984284603702, -0.22105010374862499], [-0.78589399511594116, -0.8895142672649694]], [[0.6735135460868733, -0.56646772685337399], [0.73605625715117484, -0.68735959525940049]], [[0.38440898374441201, 0.87186026279634277], [-0.59320035048324327, -0.87430848491656854]]])
      res=sup(arg)
      ref=0.959787273757
      self.failUnless(isinstance(res,float),"wrong type of result.")
      self.failUnless(abs(res-ref)<=self.RES_TOL*abs(ref),"wrong result")
   #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   def test_sup_taggedData_rank4(self):
      defval=numpy.array([[[[0.65078702842768221, -0.73900875462993776, -0.65984653996722176, -0.97539191158251093], [0.99720731720088596, -0.19242629799409516, -0.16320360691406655, -0.043083875914333492], [0.59108757025274139, 0.88522336612612706, 0.74088460755604268, 0.80676177752104627]], [[0.82498945289642323, 0.23110039892583623, -0.13089698664065774, -0.400241064232296], [-0.67523171276117, -0.72699269118844501, 0.53208807038398409, -0.49611668096456474], [-0.20482996861953673, 0.83614314521551858, -0.82232394050773272, -0.71904026227092044]]], [[[0.34003140388599551, 0.31905118515154363, 0.51883291903272832, -0.76898011700894209], [-0.00054352334236540401, -0.42459032663080087, 0.72331023817772211, -0.50647033418441123], [0.76195696335445318, -0.22666337528546276, -0.40740135145605061, -0.81651333897992373]], [[-0.9819499586934739, -0.95616911480063527, -0.2900474363658565, -0.16636609538100222], [0.66435123810546681, -0.30523563374854135, -0.21355210817886849, -0.74243246288718034], [0.82105586828161425, -0.93524621329362057, 0.36308161224720026, 0.76840492117538539]]], [[[-0.22872302699935965, 0.047300841535470761, -0.93216772922157576, -0.40541971639813301], [0.22921538079079262, 0.1958937804621288, 0.27198494374967619, 0.55888236453433282], [0.97179646000620856, 0.53691052552944973, -0.13695340427959324, -0.10499588580374764]], [[-0.4821448283439782, -0.96593591454069139, -0.95284453814535297, -0.35311046977499583], [0.4857495870271038, -0.66584818036412852, -0.04957796396188785, 0.28223147859593767], [-0.2171789936962405, -0.016212404435609562, 0.16258357268143042, -0.6781166044152207]]]])
      arg=Data(defval,self.functionspace)
      arg.setTaggedValue(1,[[[[0.80768589260978896, -0.22702941364663487, -0.72896606223385407, 0.11413326357409237], [0.40571664072592251, -0.9311405487001907, 0.80450361552618688, 0.56480640933432991], [-0.33782609968052979, 0.39512515837757123, 0.73591694462004398, 0.24768959674737778]], [[0.56569618270183164, -0.93779341659685, 0.64969642196738708, -0.77336556098096976], [0.41311175212178153, 0.056953746906872826, 0.25300968955971204, -0.35019321925911262], [-0.8863122403302417, -0.89705763853428677, 0.3060047535556778, -0.92592167036041095]]], [[[0.45649019646929379, -0.29843125838513096, -0.20714508244855367, 0.246705639144563], [-0.32477747411703084, 0.30488751585973306, 0.53390827733820756, -0.84339943975046583], [-0.12373671376305295, -0.1640054521913612, -0.87414144472044897, -0.0021211693404443732]], [[0.38273461960506805, 0.70999974995969617, 0.22361687978370237, -0.098549468178965371], [0.81724211804899904, -0.88965787513620009, -0.39375673885748119, 0.69490920308416371], [-0.65400552410197754, -0.82376412930222931, 0.046545365304690778, -0.21012949605343434]]], [[[-0.27643919361415081, -0.44880727610691973, -0.57364607821939151, -0.14013355075911993], [-0.99302452440223621, 0.70400083788517742, 0.29183091261608896, 0.57457780218190213], [0.20084128112884403, 0.98904695078892235, 0.87503585272015294, -0.26131933340055569]], [[0.94633204265993198, -0.73295197510079446, 0.56975658926329098, -0.83390352955122538], [0.2617682886960544, 0.14649180808291562, -0.29972426982703726, -0.015848496464521356], [-0.96680270201151153, -0.79982829582732196, -0.29552300849179347, 0.66620264190912515]]]])
      res=sup(arg)
      ref1=0.989046950789
      ref2=0.997207317201
      self.failUnless(isinstance(res,float),"wrong type of result.")
      self.failUnless(abs(res-ref1)<=self.RES_TOL*abs(ref1),"wrong result")
      arg.setTaggedValue(2,defval);
      res=sup(arg)
      self.failUnless(abs(res-ref2)<=self.RES_TOL*abs(ref2),"wrong result")


   def test_NaN_taggedData_rank4(self):
      defval=numpy.array([[[[0.65078702842768221, -0.73900875462993776, -0.65984653996722176, -0.97539191158251093], [0.99720731720088596, -0.19242629799409516, -0.16320360691406655, -0.043083875914333492], [0.59108757025274139, 0.88522336612612706, 0.74088460755604268, 0.80676177752104627]], [[0.82498945289642323, 0.23110039892583623, -0.13089698664065774, -0.400241064232296], [-0.67523171276117, -0.72699269118844501, 0.53208807038398409, -0.49611668096456474], [-0.20482996861953673, 0.83614314521551858, -0.82232394050773272, -0.71904026227092044]]], [[[0.34003140388599551, 0.31905118515154363, 0.51883291903272832, -0.76898011700894209], [-0.00054352334236540401, -0.42459032663080087, 0.72331023817772211, -0.50647033418441123], [0.76195696335445318, -0.22666337528546276, -0.40740135145605061, -0.81651333897992373]], [[-0.9819499586934739, -0.95616911480063527, -0.2900474363658565, -0.16636609538100222], [0.66435123810546681, -0.30523563374854135, -0.21355210817886849, -0.74243246288718034], [0.82105586828161425, -0.93524621329362057, 0.36308161224720026, 0.76840492117538539]]], [[[-0.22872302699935965, 0.047300841535470761, -0.93216772922157576, -0.40541971639813301], [0.22921538079079262, 0.1958937804621288, 0.27198494374967619, 0.55888236453433282], [0.97179646000620856, 0.53691052552944973, -0.13695340427959324, -0.10499588580374764]], [[-0.4821448283439782, -0.96593591454069139, -0.95284453814535297, -0.35311046977499583], [0.4857495870271038, -0.66584818036412852, -0.04957796396188785, 0.28223147859593767], [-0.2171789936962405, -0.016212404435609562, 0.16258357268143042, -0.6781166044152207]]]])
      arg=Data(defval,self.functionspace)
      arg.setTaggedValue(1,[[[[0.80768589260978896, -0.22702941364663487, -0.72896606223385407, 0.11413326357409237], [0.40571664072592251, -0.9311405487001907, 0.80450361552618688, 0.56480640933432991], [-0.33782609968052979, 0.39512515837757123, 0.73591694462004398, 0.24768959674737778]], [[0.56569618270183164, -0.93779341659685, 0.64969642196738708, -0.77336556098096976], [0.41311175212178153, 0.056953746906872826, 0.25300968955971204, -0.35019321925911262], [-0.8863122403302417, -0.89705763853428677, 0.3060047535556778, -0.92592167036041095]]], [[[0.45649019646929379, -0.29843125838513096, -0.20714508244855367, 0.246705639144563], [-0.32477747411703084, 0.30488751585973306, 0.53390827733820756, -0.84339943975046583], [-0.12373671376305295, -0.1640054521913612, -0.87414144472044897, -0.0021211693404443732]], [[0.38273461960506805, 0.70999974995969617, 0.22361687978370237, -0.098549468178965371], [0.81724211804899904, -0.88965787513620009, -0.39375673885748119, 0.69490920308416371], [-0.65400552410197754, -0.82376412930222931, 0.046545365304690778, -0.21012949605343434]]], [[[-0.27643919361415081, -0.44880727610691973, -0.57364607821939151, -0.14013355075911993], [-0.99302452440223621, 0.70400083788517742, 0.29183091261608896, 0.57457780218190213], [0.20084128112884403, 0.98904695078892235, 0.87503585272015294, -0.26131933340055569]], [[0.94633204265993198, -0.73295197510079446, 0.56975658926329098, -0.83390352955122538], [0.2617682886960544, 0.14649180808291562, -0.29972426982703726, -0.015848496464521356], [-0.96680270201151153, -0.79982829582732196, -0.29552300849179347, 0]]]])
      if getEscriptParamInt('NAN_CHECK')==1:
		arg=1/arg	#will get us an inf
		arg=arg/arg	#will give a NaN in the last position, yes we could have just sqrt(arg) but I wanted last pos
		self.failUnless(numpy.isnan(sup(arg)),"wrong result")
		self.failUnless(numpy.isnan(inf(arg)),"wrong result")
		self.failUnless(numpy.isnan(Lsup(arg)),"wrong result")	