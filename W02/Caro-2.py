def KiemTraHoa(A, n):
    for i in range(n):
        for j in range(n):
            if A[i][j] == 0:
                return False
    return True
def KiemTraLine(line, player):
    dem = 0
    for i in line:
        if i == player:
            dem += 1
            if dem == 5:
                return True
        else:
            dem = 0
    return False
def KiemTraThang(A, player):
    for i in range(len(A)):
        if KiemTraLine(A[i], player) or KiemTraLine([A[j][i] for j in range(len(A))], player):
            return True
    for i in range(len(A) - 4):
        for j in range(len(A) - 4):
            line1 = [A[i + k][j + k] for k in range(5)]
            line2 = [A[i + k][j + 4 - k] for k in range(5)]

            if KiemTraLine(line1, player) or KiemTraLine(line2, player):
                return True
    return False


def NhapCo(A, player, n):
    x = int(input(f'Nguoi choi {player} nhap vi tri x: '))
    y = int(input(f'Nguoi choi {player} nhap vi tri y: '))

    if 0 <= x < n and 0 <= y < n and A[x][y] == 0:
        A[x][y] = player
        return True
    else:
        print("Vi tri khong hop le. Hay nhap lai.")
        return False


def DanhCo():
    while True:
        n = int(input('Nhap kich thuoc ban co (lon hon hoac bang 5): '))
        if n >= 5:
            break
        else:
            print('Kich thuoc khong hop le. Vui long nhap lai.')

    A = [[0] * n for _ in range(n)]

    player = '1'

    while True:
        if NhapCo(A, player, n):
            if KiemTraThang(A, player):
                print(f"Nguoi choi {player} thang!")
                for hang in A:
                    print(hang)
                break
            elif KiemTraHoa(A, n):
                print("Hoa!")
                for hang in A:
                    print(hang)
                break
            player = '1' if player == '2' else '2'


        for hang in A:
            print(hang)


# Gọi hàm DanhCo để chơi cờ Caro
DanhCo()
