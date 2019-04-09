
# -*- coding: utf-8 -*-

# def find_max_work_time(processor):
#
#     print('I have', processor, 'processor')
#
#     while True:
#
#         works_input = input("input your five works: ")
#
#         works = [int(work) for work in works_input.split()]
#
#         if len(works) == 5:
#             break
#
#     works = sorted(works)
#
#     return max(works[0] + works[1], works[4])

def check_input(num_works):

    """ 입력 조건이 맞는지 확인 """

    print('you can assign only', num_works, 'works')

    while True:

        works_input = input('input your works: ')

        works = [int(work) for work in works_input.split()]

        if len(works) == num_works:

            return works


def add_min_to_second(works):

    """ 가장 작은 2개의 work를 한 개로 합치기 """

    works = sorted(works)

    if len(works) > 1:
        added_work = works[0] + works[1]

        del works[0]
        del works[1]

        works.append(added_work)

        return works

    else:
        return works


def find_total_work_time(works, processor):

    """ 리스트를 줄여 나가면서 작업시간 계산"""

    while len(works) > processor:     # 작업 묶음이 processor보다 크면 가장 짧은 작업 2개 합쳐서 작업 리스트 줄이기

        works = add_min_to_second(works)

    return(max(works))  # 작업 묶음이 processor 수와 같으면 각 processor의 최대 시간이 최종 작업 시간


if __name__ == "__main__":

    processor = 4
    num_works = 5

    works = check_input(num_works)  # 유효한 입력값을 리스트로 변환

    total_work_time = find_total_work_time(works, processor)    # 총 작업 시간 구하기

    print(total_work_time)


