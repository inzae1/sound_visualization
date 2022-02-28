def second_to_time(second, kor=False):
    """
    초단위를 시간으로
    :param second: second
    :param kor: true - ex) 1시간 3분 22초
                false - ex) 1:03:22
    :return:
    """
    h = second // 3600
    s = second - (h * 3600)
    m = s // 60
    ss = s - (m * 60)

    h, s, m, ss = str(int(h)), str(int(s)), str(int(m)), str(round(float(ss), 3))

    while len(ss) < 3:
        ss = ss + '0'
    while len(s) < 2:
        s = '0' + s
    while len(m) < 2:
        m = '0' + m
    while len(h) < 2:
        h = '0' + h

    kor_ss = str(int(float(ss)))

    if kor:
        return h + '시간 ' + m + '분 ' + kor_ss + '초'

    return h + ':' + m + ':' + str(ss)


def time_to_second(time):
    """
    시간을 초단위로
    :param time: h:m:ss
    :return: second
    """
    num = 0
    if time.count(':') == 1:
        m = int(time.split(':')[0])
        s = float(time.split(':')[1])
        num += m * 60
        num += s
    else:
        h = int(time.split(':')[0])
        m = int(time.split(':')[1])
        s = float(time.split(':')[2])
        num += h * 3600
        num += m * 60
        num += s
    return round(num, 3)


if __name__ == '__main__':
    print(second_to_time(3423434.343434))
    print(time_to_second('950:57:14.343'))
