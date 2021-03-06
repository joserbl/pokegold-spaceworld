#!/usr/bin/python3

from sys import argv, stdout


char_table = [
	"?", "イ゛", "ヴ", "エ゛", "オ゛", "ガ", "ギ", "グ", "ゲ", "ゴ", "ザ", "ジ", "ズ", "ゼ", "ゾ", "ダ",
	"ヂ", "ヅ", "デ", "ド", "<PLAY_G>", "<0x15>", "<0x16>", "ネ゛", "<JP_18>", "バ", "ビ", "ブ", "ボ", "<NI>", "<TTE>", "<WO>",
	"ィ゛", "あ゛", "<TA!>", "<KOUGEKI>", "<WA>", "<NO>", "が", "ぎ", "ぐ", "げ", "ご", "ざ", "じ", "ず", "ぜ", "ぞ",
	"だ", "ぢ", "づ", "で", "ど", "<ROUTE>", "<WATASHI>", "<KOKO_WA>", "<RED>", "<GREEN>", "ば", "び", "ぶ", "べ", "ぼ", "<ENEMY>",
	"パ", "ピ", "プ", "ポ", "ぱ", "ぴ", "ぷ", "ぺ", "ぽ", "<MOM>", "<GA>", "<_CONT>", "<SCROLL>", "も゜", "<NEXT>", "<LINE>",
	"@", "<PARA>", "<PLAYER>", "<RIVAL>", "#", "<CONT>", "<……>", "<DONE>", "<PROMPT>", "<TARGET>", "<USER>", "<PC>", "<TM>", "<TRAINER>", "<ROCKET>", "<DEXEND>",
	"■", "▲", "☎", "D", "E", "F", "G", "H", "I", "V", "S", "L", "M", ":", "ぃ", "ぅ",
	"「", "」", "『", "』", "・", "<・・・>", "ぁ", "ぇ", "ぉ", "┌", "─", "┐", "│", "└", "┘", " ",
	"ア", "イ", "ウ", "エ", "オ", "カ", "キ", "ク", "ケ", "コ", "サ", "シ", "ス", "セ", "ソ", "タ",
	"チ", "ツ", "テ", "ト", "ナ", "ニ", "ヌ", "ネ", "ノ", "ハ", "ヒ", "フ", "ホ", "マ", "ミ", "ム",
	"メ", "モ", "ヤ", "ユ", "ヨ", "ラ", "ル", "レ", "ロ", "ワ", "ヲ", "ン", "ッ", "ャ", "ュ", "ョ",
	"ィ", "あ", "い", "う", "え", "お", "か", "き", "く", "け", "こ", "さ", "し", "す", "せ", "そ",
	"た", "ち", "つ", "て", "と", "な", "に", "ぬ", "ね", "の", "は", "ひ", "ふ", "へ", "ほ", "ま",
	"み", "む", "め", "も", "や", "ゆ", "よ", "ら", "り", "る", "れ", "ろ", "わ", "を", "ん", "っ",
	"ゃ", "ゅ", "ょ", "ー", "゜", "゛", "？", "！", "。", "ァ", "ゥ", "ェ", "▷", "▶", "▼", "♂",
	"円", "×", ".", "/", "ォ", "♀", "０", "１", "２", "３", "４", "５", "６", "７", "８", "９"
]

if len(argv) != 4:
	print(f"Usage: {argv[0]} path/to/ROM.gb start_offset end_offset\noffsets are in the form bank:address (both hex), and end_offset is *not* included.")
	exit(1)


try:
	start_bank,start_addr = [ int(s, 16) for s in argv[2].split(':') ]
	end_bank,  end_addr   = [ int(s, 16) for s in argv[3].split(':') ]
	if start_bank != 0:
		start_addr += (start_bank - 1) * 0x4000
	if end_bank != 0:
		end_addr   += (end_bank   - 1) * 0x4000
except Error:
	print("Please specify valid offsets (bank:address, both hex)")
	exit(1)


with open(argv[1], "rb") as f:
	f.seek(start_addr)
	
	string = ""
	while start_addr < end_addr:
		string += char_table[ int.from_bytes(f.read(1), "little") ]
		start_addr += 1
	
	stdout.buffer.write( f"db \"{string}\"\n".encode('utf-8') )
