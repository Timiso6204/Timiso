import random
import os
from Cube import *

class Fore_bingo:
    def __init__(self,difficulty,num_range):
        self.player = Cube.create_bingo_board(difficulty,num_range)
        self.difficulty = difficulty
        self.num_range = num_range
        self.numbers = []

    def perform_operation(self,numbers,operator):
        if len(self.numbers) < 2:
            return print("맞춘 숫자가 2개 이상이어야 합니다.")
        else:
            print(self.numbers)
            print('선택된 연산자',operator)
            num1 = int(input('숫자1 : '))
            num2 = int(input('숫자2 : '))
            if num1 not in self.numbers or num2 not in self.numbers:
                print('선택한 숫자에서 고르시오.')
                self.perform_operation(numbers)

        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2 if num1 > num2 else None
        elif operator == "*":
            return num1 * num2
        elif operator == "/":
            return num1 // num2 if num2 != 0 and num1 % num2 == 0 else None
        return None

    def mark_number(self,boards, number):
        for board in boards:
            for row in range(3):
                for col in range(3):
                    if board[row][col] == number:
                        board[row][col] = "X"
                        print(f"숫자 {number}이 빙고판에 적용되었습니다!")
                        self.numbers.append(number)
                        return self.numbers

    def fore_play_game(self):
        os.system('cls')
        print("=== 사칙 빙고 (Rank) ===")

        # 빙고판 생성
        boards = self.player
        Cube.print_board(boards)
        # 게임 진행
        turn = 1
        numbers = []
        while True:
            print(f"=== 턴 {turn} ===")
            # 랜덤 숫자 선택
            choice = int(input('랜덤 숫자 : 1, 사칙 연산 : 2 '))
            os.system('cls')
            if choice == 1:
                rand_num = random.randint(1, self.num_range)
                print(f"랜덤 숫자: {rand_num}")
                numbers = self.mark_number(boards, rand_num)
            elif choice == 2:
                a = ['+','-','*','/']
                operator = random.choice(a)
                num = self.perform_operation(numbers,operator)
                numbers = self.mark_number(boards, num)
            else:
                print('랜덤 숫자와 사칙 연산 중에 고르시오.')
                continue
            # 빙고 체크
            total_bingo = 0
            for board in boards:
                total_bingo += Cube.check_bingo(board)
            turn += 1
            print(f"현재 빙고 개수: {total_bingo}")
            Cube.print_board(boards)
            if Cube.victory(self.difficulty,total_bingo,turn) == 1:
                break