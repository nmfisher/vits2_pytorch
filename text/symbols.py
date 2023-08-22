""" from https://github.com/keithito/tacotron """

'''
Defines the set of symbols used in text input to the model.
'''
_pad        = '_'
_punctuation = ';:,.!?¡¿—…"«»“” '
_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
_letters_ipa = "ɑɐɒæɓʙβɔɕçɗɖðʤəɘɚɛɜɝɞɟʄɡɠɢʛɦɧħɥʜɨɪʝɭɬɫɮʟɱɯɰŋɳɲɴøɵɸθœɶʘɹɺɾɻʀʁɽʂʃʈʧʉʊʋⱱʌɣɤʍχʎʏʑʐʒʔʡʕʢǀǁǂǃˈˌːˑʼʴʰʱʲʷˠˤ˞↓↑→↗↘'̩'ᵻ"


# Export all symbols:
#symbols = [_pad] + list(_punctuation) + list(_letters) + list(_letters_ipa)


symbols = [_pad] + [" ", 
"!",
"\"",
"'",
",",
".",
"?",
"“",
"”",
"、",
"。",
"《",
"》",
"！",
"，",
"？",
"a1",
"a2",
"a3",
"a4",
"a5",
"AA0",
"AA1",
"AA2",
"AE0",
"AE1",
"AE2",
"AH0",
"AH1",
"AH2",
"ai1",
"ai2",
"ai3",
"ai4",
"an1",
"an2",
"an3",
"an4",
"ang1",
"ang2",
"ang3",
"ang4",
"AO0",
"ao1",
"AO1",
"ao2",
"AO2",
"ao3",
"ao4",
"AW0",
"AW1",
"AW2",
"AY0",
"AY1",
"AY2",
"b",
"B",
"c",
"ch",
"CH",
"d",
"D",
"DH",
"e1",
"e2",
"e3",
"e4",
"e5",
"EH0",
"EH1",
"EH2",
"ei1",
"ei2",
"ei3",
"ei4",
"en1",
"en2",
"en3",
"en4",
"en5",
"eng1",
"eng2",
"eng3",
"eng4",
"ER0",
"ER1",
"ER2",
"EY0",
"EY1",
"EY2",
"f",
"F",
"g",
"G",
"h",
"HH",
"i1",
"i2",
"i3",
"i4",
"i5",
"ia1",
"ia2",
"ia3",
"ia4",
"ian1",
"ian2",
"ian3",
"ian4",
"iang1",
"iang2",
"iang3",
"iang4",
"iao1",
"iao2",
"iao3",
"iao4",
"ie1",
"ie2",
"ie3",
"ie4",
"IH0",
"IH1",
"IH2",
"ii1",
"ii2",
"ii3",
"ii4",
"ii5",
"iii1",
"iii2",
"iii3",
"iii4",
"in1",
"in2",
"in3",
"in4",
"ing1",
"ing2",
"ing3",
"ing4",
"iong1",
"iong2",
"iong3",
"iong4",
"iou1",
"iou2",
"iou3",
"iou4",
"IY0",
"IY1",
"IY2",
"j",
"JH",
"k",
"K",
"l",
"L",
"m",
"M",
"n",
"N",
"NG",
"o1",
"o2",
"o4",
"o5",
"ong1",
"ong2",
"ong3",
"ong4",
"ou1",
"ou2",
"ou3",
"ou4",
"OW0",
"OW1",
"OW2",
"OY1",
"OY2",
"p",
"P",
"q",
"r",
"R",
"rr",
"s",
"S",
"sh",
"SH",
"[SIL]",
"t",
"T",
"TH",
"u1",
"u2",
"u3",
"u4",
"ua1",
"ua2",
"ua3",
"ua4",
"uai1",
"uai2",
"uai3",
"uai4",
"uan1",
"uan2",
"uan3",
"uan4",
"uang1",
"uang2",
"uang3",
"uang4",
"UH0",
"UH1",
"UH2",
"ui1",
"ui2",
"ui3",
"ui4", 
"un1",
"un2",
"un3",
"un4",
"[UNK]",
"uo1",
"uo2",
"uo3",
"uo4",
"UW0",
"UW1",
"UW2",
"V",
"v1",
"v2",
"v3",
"v4",
"van1",
"van2",
"van3",
"van4",
"ve1",
"ve2",
"ve3",
"ve4",
"vn1",
"vn2",
"vn3",
"vn4",
"W",
"x",
"Y",
"z",
"Z",
"zh",
"ZH"]

SPACE_ID = symbols.index(" ")
