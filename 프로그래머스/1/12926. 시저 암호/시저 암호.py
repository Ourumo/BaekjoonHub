def solution(s, n):
    lower_a, lower_z, upper_a, upper_z, result = ord("a"), ord("z"), ord("A"), ord("Z"), []
    new_s = list(map(lambda x: ord(x) if not x == " " else " ", list(s)))

    for c in new_s:
        if c == " ":
            result.append(c)
            continue

        tmp_c = c + n
        if lower_a <= c <= lower_z:
            if not lower_a <= tmp_c <= lower_z:
                result.append(chr(lower_a + tmp_c - lower_z - 1))
            else:
                result.append(chr(tmp_c))
        else:
            if not upper_a <= tmp_c <= upper_z:
                result.append(chr(upper_a + tmp_c - upper_z - 1))
            else:
                result.append(chr(tmp_c))

    return "".join(result)