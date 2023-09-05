def numDistinct(num, line):
    num -= 1
    i = 0
    for c in line[num:]:
        if c not in line[i:i+num] and len(set(line[i:i+num])) == num:
            print(i+num + 1)
            break
        i += 1

with open('day6In.txt') as f:
    lines = f.readlines()

    line = lines[0].strip()

    # Part 1
    numDistinct(4, line)
    # Part 2
    numDistinct(14, line)
























# def find_marker(data):

#     counter = 0
#     recent_chars = ""
#     for char in data:
#         counter += 1
#         recent_chars += char
#         if len(recent_chars) > 4:
#             recent_chars = recent_chars[1:]
#         if len(set(recent_chars)) == 4:
#             return counter
#     return -1

# inputTxt = "zcncrcnrrlccmhchssgqsqrsstfffnqfnfsswgwjjcmcnnvjvwjvwvfvnvwwhvvwmwhmwwwhbhhldhdmhhdfdbdfbdblllnfllgslllqhlhfhlhqllncnfnsffwmwzzlglzlwlhwwmvmddpvvbrvrdvrdvdhhzdhdpdzzbgbsssrpsrshrshhbqbgbmmtwwcbcrbbvnvhnncscwcwlcwlwnwswbbnwntthzzdlzdzffvqvdqvvtptdptphpddzzvhzvzwwqgqjjjvsspvspsbsffvpvcvjcvjvrvjjgmjjhrrdhhdvhvttjttzptpssnlnjjlnnhmnndjnjwwtjjtbbfflwfwgwvvpjpwpcwcgglmgmdmnmbbqtqctcwcmwwvmvlmvmdvdvhvlhlzhzttghttnvnjntnqqtmtwwhvhrhfhchqchhdrdllnwnfwfjjmsmmnhhshnhpptstjjpnpzzhmmpssgrsrzsrrffzjjhvjhjcjcpcvpccfnfjnfjfllssrdsdnnmffldldppcctcmtctffprpsrrrfhfmflldccnpppvsswppdgpgjpgpqgpqpjppclcjczcnzzzqvzzwlzzqfzffsqqphqhvqqbcccstsdttwcwcvvmjjhqqmllpglgtgwgnnbnrbnnjdndhhbrbvrvwwwblwwwppmdmttztqzqrqjjpggpmgpmpqqmssvnsvnndnvddtztddrrsnsbbshhqmhqmmdnnrsrllqvvfjfpfqpqfqflqlmqmrrqgrqrrhvvfddfhhfnhnlncnzzwwjwswpsscpchcssrzssjqsqrsswbbzggnqnwqqsrqqzbqbddtffcjjdggwlwnwtnnpddcqddsppcwpcwpphvphhhrprqrqttwgwqwppvdpvvrgggmpmddzvvwwthwtttbqtbbftfrffbdfbbspshphpwhppnhnmhhbbshbsbmbdmmtrmrbrprbprphhnmhmvhmhhqqbvqvqcvcwcbwcchbbgwwqffrcffsvvcczrztrzzdhdmhdmmzbbvlvqqtptpvvfsfppdzppmddfvdfdwdfdmdwwlvvqdvqdqmdqqmnmdndsswsfwfvwfwzzhrzhhwfhhpvhppmssnhsnsnwswvwlwdwzwnwswwmqmjmbbdjdbbtllcpllltqlttnvvppznpnttlrrwlwvllphpbblccgjcggbtbwtwdwrrbnndpddbqqnpnrnnqqshspsggtptztpzzclcggtqtgqttcmmbgbfbdfdfsddlrlvrlvvmqqgbqgbqbcbbnpplqqblqbqmbbbdqbbhjjcgcdgdwdjwjqqlsqqnnwffglfglgnlggjgjtgjtgjtgjjclcwcqqvpvwwvgvhgvhvjjzpzbznnvrrrpbpdbdhhmshsnnnwppcbcvvlldccdggqnqgnqqzbzzcfflnnmppcgcmgmrgmrgmgngwwptpzzpfzpfzpzdppgcgtcgtgccvtctzzdmzmlmzlzwllbplblltgtctrrghgvhgvvfvssngsschshrhvrvddghgwwwwzgwgvgccjdjzjwwvdvvqsqshsvvddmddbllvppmlpmlmwlwppjmppwrrdzrrpmrmrdmrmbmzzwttvwwsfswwlflnlrlvvdllzbztbtpbtppnjpnpdnnjrjsshtssvvsjvjfjwffsszvsvjssqzsslpslppjpspqptbncvzrlwtjvsrwtnzzhwdfsmlthvgqgjrpshpbsrrvnsdbqslbcplnpcjqwmwqsnwdcjsdmccbdglwbrcdcqsfhjqhstvhqqdwltqwhhqcrnpvnzjhhbjvqbqhclwggjqfvnfsvcnjjhbmrvbpjqrbljbtltvnsgdfhddlmsdhcrfwvlvbsdrjwjvtnqzhrlqgjmzsmjlpdjsrjmdhmvgwjmfwtqffnzfrtswrlgvvhhqgpzcjwscfqgjmdhtvbgzdlvzfhgqlqbfwsjrmmhrlcwhrcnwwvngcmsrfgczsfqvvmdtmtprfvjrwrwcqwvgmzcjncrzvcswlzsdszvdtwmptnrhgzqwrhjjtbchhpwsdjnqmnsgzwqzvlzlsznpqgvtqnldjqpvndtsjlzhpzsgthbwvwnlbwjlmndqpcdvjdgdzhctpghlfwrtqtvfwdpgrjbmwzqgthjpmlrsqmzsznddhrbjnggqrdntpbngvldnnltfnmdwfhftjvpqbrzqvdzbzzctshzldtcdgfnczglrrjtwswzdvjrfgwztwznbpplmbgwpcmstcsjtqhmzmzsjwsfbjlbnbdtdsmlpdmrrbhdhpzrjdpzhcwsrgfrhmqzqtjfhpvltnthwjrrrpnsbmmwrhsfqbmnvwhpntltsgwgnqhcvlndfrtrfrnlmbhltmtgzhlzqgtsbbnggdjvbslfbczhpghqqcqlrbtpnbqbflfjrmpmwwvjqgvcqtmfggmptqlqstcmdtqlslnnzwbgnstftfsvsjdrmgbzfnzltwbjmqhsvshnmwhftjdndltdpngzwbrjpgpwmqgfsflnhmtzcmdjmzwrsrrrmpvwgggwrhrwtfwdbgbpmwpcdspdtbqvdwwsnwdtrtdtgnfzzsmlbcqdzbsqnrgtvvnlfcdlcgcnfpqbddqcjfqtmpndmnwvfqgjzrltqvlprmbbhmtwbzjjgfhhhfjswpffmjnsdmrcjrwlwpmfrmhljpphlwwwwmgsjcsrcvmfrdjdhshddshpplzsnsphcmdhvllgmdgrvbvjmtpltdthffsvwwhvgqrhmfjfpdswcqldrhpmznffjsntwrnmnpmsshljszbchctptsdlnbcvpfvtlfnzcrljpdwrsjnlpqcpnwvnqhzhqmjbvlbtgslzthlbbjzsgdglbrltzjdshpfbndjtssvsjqlstnrjdzzjvlpqhmwvrsvndcqrqjjcsqvmvrbhngtcfdprlbnqmhqllddgjpdzbjlphntrtgjrdgtbslrtzczbnnlddzzsvqvqvvzjpjqfhztgtsfggdppfdhzsbjzqjmpnmgqzlsdhjjbfpbsbnzpmhwrzjqhczrgcsflfwtrgwbnbrshjpwltntsnsdhmhqlmzdprcrcpcpjnphsmjwhzdqtncdbwgspmnfzsgmpbdhmslqchhhbbwfrghhnfjplsvrtbvplgrwdnbnfsgpwrqczvzlnfsngnsnbwvpmfdcmjztdnrllslnwcfwwnwsvztqmgqtfvmdqrrrmwfmphbcvwwttpmwjjbvqrmlwtwfsjdpcbmdlnlzcqntfzzmslshwprjfhwwpbbdfcdjwllfwcznwpjpwrlsfnnbgzjllrgtzcdcvhdhbtlrcvfdvsdjlzsmwwqvpzfhzjlqpfbqstvfrpcchmtwgbrhqqbglrvzmctdlpnvmglgdtzpbdngtfdnmsmwbgjstzbqwqcdlhfrtqqnhqvpfhdrjqvsvstftdgwwnwpfbfbdcfqnqlwpdnfhhfctwrgdqpbpbmgnfsnbpjfctvdtjnsfqlrtctrnjgltndngcmrdphhsqpjhprbngjzqqhnhhrdwlwwpmhzwshvrtzfgzlrhwghvpvfprbbvflltplpptvrmwcrdqndfqbfqtlqqwvphsmcvnbzghvsptrphhfcgdsslhfbcwhtjcmnpbvqrfgpsjgqpnnwwhjjwqrhhqgznwdzjqbtmmjljjwctqtfgwqbdrjwqwbbcftvjwfdfrgvsrlcrccpvfzdrcjvqfbhddpvrrhjrmhdgchrghbzsqpmgnmslfctblwlvphdfpvtdtwpdfsjwssmgnsvsqpdbqngccsplhmjbwjwtzwsbjhwpwcslqjdchmbvzrbgnwvjrrrdtvhtlzlrbwthzlhhqzzpvpwbzrrbrbtpwnhldhqqltqrqdddfwdmjzgctnlrjrjwvddfmjpnptdmrvnqjvsjfrmlvlqsthhsbvnjlsdzrjngfnqdjfssmvgrchbwmwbbvfqfhvrtwghmrpddnwbrbvbmqvfzbjdsnbzgrtmsfhmsmjtrqsgmpnwwbfwtp"
# print(find_marker(inputTxt))

# def find_marker(s, marker_length):
#   # Keep track of the last marker_length characters we've seen
#   last_chars = []

#   # Loop over each character in the string
#   for i, c in enumerate(s):
#     # Add the current character to the list of last characters
#     last_chars = last_chars[1:] + [c]

#     # If we've seen marker_length characters and they're all different,
#     # we've found a marker
#     if len(last_chars) == marker_length and len(set(last_chars)) == marker_length:
#       return i - marker_length + 1
  
#   # If we reach here, we haven't found a marker
#   return -1

# marker_length = 14
# position = find_marker(inputTxt, marker_length)
# print(position)
