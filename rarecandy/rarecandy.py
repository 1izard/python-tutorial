import readline
import os
import random
from enum import Enum
from typing import List


PROBLEM_FILEPATH = 'problem.csv'


def input_int(min_no, max_no) -> int:
    no = min_no - 1
    while no < min_no or max_no < no:
        print('> ', end='')
        input_no_str = input()
        try:
            no = int(input_no_str)
        except ValueError:
            no = min_no - 1
        if no < min_no or max_no < no:
            print(f'{min_no}から{max_no}までの数を入力してください')
    return no


class FrontMenu(Enum):
    PLAY_NORMAL = '通常モードでプレイ'
    PLAY_RANDOM = 'ランダムモードでプレイ'
    REGISATER = '問題を登録する'
    DELETE = '問題を削除する'
    EXIT = '終了'


class RegisterMenu(Enum):
    REGISTER = '選択肢を追加する'
    EXIT = '登録終了'


class DeleteMenu(Enum):
    DELETE = '問題を削除する'
    EXIT = '削除終了'


class Problem:
    def __init__(self, sentence: str, ans_idx: int, choice_list: List[str]):
        self.sentence = sentence
        self.ans_idx = ans_idx
        self.choice_list = choice_list

    def tolist(self) -> List[str]:
        return [self.sentence, str(self.ans_idx)] + self.choice_list


class Game:
    def __init__(self):
        self.problem_list = []
        if os.path.isfile(PROBLEM_FILEPATH):
            with open(PROBLEM_FILEPATH, 'r') as f:
                for line in f:
                    cell_list = line.split(',')
                    self.problem_list.append(
                        Problem(cell_list[0], int(cell_list[1]), cell_list[2:]))

    def play(self, problem_list: List[Problem]):
        print()
        if len(problem_list) == 0:
            print('登録されている問題がありません\n')
            return
        for i, problem in enumerate(problem_list):
            print(f'[問題{i}] {problem.sentence}')
            correct = False
            while not correct:
                for j, choice in enumerate(problem.choice_list):
                    print(f'{j}) {choice}')
                input_ans = input_int(0, len(problem.choice_list) - 1)
                correct = input_ans == problem.ans_idx
                if correct:
                    print('O\n')
                else:
                    print('X\n')

    def play_normal(self):
        self.play(self.problem_list)

    def play_random(self):
        problem_list_copy = self.problem_list.copy()
        random.shuffle(problem_list_copy)
        self.play(problem_list_copy)

    def register(self):
        print('\n問題文を入力してください')
        input_sentence = ''
        while len(input_sentence) == 0:
            print('> ', end='')
            input_sentence = input().strip()
            print()
        input_choice_list = []
        menu_no = 0
        while list(RegisterMenu)[menu_no] != RegisterMenu.EXIT or len(input_choice_list) == 0:
            for i, menu in enumerate(RegisterMenu):
                print(f'{i}){menu.value} ', end='')
            print()
            menu_no = input_int(0, len(RegisterMenu) - 1)
            print()
            if list(RegisterMenu)[menu_no] == RegisterMenu.REGISTER:
                input_choice = ''
                while len(input_choice) == 0:
                    print(f'選択肢{len(input_choice_list)} > ', end='')
                    input_choice = input().strip()
                    print()
                input_choice_list.append(input_choice)
            if len(input_choice_list) == 0:
                print('最低1つ選択肢を登録してください\n')
        print('正解番号を入力してください')
        input_ans_idx = input_int(0, len(input_choice_list) - 1)
        self.problem_list.append(Problem(input_sentence, input_ans_idx, input_choice_list))
        lines = []
        for problem in self.problem_list:
            line = ','.join(problem.tolist())
            lines.append(line)
        with open(PROBLEM_FILEPATH, 'w') as f:
            f.write('\n'.join(lines))
        print()

    def delete(self):
        print()
        menu_no = 0
        while list(DeleteMenu)[menu_no] != DeleteMenu.EXIT:
            for i, menu in enumerate(DeleteMenu):
                print(f'{i}){menu.value} ', end='')
            print()
            menu_no = input_int(0, len(DeleteMenu) - 1)
            print()
            if list(DeleteMenu)[menu_no] == DeleteMenu.DELETE:
                if len(self.problem_list) > 0:
                    for i, problem in enumerate(self.problem_list):
                        print(f'{i}) {problem.sentence}')
                    print('消去する問題番号を入力してください')
                    no = input_int(0, len(self.problem_list) - 1)
                    self.problem_list.pop(no)
                    lines = []
                    for problem in self.problem_list:
                        line = ','.join(problem.tolist())
                        lines.append(line)
                    with open(PROBLEM_FILEPATH, 'w') as f:
                        f.write('\n'.join(lines))
                else:
                    print('登録されている問題がありません\n')


def main():
    print('-*-' * 15 + ' Rare Candy ' + '-*-' * 15)
    game = Game()
    menu_no = 0
    while list(FrontMenu)[menu_no] != FrontMenu.EXIT:
        for i, menu in enumerate(FrontMenu):
            print(f'{i}){menu.value} ', end='')
        print()
        menu_no = input_int(0, len(FrontMenu) - 1)
        if list(FrontMenu)[menu_no] == FrontMenu.PLAY_NORMAL:
            game.play_normal()
        elif list(FrontMenu)[menu_no] == FrontMenu.PLAY_RANDOM:
            game.play_random()
        elif list(FrontMenu)[menu_no] == FrontMenu.REGISATER:
            game.register()
        elif list(FrontMenu)[menu_no] == FrontMenu.DELETE:
            game.delete()
    print('### See you ###')


if __name__ == '__main__':
    main()