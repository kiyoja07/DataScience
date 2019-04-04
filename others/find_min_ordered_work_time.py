
works_input = input("input your work list: ")

processor = 4
works = sorted([int(work) for work in works_input.split()])


def last_work_for_complted_matrix(index, _matrix,  _list):

    """짝수 리스트는 그대로 추가, 홀수 리스트는 역순해서 추가"""

    if (index // processor) % 2 == 0:

        return _matrix.append(_list)
    else:
        _list = sorted(_list, reverse=True)

        return _matrix.append(_list)


def make_work_matrix_from_works(works):

    work_matrix = []
    work_list = []

    for i, work in enumerate(works):

        if i < len(works) - 1:

            if i % processor == processor - 1:
                work_list.append(work)
                last_work_for_complted_matrix(i, work_matrix, work_list)
                work_list = []

            else:
                work_list.append(work)

        else:
            work_list.append(work)
            last_work_for_complted_matrix(i, work_matrix, work_list)

    return work_matrix

# print(make_work_matrix_from_works(works))
work_matrix = make_work_matrix_from_works(works)

def find_max_work_time(work_matrix):

    total_work_time_list =[]

    if len(works) % processor == 0:

        for pairs in zip(*work_matrix):
            sum = 0
            for i in pairs:
                sum += i
            total_work_time_list.append(sum)

    else:

        before_tail = []

        for pairs in zip(*work_matrix[:-1]):
            sum = 0
            for i in pairs:
                sum += i
            before_tail.append(sum)


        before_tail = sorted(before_tail)
        tail = sorted(work_matrix[-1], reverse=True)
        print(before_tail, tail)

        before_tail_and_tail = []

        before_tail_and_tail.append(before_tail)
        before_tail_and_tail.append(tail)

        for i, _ in enumerate(before_tail):

            try:
                total_work_time = before_tail_and_tail[0][i]+before_tail_and_tail[1][i]
                total_work_time_list.append(total_work_time)

            except:
                total_work_time = before_tail_and_tail[0][i]
                total_work_time_list.append(total_work_time)

    return max(total_work_time_list)


if __name__ == "__main__":

    if len(works) <= processor:
        print(max(works))
    else:
        print(find_max_work_time(work_matrix))


