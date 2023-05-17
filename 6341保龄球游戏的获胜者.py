player1=[9,7,10,7]



player2=[10,2,4,10]

class Solution:
    def isWinner(self, player1, player2) -> int:
        # 一个函数计算分数
        def calculate(player, score = 0):
            for i in range(len(player)):    
                #遍历循环一下
                if i == 1 and player[i-1] == 10:    
                    #特殊情况第一个是10
                    score += 2 * player[i]
                elif i-2 >= 0 and 10 in player[i - 2:i]:    
                    #前两个数字中有一个10
                    score += 2 * player[i]
                else:
                    #没有10
                    score += player[i]
            return score

        # 比较两位选手分数
        if calculate(player1) > calculate(player2):
            return 1
        elif calculate(player1) == calculate(player2):
            return 0
        else:
            return 2


